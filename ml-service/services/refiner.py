from models.ollama_client import call_model

def refine_prompt(old_prompt, feedback):
    prompt = f"""
You are a prompt engineer.

Original Prompt:
{old_prompt}

Feedback:
{feedback}

Improve the prompt so that the model avoids these mistakes.
Make it clearer and more structured.
"""

    return call_model("mistral:7b", prompt)