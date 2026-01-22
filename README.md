# LLM Input Validator

## Overview
This project implements an LLM-based input validation system.
All validation logic is delegated to the language model via prompt engineering.

## How it works
- `validate_user.py` loads input JSON and sends it to the LLM
- `validator.txt` defines validation rules and output format
- The LLM returns structured JSON with errors and warnings

## Running the validator
```bash
python validate_user.py user.json


file structure: 

## Project Structure
![Project Stucture](/screenshot/image.png)


---

## How It Works
1. `validate_user.py` reads an input JSON file
2. The input is injected into a strict validation prompt (`validator.txt`)
3. The LLM validates the input and returns structured JSON:
   - `is_valid`
   - `errors`
   - `warnings`
4. The script parses and prints the final result

---

## Running the Validator

### Requirements
- Python 3.10+
- Valid API key for Gemini (runtime)

### Run
```bash
python validate_user.py user.json


Example output:
{
  "is_valid": false,
  "errors": ["name is required"],
  "warnings": ["age is below 18 years"]
}

Prompt Evaluations

Prompt behavior is evaluated using promptfoo.

Evals are defined in evals/promptfooconfig.yaml

The same prompt (validator.txt) is reused

Assertions check semantic correctness using substring matching

Run evals
npx promptfoo eval -c evals/promptfooconfig.yaml