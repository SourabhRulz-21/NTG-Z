import json
from pathlib import Path

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    body = json.loads(request.body)
    question = body.get("question", "").lower()

    data_path = Path("data/concepts.json")
    concepts = json.loads(data_path.read_text())

    for key, value in concepts.items():
        if key in question:
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({
                    "response": value["definition"]
                })
            }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "response": "Topic not found. Try rephrasing."
        })
    }
