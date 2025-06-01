import re
from datetime import datetime

def update_file_with_datestamp(fileName, segments, debug=0):
    if debug >= 1:
        print("AI_001:update_file_with_datestamp - Function started")
        print(f"AI_002:update_file_with_datestamp - Input fileName = {fileName}")

    try:
        with open(fileName, 'r') as file:
            content = file.read()

        if debug >= 2:
            print("AI_003:update_file_with_datestamp - File content read successfully")

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DateStamp",timestamp)
        updatedContent = content
        print(f"updatedContent",updatedContent)
        for segment in segments:
            print(f"segment",segment)
            updatedSegment = re.sub(r"(Start:.*?)(\n)", r"\1 DateStamp: " + timestamp + r"\2", segment)
            print("updatedSegment after Start:", updatedSegment)
            # Add DateStamp on the same line as END:
            updatedSegment = re.sub(r"(END:.*?)(\n)", r"\1 DateStamp: " + timestamp + r"\2", updatedSegment)
            print("updatedSegment after END:", updatedSegment)

            updatedContent = updatedContent.replace(segment, updatedSegment)

        print(f"updatedContent2",updatedContent)
        if debug >= 2:
            print("AI_004:update_file_with_datestamp - Segments updated with DateStamp")

        with open(fileName, 'w') as file:
            file.write(updatedContent)

        if debug >= 1:
            print(f"AI_005:update_file_with_datestamp - File updated successfully",fileName)

    except Exception as error:
        print("AI_006:update_file_with_datestamp - Error occurred:")
        print(str(error))
