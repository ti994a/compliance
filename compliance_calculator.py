import re

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