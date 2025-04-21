from dotenv import load_dotenv
import os
from google import genai
from etl import get_dataframe

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")


def get_gemini_response(question):
    """
    This function uses the Google Gemini API to get a response for a given input.
    """
    try:
        instructions = "You are a financial analyst. Answer the question based on the data provided."
        dataframe = get_dataframe().to_string()
        client = genai.Client(api_key=google_api_key)
        model = "gemini-2.0-flash"
        response = client.models.generate_content(
            model=model, contents=[instructions, dataframe, question]
        )
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing your request."
    return response.text
