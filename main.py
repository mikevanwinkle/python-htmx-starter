from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.routes.partials import router as partial_router
from src.routes.brewery import router as brewery_router

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/worker.js", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/",  response_class=HTMLResponse)
async def root(request: Request):
    pagedata = {
        "name": "Home",
        "loggedin": False,
    }
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )

app.include_router(partial_router)
app.include_router(brewery_router)
