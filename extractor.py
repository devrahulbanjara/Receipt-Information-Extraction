import os
from dotenv import load_dotenv
from google import genai
from prompts.prompt import EXTRACTION_PROMPT, EXTRACTION_KEYS_WITH_DESCRIPTIONS

load_dotenv()


API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
prompt = EXTRACTION_PROMPT.format(EXTRACTION_KEYS_WITH_DESCRIPTIONS)
my_file = client.files.upload(file="data/mango.png")


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[my_file, prompt],
)

print(response.text)
