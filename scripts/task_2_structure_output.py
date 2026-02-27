from openai import OpenAI
from pydantic import BaseModel

import tqdm
import json

OUTPUT_FILE = "output.jsonl"
DATASET_FILE = "sample/sample_thaisum.json"
client = OpenAI(
    api_key=...,
    base_url="https://openrouter.ai/api/v1",
)

### Task
# - Extract infomration from News (thaisum.json) using LLM "Tool calling" approach
# - Save each result into output.jsonl


# sentiment, summary, people name, Relation Extraction, Event Extraction
class ExtractedData(BaseModel):
    pass


schema = json.dumps(ExtractedData.model_json_schema())

tools = ...
system_prompt = ...

with open(DATASET_FILE, "r", encoding="utf-8") as f:
    dataset = json.load(f)

for sample in tqdm.tqdm(dataset):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": sample},
        ],
        temperature=0,
    )

    meesage = response.choices[0].message

    extracted_data = json.loads(content)
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(extracted_data, ensure_ascii=False) + "\n")
