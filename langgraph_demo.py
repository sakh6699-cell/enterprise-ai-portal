# ==================================================
# LANGGRAPH DEMO
#
# Definition:
#
# LangGraph builds graph based workflows.
#
# Why?
#
# Controls execution flow.
#
# Interview:
#
# LangGraph enables stateful AI systems.
#
# ==================================================
from typing import TypedDict
from langgraph.graph import (
    StateGraph,
    END
)
# ==================================================
# STATE
# ==================================================
# Shared data
#
# between nodes
class AgentState(
    TypedDict
):
    question: str
    answer: str
# ==================================================
# NODE
# ==================================================
# Calculator node
def calculator_node(
        state
):
    q = state["question"]
    if "+" in q:
        result = eval(
            q
        )
        return {
            "answer":
            str(result)
        }
    return {
        "answer":
        "No Calculation"
    }
# ==================================================
# GRAPH
# ==================================================
builder = StateGraph(
    AgentState
)
builder.add_node(
    "calculator",
    calculator_node
)
builder.set_entry_point(
    "calculator"
)
builder.add_edge(
    "calculator",
    END
)
graph = builder.compile()
# ==================================================
# TEST
# ==================================================
result = graph.invoke(
    {
        "question":"5+5"
    }
)
print(
    result
)