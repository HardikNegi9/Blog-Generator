from langgraph.graph import StateGraph, START, END
from schema import State
from utils import orchestrator, sub_tasker, synthesizer, assign_workers, get_youtube_transcript
from IPython.display import Markdown

# Build workflow
orchestrator_worker_builder = StateGraph(State)

# Add the nodes
orchestrator_worker_builder.add_node("orchestrator", orchestrator)
orchestrator_worker_builder.add_node("sub_tasker", sub_tasker)
orchestrator_worker_builder.add_node("synthesizer", synthesizer)

# Add edges to connect nodes
orchestrator_worker_builder.add_edge(START, "orchestrator")
orchestrator_worker_builder.add_conditional_edges(
    "orchestrator", assign_workers, ["sub_tasker"]
)
orchestrator_worker_builder.add_edge("sub_tasker", "synthesizer")
orchestrator_worker_builder.add_edge("synthesizer", END)

# Compile the workflow
orchestrator_worker = orchestrator_worker_builder.compile()


def generate_markdown(input_text):
    state = orchestrator_worker.invoke({"topic": "Create a report on Blog Generation using LangGraph"})
    # print(state["final_blog"])
    return state["final_blog"]

