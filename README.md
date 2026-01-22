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
    