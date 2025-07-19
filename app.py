from fastapi import FastAPI
from schema import Api
from LLM_eval import chain

app = FastAPI()

@app.post("/evaluate")
def evaluate(state: Api):
    response = chain.invoke({
        "input": state.input,
        "ai_output": state.ai_output,
        "actual_output": state.actual_output
    })
    return response
