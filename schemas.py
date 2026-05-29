from pydantic import BaseModel, ConfigDict, Field


class BasePost(BaseModel):
    title:str = Field(min_length=5, max_length=100)
    content:str =Field(min_length=1)
    author:str = Field(min_length=3, max_length=50)


#post create schema
class CreatePost(BasePost):
    pass
    

class PostResponse(BasePost):
    model_config = ConfigDict(from_attributes=True)
    id:int
    date_posted:str