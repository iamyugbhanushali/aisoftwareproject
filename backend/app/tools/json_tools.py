import json

def parse_agent_response(response):

    try:
        return json.loads(response)

    except Exception as e:
        print("JSON PARSE ERROR")
        print(e)

        return None