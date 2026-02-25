# LLM Stack Workshop 1: Information Extraction Pipeline

This project demonstrates how to build an LLM-powered information extraction pipeline using Python, Streamlit, and OpenRouter.

## Project Structure

- `scripts/task_1_chatbot.py`: A simple Streamlit chatbot using OpenRouter or GoogleAI Studio.
- `scripts/task_2_structure_output.py`: A script that loads the `pythainlp/thaisum` dataset and extracts structured information (sentiment, summary, entities, relations) into a JSONL file.
- `pyproject.toml`: Project dependencies managed by `uv`.
- `Dockerfile` & `docker-compose.yml`: Containerization setup.

## Setup

```bash
# Build the images
docker-compose build

# Run Task 1 (Chatbot)
docker-compose up chatbot

# Run Task 2 (Structured Extraction)
docker-compose run extractor
```