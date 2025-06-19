# File: update_file_with_datestamp.py
import re
from datetime import datetime

def update_file_with_datestamp(fileName: str, segments: list, debug: int = 0):
    """
    Adds a DateStamp after Start: and END: markers for each segment in the file.
    """
    if debug >= 1:
        print(f"[DEBUG] update_file_with_datestamp started for {fileName}")

    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            content = f.read()
        if debug >= 2:
            print("[DEBUG] File content loaded successfully")

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_content = content

        for segment in segments:
            if debug >= 2:
                print(f"[DEBUG] Original segment: {segment}")

            # Insert DateStamp after Start:
            updated_segment = re.sub(
                r"(Start:.*?)(\n)",
                lambda m: f"{m.group(1)} DateStamp: {timestamp}{m.group(2)}",
                segment,
                flags=re.S
            )
            if debug >= 2:
                print(f"[DEBUG] After Start insertion: {updated_segment}")

            # Insert DateStamp after END:
            updated_segment = re.sub(
                r"(END:.*?)(\n)",
                lambda m: f"{m.group(1)} DateStamp: {timestamp}{m.group(2)}",
                updated_segment,
                flags=re.S
            )
            if debug >= 2:
                print(f"[DEBUG] After END insertion: {updated_segment}")

            updated_content = updated_content.replace(segment, updated_segment)

        if debug >= 1:
            print(f"[DEBUG] Writing updates back to {fileName}")
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        if debug >= 1:
            print(f"[DEBUG] update_file_with_datestamp completed for {fileName}")
    except Exception as e:
        print(f"[ERROR] update_file_with_datestamp failed: {e}")




# #update_file_with_datestamp1.py
# import re
# from datetime import datetime

# def update_file_with_datestamp(fileName, segments, debug=0):
#     if debug >= 1:
#         print("AI_001:update_file_with_datestamp - Function started")
#         print(f"AI_002:update_file_with_datestamp - Input fileName = {fileName}")

#     try:
#         with open(fileName, 'r') as file:
#             content = file.read()

#         if debug >= 2:
#             print("AI_003:update_file_with_datestamp - File content read successfully")

#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         print(f"DateStamp",timestamp)
#         updatedContent = content
#         print(f"updatedContent",updatedContent)
#         for segment in segments:
#             print(f"segment",segment)
#             updatedSegment = re.sub(r"(Start:.*?)(\n)", r"\1 DateStamp: " + timestamp + r"\2", segment)
#             print("updatedSegment after Start:", updatedSegment)
#             # Add DateStamp on the same line as END:
#             updatedSegment = re.sub(r"(END:.*?)(\n)", r"\1 DateStamp: " + timestamp + r"\2", updatedSegment)
#             print("updatedSegment after END:", updatedSegment)

#             updatedContent = updatedContent.replace(segment, updatedSegment)

#         print(f"updatedContent2",updatedContent)
#         if debug >= 2:
#             print("AI_004:update_file_with_datestamp - Segments updated with DateStamp")

#         with open(fileName, 'w') as file:
#             file.write(updatedContent)

#         if debug >= 1:
#             print(f"AI_005:update_file_with_datestamp - File updated successfully",fileName)

#     except Exception as error:
#         print("AI_006:update_file_with_datestamp - Error occurred:")
#         print(str(error))
