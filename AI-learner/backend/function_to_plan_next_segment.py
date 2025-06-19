import re
import time
from datetime import datetime

def function_to_plan_next_segment(fileName, startPattern, endPattern, numSegments, waitPeriod, debug=0):
    if debug >= 1:
        print("AI_001:function_to_plan_next_segment - Function started")
        print(f"AI_002:function_to_plan_next_segment - Input fileName = {fileName}")
        print(f"AI_003:function_to_plan_next_segment - Input numSegments = {numSegments}")
        print(f"AI_004:function_to_plan_next_segment - Input waitPeriod = {waitPeriod}")

    try:
        with open(fileName, 'r') as file:
            content = file.read()

        if debug >= 2:
            print("AI_005:function_to_plan_next_segment - File content read successfully")

        startMatches = re.findall(startPattern, content)
        endMatches = re.findall(endPattern, content)

        if not startMatches or not endMatches:
            raise ValueError("Error: Data is not in the required format. 'Start:' or 'END:' patterns not found.")

        if debug >= 2:
            print(f"AI_006:function_to_plan_next_segment - Found {len(startMatches)} 'Start:' matches")
            print(f"AI_007:function_to_plan_next_segment - Found {len(endMatches)} 'END:' matches")

        segments = re.findall(f"{startPattern}.*?{endPattern}", content, re.DOTALL)

        if debug >= 2:
            print(f"AI_008:function_to_plan_next_segment - Extracted {len(segments)} segments")

        unsentSegments = [segment for segment in segments if "DateStamp:" not in segment]

        if debug >= 2:
            print(f"AI_009:function_to_plan_next_segment - Found {len(unsentSegments)} unsent segments")

        plannedSegments = unsentSegments[:numSegments]

        if debug >= 1:
            print(f"AI_010:function_to_plan_next_segment - Planned {len(plannedSegments)} segments")

        for i, segment in enumerate(plannedSegments):
            if debug >= 2:
                print(f"AI_011:function_to_plan_next_segment - Sending segment {i + 1}")
            time.sleep(waitPeriod)

        return plannedSegments

    except Exception as error:
        print("AI_012:function_to_plan_next_segment - Error occurred:")
        print(str(error))
        return []

