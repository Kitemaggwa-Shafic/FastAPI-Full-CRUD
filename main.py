from fastapi import FastAPI, Request, HTTPException, status
# using jinja2templates in python 
from fastapi.templating import Jinja2Templates
#link for statis file to use in project
from fastapi.staticfiles import StaticFiles
from schemas import CreatePost, PostResponse


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
        "content": "FastAPI documentation made easy sample content to be added here in",
        "date_posted": "23 May 2026",
    },
    {
        "id": 2,
        "author": "Slyvie",
        "title": "Python Training",
        "content": "Python is an easy language to learn by anyone as long you do practice and keep up with principles",
        "date_posted": "02 Feb 1999",
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
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Posts"})
    #return {"message": "HEllo World!!"}



# getting a single post
@app.get("/posts/{post_id}", include_in_schema=False)
def view_a_post(request:Request, post_id: int):
    for post in posts:
        if post.get("id")== post_id:
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": post["title"]})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")



#get posts route,
# we are using response_model to specify the type of data we want to return, in this case we want to return a list of PostResponse objects, and we are also using the posts variable to return the data
@app.get("/api/posts", response_model=list[PostResponse])
def get_posts():
    return posts


# creating a post route, we are using the CreatePost schema to validate the data we are sending to the server, and we are also using the posts variable to store the data
@app.post("/api/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: CreatePost):
    new_id = max([post["id"] for post in posts]) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "date_posted": "May 29, 2026",
    }
    posts.append(new_post)
    return new_post



# getting a single post
@app.get("/api/posts/{post_id}", response_model=PostResponse)
# we are using path parameter to get a specific post by its id and shld be an int type, and we are also using 
# HTTPException to handle the case when the post is not found
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    # we are using raising HTTPException to return a 404 error if the post is not found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
 
