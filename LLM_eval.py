from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from schema import Evaluation
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(temperature=0)

parser = PydanticOutputParser(pydantic_object=Evaluation)

prompt = PromptTemplate(
    template="""
You are an LLM evaluator.

Evaluate the AI's response to a user input by comparing it with the actual answer.

Give a score between 0 and 10 for:
- factual: Is the AI's answer factually correct?
- coherance: Is the answer well-structured and clear?
- relevance: Is the answer relevant to the input question?

### INPUT ###
User question: {input}
AI answer: {ai_output}
Actual correct answer: {actual_output}

### FORMAT ###
Respond with a valid JSON like this:
{{
  "input": "original input",
  "ai_output": "response from AI",
  "actual_output": "actual expected answer",
  "factual": 4,
  "coherance": 7,
  "relevance": 6
}}

{format_instructions}
""",
    input_variables=["input", "ai_output", "actual_output"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser
