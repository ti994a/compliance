def judge_scenarios(source_scenarios: List[Dict], model_arn: str, kb_id: str = KNOWLEDGE_BASE_ID) -> List[Dict]:
    """
    Process scenarios and add judgment fields.
    """

    # Extract model ID from ARN (Converse API requires model ID, not full ARN)
    model_id = model_arn.split('/')[-1] if '/' in model_arn else model_arn
    
    judged_scenarios = []
    for scenario in source_scenarios:
        judged_scenario = scenario.copy()

        # Extract policy IDs from scenario and pull the policy data from the knowledge base
        import re
        policy_match = re.search(r'Policies referenced: (.+)', scenario["scenario-detail"])
        if policy_match:
            policy_ids = [p.strip().replace('policy_', '') for p in policy_match.group(1).split(',')]
            retrieved_policies = retrieve_policies_by_id(policy_ids, kb_id)
        else:
            print(f"No policies referenced in scenario: {scenario['scenario-detail']}")
            continue
                
        prompt = f"""
        You are **ComplianceEvaluator**, an expert AI compliance analyst specializing in NIST 800-53 controls and policies. 
        Your mission is to judge organizational policy scenarios against reference policies stored in your knowledge base.
                
        **Your Expertise:**
        - Deep understanding of all NIST 800-53 Rev. 5 control families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR)
        - Policy-to-control mapping and compliance evaluation
        - Evidence-focused assessment methodology

        **Task:** Judge if the scenario complies with ALL referenced policies from your knowledge base.

        **Avoid judging scenarios based on cost-benefit principles or concentration percentages.
    
        **Note that non-US citizens cannot obtain US security clearances.**
        
        **Response Format:**
        {{
          "judged-compliant": true/false, true if you determined the scenario is compliant with the organizational 
        policies stored in your knowledge base.  false if the scenario is not compliant.
          "judged-compliant-reason": "Empty if compliant. If the scenario is not compliant, explain very briefly why it is not compliant, citing
          exactly the policy ID(s) is violates, followed by the extracted policy text that indicates non-compliance."
        }}

        **Evaluate scenario against this policy data**:
        {retrieved_policies}

        **Here is the actual compliance scenario to judge**:
        {scenario["scenario-detail"]}
        """
        
        messages = [{"role": "user", "content": [{"text": prompt}]}]
        
        while True:
            response = bedrock_runtime.converse(
                modelId=model_id,
                messages=messages,
                toolConfig=TOOL_CONFIG,
                inferenceConfig={
                    "maxTokens": MAX_TOKENS,
                    "temperature": TEMPERATURE
                }
            )
            
            if response['stopReason'] == 'tool_use':
                tool_results = []
                for content_block in response['output']['message']['content']:
                    if 'toolUse' in content_block:
                        tool_name = content_block['toolUse']['name']
                        tool_use_id = content_block['toolUse']['toolUseId']
                        
                        if tool_name == 'compliance_calculator':
                            expression = content_block['toolUse']['input']['expression']
                            result = compliance_calculator(expression)
                            tool_results.append({
                                "toolResult": {
                                    "toolUseId": tool_use_id,
                                    "content": [{"text": result}]
                                }
                            })
                        elif tool_name == 'judged_scenario_json':
                            tool_result = content_block['toolUse']['input']
                            judged_scenario["judged-compliant"] = tool_result['scenarios'][0]['judged-compliant']
                            judged_scenario["judged-compliant-reason"] = tool_result['scenarios'][0]['judged-compliant-reason']
                            break
                
                if tool_results:
                    messages.append({"role": "assistant", "content": response['output']['message']['content']})
                    messages.append({"role": "user", "content": tool_results})
                else:
                    break
            else:
                break

        judged_scenario["llm-judge"] = MODEL_ARN.split('/')[-1]
        judged_scenario["judged-dtm"] = datetime.datetime.now().isoformat()
        judged_scenarios.append(judged_scenario)
    
    return judged_scenarios