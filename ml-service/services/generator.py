from models.ollama_client import call_model

def generate_code(problem, prompt):
    full_prompt = f"""
You are an expert Python programmer.

{prompt}

Problem:
{problem}

Return ONLY valid Python code. No explanation.
"""

    return call_model("deepseek-coder:6.7b", full_prompt)