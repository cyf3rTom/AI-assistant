def collect_user_inputs(emailId, username, subjectName, debug=1):
    debug = debug

    if debug >= 1:
        print("\n## Entering collect_user_inputs")
        print("AI_001:collect_user_inputs Initializing variables")

    mVar = "collect_user_inputs"
    inputData = {}

    if debug >= 1:
        print(f"AI_002:collect_user_inputs mVar  : {mVar}")

    try:
        inputData["emailId"] = emailId
        inputData["username"] = username
        inputData["subjectName"] = subjectName

        if debug >= 2:
            print(f"AI_003:collect_user_inputs inputData : {inputData}")

    except Exception as e:
        if debug >= 1:
            print(f"AI_004:collect_user_inputs Error collecting input data: {e}")

    if debug >= 1:
        print(f"AI_005:collect_user_inputs mVar SESSION(name): [{mVar}]")
        print("AI_006:collect_user_inputs Exiting collect_user_inputs")

    return inputData

