import os
import random

def llm_api_key_access_function(debug=0):
    if debug >= 1:
        print(f"AI_001:llm_api_key_access_function - Function started")

    # Collect all available keys
    # apiKeys = [
    #     os.getenv("OPENAI_API_KEY_1"),
    #     os.getenv("OPENAI_API_KEY_2"),
    #     os.getenv("OPENAI_API_KEY_3"),
    #     os.getenv("OPENAI_API_KEY_4")
    # ]

    apiKeys = [
        os.getenv("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")                                                            
        
    ]

    # Filter out any None values
    validKeys = [key for key in apiKeys if key]

    if debug >= 2:
        print(f"AI_002:llm_api_key_access_function - Valid keys found: {len(validKeys)}")

    if not validKeys:
        if debug >= 1:
            print(f"AI_003:llm_api_key_access_function - No valid API keys found")
        return None

    selectedKey = random.choice(validKeys)

    if debug >= 2:
        print(f"AI_004:llm_api_key_access_function - Selected API key: {selectedKey}")

    return selectedKey
