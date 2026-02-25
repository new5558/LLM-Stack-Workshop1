from openai import OpenAI
from pydantic import BaseModel

import tqdm
import json

OUTPUT_FILE = "output.jsonl"
DATASET_FILE = "sample/sample_thaisum.json"
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
)


# sentiment, summary, people name, Relation Extraction, Event Extraction
class ExtractedData(BaseModel):
    sentiment: str
    summary: str
    people_name: list[str]
    relation_extraction: list[tuple[str, str, str]]
    event_extraction: list[tuple[str, str, str]]


schema = json.dumps(ExtractedData.model_json_schema())

system_prompt = f"""
You are an expert information extraction system. Analyze the provided text and extract structured data.
Your output must be a valid JSON object that follows this schema:
{schema}

Ensure that:
- 'sentiment' is the overall tone of the text.
- 'summary' is a concise summary.
- 'people_name' is a list of names mentioned.
- 'relation_extraction' is a list of tuples (subject, relation, object).
- 'event_extraction' is a list of tuples (event, time, location).
"""

with open(DATASET_FILE, "r", encoding="utf-8") as f:
    dataset = json.load(f)

for sample in tqdm.tqdm(dataset):
    response = client.chat.completions.create(
        model="qwen/qwen3-235b-a22b-2507",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": sample},
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    extracted_data = json.loads(content)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(extracted_data, ensure_ascii=False) + "\n")
