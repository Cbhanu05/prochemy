def run_code(code):
    try:
        local_env = {}

        exec(code, {}, local_env)

        functions = [v for v in local_env.values() if callable(v)]

        if not functions:
            return False, 0, "No function found"

        func = functions[0]

        tests = [
            ((2, 3), 5),
            ((10, 20), 30),
            ((-1, 1), 0),
        ]

        passed_count = 0
        total = len(tests)

        for inputs, expected in tests:
            try:
                result = func(*inputs)
                if result == expected:
                    passed_count += 1
            except:
                continue

        score = passed_count / total

        if score == 1:
            return True, score, "All tests passed"
        else:
            return False, score, f"{passed_count}/{total} tests passed"

    except Exception as e:
        return False, 0, str(e)