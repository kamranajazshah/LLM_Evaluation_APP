from pydantic import BaseModel, Field
from typing import Optional

class Evaluation(BaseModel):
    input: str
    ai_output: str
    actual_output: str
    factual: Optional[int] = Field(default=None)
    coherance: Optional[int] = Field(default=None)
    relevance: Optional[int] = Field(default=None)

class Api(BaseModel):
    input: str
    ai_output: str
    actual_output: str
