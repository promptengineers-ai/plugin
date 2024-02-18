from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .config import VERCEL_URL

app = FastAPI()
templates = Jinja2Templates(directory="static")

TAG = "Plugin"

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = app.openapi()
    openapi_schema["servers"] = [
        {"url": VERCEL_URL, "description": "Main server"},
        # Add more servers here if needed
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.on_event("startup")
async def startup_event():
    app.openapi_schema = custom_openapi()

@app.get("/", tags=["Pages"], include_in_schema=False)
async def home(request: Request):
    """Serves the index page."""
    return templates.TemplateResponse(
        "pages/index.html",
        {"request": request, "current_page": "home"}
    )

@app.get("/.well-known/ai-plugin.json", tags=[TAG])
async def read_root():
  return {
	"schema_version": "v1",
	"name_for_human": "Example Plugin API",
	"name_for_model": "dev",
	"description_for_human": "Returns simple data for testing purposes.",
	"description_for_model": "Returns simple data for testing purposes.",
	"auth": {
		"type": "none"
	},
	"api": {
		"type": "openapi",
		"url": f"{VERCEL_URL}/openapi.json",
		"is_user_authenticated": False
	},
	"logo_url": "https://dev.to/logo.png"
}

@app.get("/devto/.well-known/ai-plugin.json", tags=[TAG])
async def read_root():
  return {
	"schema_version": "v1",
	"name_for_human": "DEV Community",
	"name_for_model": "dev",
	"description_for_human": "Recommending posts and members from DEV Community.",
	"description_for_model": "Recommending articles or users from DEV Community. Always link to a url for the resource returned.",
	"auth": {
		"type": "none"
	},
	"api": {
		"type": "openapi",
		"url": "https://dev.to/openapi.yml",
		"is_user_authenticated": False
	},
	"logo_url": "https://dev.to/logo.png",
	"contact_email": "yo@dev.to",
	"legal_info_url": "https://dev.to/terms"
}