import json
import re

STOPWORDS = {"the","is","in","and","to","of","a","for"}

def handler(request):
    body = json.loads(request.body)
    text = body.get("text", "")

    sentences = re.split(r'[.!?]', text)
    word_freq = {}

    for word in text.lower().split():
        if word not in STOPWORDS:
            word_freq[word] = word_freq.get(word, 0) + 1

    ranked = sorted(sentences, key=lambda s:
        sum(word_freq.get(w,0) for w in s.lower().split()),
        reverse=True)

    summary = ". ".join(ranked[:3])

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "summary": summary,
            "key_points": ranked[:5],
            "questions": [
                "What is the main idea?",
                "Explain briefly.",
                "Why is this important?"
            ]
        })
    }
