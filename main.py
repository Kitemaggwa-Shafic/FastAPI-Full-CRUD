from fastapi import FastAPI, Request
# using jinja2templates in python 
from fastapi.templating import Jinja2Templates
#link for statis file to use in project
from fastapi.staticfiles import StaticFiles


# this app will be used to defie our routes
app = FastAPI()

# mount method with 3 parameters "url path, static file instatnce to dir, name to ref in template"
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory = "templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Profic",
        "title": "FastAPI Training",
        "content": "FastAPI documentation made easy",
        "date_posted": "23 May 2026",
    },
    {
        "id": 2,
        "author": "Slyvie",
        "title": "Pythn Training",
        "content": "Python is an easy language made easy",
        "date_posted": "23 May 2026",
    },
]

# Updating my route to return HTML reponses in the decorator 
@app.get("/", include_in_schema=False, name="home")
# i have te same route returning the same data, so we are going to hide the 
# HTML routes from our API data and only appear in browser (include_in_schema=False),
# so now /posts routes wont be seen in API but oly in browser 
@app.get("/posts", include_in_schema=False, name="posts")
def home(request:Request):
    #having arequest and 
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})
    #return {"message": "HEllo World!!"}


#get posts route
@app.get("/api/posts")
def get_posts():
    return posts