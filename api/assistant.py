import json
from pathlib import Path

def handler(request):
    if request.method != "POST":
        return {"statusCode": 405}

    body = json.loads(request.body)
    question = body.get("question", "").lower()

    data_path = Path(__file__).parent.parent / "data" / "concepts.json"
    concepts = json.loads(data_path.read_text())

    for key, value in concepts.items():
        if key in question:
            if "define" in question:
                return json_response(value["definition"])
            elif "example" in question:
                return json_response(value["example"])
            else:
                return json_response(value["definition"])

    return json_response("I couldn't find this topic. Try rephrasing.")

def json_response(message):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"response": message})
    }
