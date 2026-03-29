from services.generator import generate_code
from services.runner import run_code
from services.evaluator import evaluate_code
from services.refiner import refine_prompt


def run_pipeline(problem, iterations=3):
    prompt = "Write a Python function to solve the problem."

    history = []

    for i in range(iterations):
        print(f"\n--- Iteration {i+1} ---")

        # 1. Generate
        code = generate_code(problem, prompt)

        # 2. Run
        passed, error = run_code(code)

        # 3. Save step
        history.append({
            "iteration": i + 1,
            "code": code,
            "passed": passed,
            "error": error
        })

        if passed:
            return {
                "success": True,
                "final_code": code,
                "history": history
            }

        # 4. Evaluate
        feedback = evaluate_code(problem, code, error)

        # 5. Refine prompt
        prompt = refine_prompt(prompt, feedback)

    return {
        "success": False,
        "final_code": code,
        "history": history
    }