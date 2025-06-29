def write_to_file(fileName, contentList, debug=0):
    if debug >= 1:
        print("AI_001:write_to_file - Function started")
        print(f"AI_002:write_to_file - Input fileName = {fileName}")
        print(f"AI_003:write_to_file - Number of lines to write = {len(contentList)}")

    try:
        with open(fileName, 'w', encoding='utf-8') as file:
            for index, line in enumerate(contentList):
                file.write(f"{line}\n")
                if debug >= 2:
                    print(f"AI_004:write_to_file - Line {index + 1}: {line}")

        if debug >= 1:
            print("AI_005:write_to_file - File written successfully")

    except Exception as error:
        if debug >= 1:
            print(f"AI_006:write_to_file - Error occurred: {error}")