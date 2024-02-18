import os

# Load environment variables
VERCEL_ENV = os.environ.get("VERCEL_ENV", 'development')
VERCEL_URL = os.environ.get("VERCEL_URL", 'localhost:8001')

# Dependents
PROTOCOL = 'https' if VERCEL_ENV in {'production', 'preview'} else 'http'