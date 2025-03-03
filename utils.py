import os
import dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain_groq import ChatGroq
from schema import Sections, State, Subtask_State
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.constants import Send


dotenv.load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model = 'llama3-8b-8192')


def get_youtube_transcript(yt_url):

    loader = YoutubeLoader.from_youtube_url(
    yt_url, add_video_info=False
    )

    return loader.load()[0].page_content



def get_planner():
    planner = llm.with_structured_output(Sections)
    return planner



def orchestrator(state: State):
    """Orchestrator that generates a plan for the Blog"""

    # Generate queries
    blog_sections = get_planner().invoke(
        [
            SystemMessage(content="Generate a plan for the Blog."),
            HumanMessage(content=f"Here is the Blog topic: {state['topic']}"),
        ]
    )

    print("Report Sections:",blog_sections)

    return {"sections": blog_sections.sections}


def sub_tasker(state: Subtask_State):
    """Worker writes a section of the Blog"""

    section = llm.invoke(
        [
            SystemMessage(
                content="Write a Blog section following the provided name and description. Include no preamble for each section. Use markdown formatting."
            ),
            HumanMessage(
                content=f"Here is the section name: {state['section'].name} and description: {state['section'].description}"
            ),
        ]
    )

    return {"completed_sections": [section.content]}

def synthesizer(state: State):
    """Synthesize full Blog from sections"""

    completed_sections = state["completed_sections"]

    completed_report_sections = "\n\n---\n\n".join(completed_sections)

    return {"final_blog": completed_report_sections}


def assign_workers(state: State):
    """Assign a worker to each section in the plan"""

    # Kick off section writing in parallel via Send() API
    return [Send("sub_tasker", {"section": s}) for s in state["sections"]]