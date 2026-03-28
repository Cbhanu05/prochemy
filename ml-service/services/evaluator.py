from models.ollama_client import call_model

def evaluate_code(problem, code, error):
    prompt = f"""
You are a code evaluator.

Problem:
{problem}

Generated Code:
{code}

Error =  "Expected add(2,3)=5 but got wrong result"

Explain clearly:
1. Why it failed
2. What is wrong
3. What is missing
"""

    return call_model("mistral:7b", prompt)