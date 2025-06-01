import os

def check_file_exists(fileName, debug=0):
    if debug >= 1:
        print("AI_001:check_file_exists - Function started")
        print(f"AI_002:check_file_exists - Input fileName = {fileName}")

    try:
        fileExists = os.path.isfile(fileName)

        if debug >= 2:
            print(f"AI_003:check_file_exists - os.path.isfile result = {fileExists}")

        if fileExists:
            if debug >= 1:
                print("AI_004:check_file_exists - File exists")
            return 1
        else:
            if debug >= 1:
                print("AI_005:check_file_exists - File does not exist")
            return 0

    except Exception as error:
        if debug >= 1:
            print(f"AI_006:check_file_exists - Error occurred: {error}")
        return 0