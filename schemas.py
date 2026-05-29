from pydantic import BaseModel, ConfigDict, Field


# class showing how our schema will look like, this is the base schema that we will use to create our post and also to return our post, we will inherit from this base schema to create our post and also to return our post
class BasePost(BaseModel):
    title:str = Field(min_length=5, max_length=100)
    content:str =Field(min_length=1)
    author:str = Field(min_length=3, max_length=50)


#post create schema
class CreatePost(BasePost):
    pass
    

# For returning our data
class PostResponse(BasePost):
    model_config = ConfigDict(from_attributes=True)
    id:int
    date_posted:str