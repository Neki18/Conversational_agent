import json

def load_knowledge():
    with open("data/knowledge.json") as f:
        return json.load(f)

def retrieve_answer(query):
    kb = load_knowledge()

    text = str(kb).lower()

    if "price" in query or "plan" in query:
        return kb["pricing"]["basic"] + "\n" + kb["pricing"]["pro"]

    if "refund" in query:
        return kb["policies"]["refund"]

    if "support" in query:
        return kb["policies"]["support"]

    return "Let me help you with that."