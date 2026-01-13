# NIST Compliance LLM Evaluation - Configuration Notes

## Optimal Temperature and Max Token Settings

### Task-Specific Recommendations

#### 1. Policy Generation (Notebook 1)
- **Current**: Temperature 0.7, Max Tokens 4096
- **Recommended**: Temperature 0.3, Max Tokens 3000
- **Rationale**: Policy generation requires consistency, accuracy, and adherence to structured formats. Lower temperature reduces randomness while maintaining some creativity for natural language flow.

#### 2. Scenario Generation (Notebook 2)
- **Current**: Not explicitly set (using defaults)
- **Recommended**: Temperature 0.8, Max Tokens 2500
- **Rationale**: Scenario generation benefits from higher creativity to produce diverse, realistic compliance situations while maintaining coherence.

#### 3. Compliance Judgment (Notebook 3)
- **Current**: Temperature 0.7, Max Tokens 4096
- **Recommended**: Temperature 0.2, Max Tokens 2000
- **Rationale**: Compliance evaluation requires high precision and consistency. Very low temperature ensures deterministic, accurate judgments based on policy rules.

### Model-Specific Adjustments

#### Claude Models (Anthropic)
- **Haiku (fast_cheap)**: Reduce max tokens by 20% due to shorter context preference
- **Sonnet (balanced)**: Use recommended settings as-is
- **Opus (premium)**: Can handle slightly higher complexity

#### Nova Models (AWS)
- **Pro**: Reduce temperature by 0.1 for more consistent outputs
- **Premier**: Use recommended settings as-is

### Implementation Example

```python
# Notebook 1: Policy Generation
TEMPERATURE = 0.3
MAX_TOKENS = 3000

# Notebook 2: Scenario Generation
TEMPERATURE = 0.8
MAX_TOKENS = 2500

# Notebook 3: Compliance Judgment
TEMPERATURE = 0.2
MAX_TOKENS = 2000

# Overnight Notebook Execution Guide

## SageMaker Studio Timeout Prevention

### 1. Keep-Alive Implementation
Add this cell at the beginning of your notebook:

```python
import time
import threading

def keep_alive():
    while True:
        time.sleep(300)  # 5 minutes
        print(f"Still running... {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Start keep-alive thread
thread = threading.Thread(target=keep_alive, daemon=True)
thread.start()

import time
from botocore.exceptions import ClientError


# Error Handling & Retry Logic
def bedrock_call_with_retry(func, max_retries=3, base_delay=2):
    for attempt in range(max_retries):
        try:
            return func()
        except ClientError as e:
            if e.response['Error']['Code'] == 'ThrottlingException':
                delay = base_delay * (2 ** attempt)
                print(f"Rate limit hit, waiting {delay}s...")
                time.sleep(delay)
            else:
                raise
    raise Exception("Max retries exceeded")


def log_progress(current, total, start_time):
    elapsed = time.time() - start_time
    rate = current / elapsed if elapsed > 0 else 0
    eta = (total - current) / rate if rate > 0 else 0
    
    print(f"Progress: {current}/{total} ({current/total*100:.1f}%) "
          f"Rate: {rate:.2f}/sec ETA: {eta/3600:.1f}h")



# Overnight runs - conservative settings for stability
SCENARIOS_PER_BATCH = 5  # Smaller batches
DELAY_BETWEEN_CALLS = 2  # Seconds
MAX_RETRIES = 5
CHECKPOINT_FREQUENCY = 10  # Save every 10 items
