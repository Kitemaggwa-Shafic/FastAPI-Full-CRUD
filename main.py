from fastapi import FastAPI
#HTML reponse for humana
from fastapi.responses import HTMLResponse


# this app will be used to defie our routes
app = FastAPI()


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
@app.get("/", response_class=HTMLResponse)
def home():
    return f"<h1>{posts[0]['title']}</h1>"
    #return {"message": "HEllo World!!"}


#get posts route
@app.get("/api/posts")
def get_posts():
    return posts