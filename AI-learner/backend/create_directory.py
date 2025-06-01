import os

def create_directory(directoryName, debug=1):
    debug = debug

    if debug >= 1:
        print("\n## Entering create_directory")
        print("AI_001:create_directory Initializing variables")

    mVar = "create_directory"
    dirPath = directoryName

    if debug >= 1:
        print(f"AI_002:create_directory mVar       : {mVar}")
        print(f"AI_003:create_directory directory : {dirPath}")

    try:
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
            if debug >= 1:
                print(f"AI_004:create_directory Directory created: {dirPath}")
        else:
            if debug >= 1:
                print(f"AI_005:create_directory Directory already exists: {dirPath}")
    except Exception as e:
        if debug >= 1:
            print(f"AI_006:create_directory Error creating directory: {e}")

    if debug >= 1:
        print(f"AI_007:create_directory mVar SESSION(name): [{mVar}]")
        print("AI_008:create_directory Exiting create_directory")