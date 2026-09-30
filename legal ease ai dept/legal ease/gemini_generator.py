
from google import genai
from config import API_KEY

# Initialize the new Google GenAI client
client = genai.Client(api_key=API_KEY)

def generate_legal_draft(document_type: str, details: str):
    """Sends the prompt to Gemini and returns an HTML-formatted legal draft."""
    prompt = f"Act as an expert legal assistant. Draft a standard, professional {document_type} based on these details: {details}. Format the output strictly in basic HTML using <h3>, <p>, <ul>, <li>, and <strong>. Do not use Markdown."
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"<p>Error generating document: {str(e)}</p>"
        