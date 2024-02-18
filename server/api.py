from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .config import PROTOCOL, VERCEL_URL

TAG = "Plugin"
templates = Jinja2Templates(directory="static")
app = FastAPI(servers=[{"url": f"{PROTOCOL}://{VERCEL_URL}"}],
              title="Prompt Engineers - Plugin API",
			  description="Returns simple data for testing purposes.",
			  version="0.1.0")

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
		"url": f"{PROTOCOL}://{VERCEL_URL}/openapi.json",
		"is_user_authenticated": False
	},
	"logo_url": "https://avatars.githubusercontent.com/u/139279732?s=200&v=4"
}