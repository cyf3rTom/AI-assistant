import os

def check_directory_exists(directoryName, debug=1):
    debug = debug

    if debug >= 1:
        print("\n## Entering check_directory_exists")
        print("AI_001:check_directory_exists Initializing variables")

    mVar = "check_directory_exists"
    dirExists = False

    if debug >= 1:
        print(f"AI_002:check_directory_exists mVar : {mVar}")
        print(f"AI_003:check_directory_exists directoryName : {directoryName}")

    try:
        dirExists = os.path.isdir(directoryName)

        if debug >= 2:
            print(f"AI_004:check_directory_exists os.path.isdir result : {dirExists}")

    except Exception as e:
        if debug >= 1:
            print(f"AI_005:check_directory_exists Error checking directory: {e}")

    if debug >= 1:
        print(f"AI_006:check_directory_exists mVar SESSION(name): [{mVar}]")
        print("AI_007:check_directory_exists Exiting check_directory_exists")

    return dirExists