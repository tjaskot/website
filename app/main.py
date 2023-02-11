from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse, PlainTextResponse, FileResponse


app_description = """
Personal website for Trevor Jaskot. Consulting, software, hardware enthusiast, sound professional, physicist,
culture driver.
"""
app = FastAPI(
    title="TJaskot Website",
    description=app_description,
    version="1.0"
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/webfonts", StaticFiles(directory="app/static/webfonts"), name="webfonts")
templates = Jinja2Templates(directory="app/templates")
favicon_path = 'favicon.ico'


@app.get("/")
async def root():
    """
    Redirect url for root, users will be sent to login page or home page.
    :return:
    """
    return RedirectResponse("/home")


# Request context is used for Jinja2 insertion of html reponse body
@app.get("/home", response_class=HTMLResponse)
async def home(home_request: Request):
    """
    Index page returned when use is directed to home endpoint.
    :return:
    """
    return templates.TemplateResponse("index.html", {"request": home_request})


# Page for contacting Trevor about consulting, business opportunities, questions,
#   feedback, and any tech interest topics :)
@app.get("/contact", response_class=HTMLResponse)
async def home(contact_request: Request):
    """
    Contact page regarding opportunities and discussion topics with Trevor.
    :return:
    """
    return templates.TemplateResponse("contact.html", {"request": contact_request})


@app.get("/code", response_class=HTMLResponse)
async def home(code_request: Request):
    """
    Coding page of queried responses with programmed code by Trevor.
    :return:
    """
    return templates.TemplateResponse("code.html", {"request": code_request})


@app.get("/blog", response_class=HTMLResponse)
async def home(blog_request: Request):
    """
    Blog page for travel experiences, education topics, tech conversations, ideation, and true digital innovation.
    :return:
    """
    return templates.TemplateResponse("blog.html", {"request": blog_request})


@app.get("/business", response_class=HTMLResponse)
async def home(business_request: Request):
    """
    Business page for inquiries and potential collaboration opportunities.
    :return:
    """
    return templates.TemplateResponse("business.html", {"request": business_request})


@app.get("/askaquestion", response_class=HTMLResponse)
async def home(askaquestion_request: Request):
    """
    Ask A Question page for topics, discussions, billboards, thoughts, education, guidance, and
    anything else which comes to mind.
    :return:
    """
    return templates.TemplateResponse("askaquestion.html", {"request": askaquestion_request})


@app.api_route("/api", methods=["GET", "POST"])
async def api_test(api_test: Request):
    """
    Api endpoint for GET and POST method testing.
    :return:
    """
    if api_test.method == "GET":
        return JSONResponse({"api_get": "valid"})
    elif api_test.method == "POST":
        return JSONResponse({"api_post": "valid"})
    else:
        return PlainTextResponse("another method??")


@app.get("keepalive")
@app.get("healthcheck")
def alive():
    """
    Keepalive and healthcheck endpoint used for api responses.
    :return:
    """
    return JSONResponse(status_code=200, content={"is_alive": "healthy"})


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
