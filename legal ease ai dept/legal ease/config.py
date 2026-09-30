
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Store the key in a variable that other files can import
API_KEY = os.getenv("GEMINI_API_KEY")

