import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Get the secret key from the environment variable
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')  # Provide a default for development
