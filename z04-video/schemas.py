from pydantic import BaseModel, ConfigDict, Field
#* pydantic help us in making validation to api reuest and responces.
#* since pydentic is highly supported by fastapi, the docs of fastapi get autometically updated.

#* BaseModel let us create type validation and add other factors like min and max length.
#* in basemodel if we didnt add a default value then it will mean that input field is required

class PostBase(BaseModel):
    title:str = Field(min_length=1, max_length=100)
    content:str =Field(min_length=1)
    author:str =Field(min_length=1, max_length=50)
    #* if we didnt add any default value then it mean that field is required
    
#* by passing post base into postcreate we are providing all input schemas of postbase into create post as it is
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)#* adding fromattributes=true means we are allowing it to access object with attributes
    #*which mean we can accesss data with post.title instead of post[title]
    
    
    id: int #*input schemes that will not be provided by user
    date_posted: str #*input schemes that will not be provided by user
    
    #* you can use id field in here even  thought  its a python keyword because its is used in pydentic and database as a comman field