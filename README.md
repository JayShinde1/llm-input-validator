# LLM Input Validator

## Overview
This project implements an **LLM-based input validation system**.
All validation logic is delegated to the language model through prompt engineering.

No traditional validation libraries are used — the LLM is the **only validator**.

---

## How It Works
1. `validate_user.py` reads an input JSON file
2. The input is injected into a strict validation prompt (`validator.txt`)
3. The LLM validates the input based on real-world standards
4. The model returns structured JSON containing:
   - `is_valid`
   - `errors`
   - `warnings`
5. The script parses and prints the final output

---

## Project Structure

![Project Structure](screenshot\image.png)

---

## Running the Validator

### Requirements
- Python 3.10+
- Valid Gemini API key (set as environment variable)

### Run
```bash
python validate_user.py user.json
Example Output
{
  "is_valid": false,
  "errors": ["name is required"],
  "warnings": ["age is below 18 years"]
}
Prompt Evaluations
Prompt behavior is evaluated using promptfoo.

Evaluations are defined in evals/promptfooconfig.yaml

The same prompt (validator.txt) is reused for runtime and evals

Assertions focus on semantic correctness using substring matching
to handle LLM phrasing variance

Run Evals
npx promptfoo eval -c evals/promptfooconfig.yaml

