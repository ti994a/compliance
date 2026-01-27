import re

COMPLIANCE_JUDGE_PROMPT = """
You are **ComplianceEvaluator**, an expert AI compliance analyst specializing in NIST 800-53 controls and policies. 
Your mission is to judge organizational policy scenarios against reference policies stored in your knowledge base.
        
**Your Expertise:**
- Deep understanding of all NIST 800-53 Rev. 5 control families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR)
- Policy-to-control mapping and compliance evaluation
- Evidence-focused assessment methodology

**Task:** Judge if the scenario complies with ALL referenced policies from your knowledge base.

**Avoid judging scenarios based on cost-benefit principles or concentration percentages.

**Note that non-US citizens cannot obtain US security clearances.**

**CRITICAL: When comparing timeframes, values, or thresholds:**
- If a scenario meets or exceeds (performs better than) policy requirements, it is COMPLIANT
- 
- If a policy requires "at least quarterly (90 days)" and scenario shows "95 days", this is NON-COMPLIANT (95 > 90)
- Always use the compliance_calculator tool to verify numerical comparisons when in doubt

**CRITICAL: For ANY numerical comparison involving timeframes, values, or thresholds:**
- ALWAYS use the compliance_calculator tool to verify comparisons - do not do mental math
- If a scenario meets or exceeds (performs better than) policy requirements, it is COMPLIANT.  For example, if a policy requires "within 24 hours" and scenario shows "within 18 hours", this is COMPLIANT (18 < 24).
- If a scenario does not meet policy requirements it is NON-COMPLIANT.  For example, if a policy requires "at least quarterly (90 days)" and scenario shows "95 days", this is NON-COMPLIANT (95 > 90)

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
{scenario_detail}
"""


def compliance_calculator(expression: str) -> str:
    """Calculate with unit conversions for compliance scenarios"""
    
    # Unit conversion factors to base units
    conversions = {
        # Time (to seconds)
        'ms': 0.001, 'milliseconds': 0.001, 'millisecond': 0.001,
        's': 1, 'sec': 1, 'seconds': 1, 'second': 1,
        'min': 60, 'minutes': 60, 'minute': 60,
        'h': 3600, 'hr': 3600, 'hours': 3600, 'hour': 3600,
        'days': 86400, 'day': 86400,
        'weeks': 604800, 'week': 604800,
        'months': 2592000, 'month': 2592000,
        'years': 31536000, 'year': 31536000,
        'quarterly': 7776000,  # 90 days
        'annually': 31536000,  # 365 days  
        'yearly': 31536000,    # 365 days
        'biweekly': 1209600,   # 14 days
        'weekly': 604800,      # 7 days
        'daily': 86400,        # 1 day
        'continuous': 0,  # Special case for always-on
        'real_time': 1,   # 1 second
        'immediate': 1,   # 1 second
        'monthly': 2592000,  # 30 days
        'semiannually': 15768000,  # 182.5 days
        'biennially': 63072000,  # 2 years
        
        # Money (to dollars)
        'cents': 0.01, 'cent': 0.01,
        '$': 1, 'dollars': 1, 'dollar': 1, 'usd': 1,
        'k': 1000, 'thousand': 1000,
        'm': 1000000, 'million': 1000000,
        'b': 1000000000, 'billion': 1000000000,
        
        # Data (to bytes)
        'b': 1, 'bytes': 1, 'byte': 1,
        'kb': 1024, 'mb': 1048576, 'gb': 1073741824, 'tb': 1099511627776,
        
        # Percentages
        '%': 0.01, 'percent': 0.01, 'percentage': 0.01,

        # Security/Compliance specific units
        'business_days': 86400,  # 1 day (business day = calendar day for calculations)
        'working_days': 86400,   # 1 day
        'calendar_days': 86400,  # 1 day
        
        # Network/Performance units  
        'bps': 1, 'bits_per_second': 1,
        'kbps': 1000, 'mbps': 1000000, 'gbps': 1000000000,
    }
    
    def parse_value(text):
        # Extract number and unit
        match = re.match(r'([\d.]+)\s*([a-zA-Z%$]+)?', text.strip())
        if not match:
            return float(text)
        
        number = float(match.group(1))
        unit = match.group(2).lower() if match.group(2) else ''
        
        return number * conversions.get(unit, 1)
    
    try:
        # Handle comparisons
        if any(op in expression for op in ['>', '<', '>=', '<=', '==', '!=']):
            for op in ['>=', '<=', '==', '!=', '>', '<']:
                if op in expression:
                    left, right = expression.split(op, 1)
                    left_val = parse_value(left)
                    right_val = parse_value(right)
                    
                    if op == '>': return str(left_val > right_val)
                    elif op == '<': return str(left_val < right_val)
                    elif op == '>=': return str(left_val >= right_val)
                    elif op == '<=': return str(left_val <= right_val)
                    elif op == '==': return str(left_val == right_val)
                    elif op == '!=': return str(left_val != right_val)
        
        # Handle arithmetic
        for op in ['+', '-', '*', '/']:
            if op in expression:
                left, right = expression.split(op, 1)
                left_val = parse_value(left)
                right_val = parse_value(right)
                
                if op == '+': return str(left_val + right_val)
                elif op == '-': return str(left_val - right_val)
                elif op == '*': return str(left_val * right_val)
                elif op == '/': return str(left_val / right_val)
        
        # Single value conversion
        return str(parse_value(expression))
        
    except Exception as e:
        return f"Error: {str(e)}"

# Tool configuration
CALCULATOR_TOOL = {
    "toolSpec": {
        "name": "compliance_calculator",
        "description": "Calculate and compare values with time, money, data, and percentage units",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Expression like '800ms < 1s' or '4m > 3b'"}
                },
                "required": ["expression"]
            }
        }
    }
}

####################
def print_color(text, color='white'):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m', 
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m'
    }
    reset = '\033[0m'
    print(f"{colors.get(color, colors['white'])}{text}{reset}")

# Usage:
# print_color("Error message", 'red')
# print_color("Success message", 'green')
# print_color("Warning message", 'yellow')
