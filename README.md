# 🧠 LLM Evaluation App

A web application to **evaluate the quality of LLM (Large Language Model) responses** based on:

- ✅ Factuality
- 🔄 Coherence
- 🎯 Relevance

This project uses **FastAPI**, **LangChain**, **Pydantic**,**Streamlit** for UI and **OpenAI GPT models** to analyze how accurately and logically an LLM's response matches a user query and a reference answer.

![LLM Evaluation Screenshot](https://github.com/kamranajazshah/LLM_Evaluation_APP/blob/main/Screenshot%202025-07-19%20205800.png?raw=true)


---

## 📖 Overview

### ❓ What Problem Does It Solve?

LLMs often produce fluent but inaccurate or irrelevant responses. This app enables you to:
- Input a **user query**, the **AI's response**, and the **ground truth**
- Receive an evaluation of how good the response is
- Use this feedback to refine prompts, retrain models, or benchmark LLMs

### 🧪 What Does It Measure?

Each AI response is rated on:
| Metric      | Description |
|-------------|-------------|
| **Factuality** | Is the information factually correct? |
| **Coherence** | Is the sentence logically and grammatically well-formed? |
| **Relevance** | Does the response address the input prompt? |

The output is a **numerical score from 1 to 10** for each dimension.

### 🔁 Workflow Diagram

```text
[User Input]
     |
     v
[FastAPI Backend]
     |
     v
[LangChain Prompts]
     |
     v
[OpenAI GPT Model]
     |
     v
[Response Scoring: Factual, Coherent, Relevant]
     |
     v
[Return JSON or Rendered UI Output]
