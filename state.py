from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    intent: str
    user_info: dict
    stage: str