
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from gemini_generator import generate_legal_draft

router = APIRouter()
templates = Jinja2Templates(directory="frontend")

@router.get("/")
async def load_home(request: Request):
    # Loads the default homepage
    return templates.TemplateResponse(request=request, name="index.html", context={"result": None})

@router.post("/generate-doc")
async def handle_form(request: Request, doc_type: str = Form(...), details: str = Form(...)):
    # Sends user inputs to the AI and returns the result
    ai_draft = generate_legal_draft(doc_type, details)
    return templates.TemplateResponse(request=request, name="index.html", context={"result": ai_draft, "doc_type": doc_type})
    