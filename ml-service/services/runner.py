def run_code(code):
    try:
        local_env = {}

        exec(code, {}, local_env)

        # get all functions defined
        functions = [v for v in local_env.values() if callable(v)]

        if not functions:
            return False, "No function found"

        func = functions[0]  # take first function

        # simple test (can expand later)
        try:
            result = func(2, 3)

            if result == 5:
                return True, "Passed"
            else:
                return False, f"Wrong output: got {result}, expected 5"

        except Exception as e:
            return False, f"Runtime error: {str(e)}"

    except Exception as e:
        return False, str(e)