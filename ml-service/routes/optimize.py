from fastapi import APIRouter
from services.generator import generate_code
from services.evaluator import evaluate_code
from services.refiner import refine_prompt

router = APIRouter()

@router.post("/optimize")
def optimize(data: dict):
    problem = data.get("problem")
    prompt = data.get("prompt", "Write a Python function.")

    code = generate_code(problem, prompt)

    # Step 2: Fake error (temporary)
    error = "Expected correct output but got wrong result"

    feedback = evaluate_code(problem, code, error)

    new_prompt = refine_prompt(prompt, feedback)

    return {
        "generated_code": code,
        "feedback": feedback,
        "refined_prompt": new_prompt
    }