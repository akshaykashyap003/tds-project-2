# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "chardet",
#   "pandas",
#   "seaborn",
#   "matplotlib",
#   "ipykernel",
#   "openai",
#   "requests",
# ]
# ///

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import requests
import chardet
from openai import ChatCompletion

# Step 1: Load the AIPROXY_TOKEN
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN") or "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjEwMDE4NTNAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.3UAeJMA-I52V2PVe3mGIW4ghug6VzHAJ34xuv2fsK34"
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN is not set.")
    sys.exit(1)

# Step 2: Configure OpenAI Proxy
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AIPROXY_TOKEN}",
}

# Step 3: Detect Encoding and Load CSV File
def detect_encoding(file_path):
    """Detect the encoding of a CSV file."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def load_csv_with_detected_encoding(file_path):
    """Load a CSV file with the detected encoding."""
    encoding = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except UnicodeDecodeError:
        print(f"Failed to decode {file_path} with encoding {encoding}. Trying 'utf-8-sig'.")
        df = pd.read_csv(file_path, encoding='utf-8-sig')  # Fallback to 'utf-8-sig'
        return df

if len(sys.argv) < 2:
    print("Usage: python autolysis.py <dataset.csv>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    data = load_csv_with_detected_encoding(file_path)
    print(f"DataFrame loaded successfully. First few rows:\n{data.head()}")
except Exception as e:
    print(f"Error loading file {file_path}: {e}")
    sys.exit(1)

# Step 4: Basic Data Analysis
summary = {
    "columns": list(data.columns),
    "dtypes": data.dtypes.astype(str).to_dict(),
    "summary_stats": data.describe(include='all').to_dict(),
    "missing_values": data.isnull().sum().to_dict(),
}

# Step 5: Interact with LLM for Insights
def ask_llm(prompt):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

llm_prompt = f"Analyze the following dataset summary and suggest key insights and visualizations: {summary}"
analysis_insights = ask_llm(llm_prompt)

# Step 6: Generate Visualizations
plt.figure(figsize=(10, 6))
data.isnull().sum().plot(kind='bar', color='skyblue')
plt.title("Missing Values per Column")
plt.savefig("missing_values.png")

# Step 7: Create a Markdown Narrative
readme_content = f"""# Automated Analysis Results

## Dataset Overview
Columns: {', '.join(summary['columns'])}

## Data Types
{summary['dtypes']}

## Summary Statistics
{summary['summary_stats']}

## Missing Values
{summary['missing_values']}

## Insights
{analysis_insights}

## Visualizations
![Missing Values](missing_values.png)
"""

# Save Markdown File
with open("README.md", "w") as f:
    f.write(readme_content)

print("Analysis complete. Outputs saved as README.md and *.png files.")
