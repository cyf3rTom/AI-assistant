import openai
from llm_api_key_access_function import llm_api_key_access_function

def fetch_data_from_llm(taskPrompt, debug=0):
    if debug >= 1:
        print(f"AI_001:fetch_data_from_llm - Function started")
        print(f"AI_002:fetch_data_from_llm - taskPrompt = {taskPrompt[:50]}...")

    openai.api_key = llm_api_key_access_function()

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": taskPrompt}
            ]
        )

        result = response['choices'][0]['message']['content']

        if debug >= 1:
            print("AI_003:fetch_data_from_llm - Response received successfully")

        if debug >= 2:
            print(f"AI_004:fetch_data_from_llm - Full response: {result}")

        return result

    except Exception as error:
        print("AI_005:fetch_data_from_llm - Error occurred:")
        print(str(error))
        return ""