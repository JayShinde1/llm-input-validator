import json
import sys
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def load_input_json(file_path: str) -> str:
    """Load and return input JSON as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.dumps(json.load(f))


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_user.py <input_json_file>")
        sys.exit(1)

    input_json = load_input_json(sys.argv[1])

    with open("prompts/validator.txt", "r", encoding="utf-8") as f:
        prompt_text = f.read()

    prompt = PromptTemplate(
        template=prompt_text,
        input_variables=["input_json"]
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        response_mime_type="application/json",
        temperature=0
    )

    chain = prompt | model | StrOutputParser()

    try:
        raw_output = chain.invoke({"input_json": input_json})

        parsed_output = json.loads(raw_output)

        print(json.dumps(parsed_output, indent=2))

    except json.JSONDecodeError:
        print(json.dumps({
            "is_valid": False,
            "errors": ["system_error: invalid LLM JSON output"],
            "warnings": []
        }, indent=2))


if __name__ == "__main__":
    main()
