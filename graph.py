from langgraph.graph import StateGraph, END
from nodes import intent_node, rag_node, lead_node

def build_graph():
    builder = StateGraph(dict)

    builder.add_node("intent", intent_node)
    builder.add_node("rag", rag_node)
    builder.add_node("lead", lead_node)

    builder.set_entry_point("intent")

    # Decide where to go
    builder.add_conditional_edges(
        "intent",
        lambda state: state["intent"],
        {
            "rag": "rag",
            "lead": "lead"
        }
    )

    # ✅ IMPORTANT: STOP after execution
    builder.add_edge("rag", END)
    builder.add_edge("lead", END)

    return builder.compile()