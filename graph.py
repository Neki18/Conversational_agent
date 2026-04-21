from langgraph.graph import StateGraph
from nodes import intent_node, rag_node, lead_node

def build_graph():
    builder = StateGraph(dict)

    builder.add_node("intent", intent_node)
    builder.add_node("rag", rag_node)
    builder.add_node("lead", lead_node)

    builder.set_entry_point("intent")

    builder.add_edge("intent", "rag")
    builder.add_edge("rag", "lead")

    return builder.compile()