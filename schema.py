from typing_extensions import TypedDict, List
from typing import Annotated
from pydantic import BaseModel, Field
import operator


class Section(BaseModel):
  name: str = Field(
      description = "Section of The blog.",
  )
  description: str = Field(
      description = "Brief overview of the main topics and concepts to be covered in this section.",
  )


class Sections(BaseModel):
  sections: List[Section] = Field(
      description = "List of sections to be covered in the blog.",
    )


class State(TypedDict):
  topic: str = Field(
      description = "The topic of the blog.",
  )
  sections: Sections = Field(
      description = "List of sections to be covered in the blog.",
  )
  completed_sections: Annotated[list , operator.add] = Field(
      description = "List of sections that have been completed.",
  )
  final_blog: str = Field(
      description = "The final blog.",
  )


class Subtask_State(BaseModel):
  section: Section = Field(
      description = "The section of the blog.",
  )
  completed_sections: Annotated[list , operator.add] = Field(
      description = "List of sections that have been completed.",
  )
  completed_section: str = Field(
      description = "The completed section of the blog.",
  )



