from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel, Field
from fastapi import status

app = FastAPI(title="Gowtham")
@app.get("/aji")
def root():
    return{"message": "Hello FastApi"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "type": str(type(user_id))}

@app.get("/search")
def search(q: str, page: int = 1, limit: int = 10):
    return {"q": q, "page": page, "limit": limit}

class usercreate(BaseModel):
    name: str
    email: str
    password: int | None

@app.post("/users")
def create_user(payload: usercreate):
    return{"created":True, "user": payload.model_dump()}

class ProductCreate(BaseModel):
    name: str =Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    
@app.post("/products")
def create_product(p: ProductCreate):
    return p.model_dump()

@app.post("/items",status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Item created successfully."}

@app.get("/users/db/{user_id}")
def get_user_from_db(user_id: int):
    if user_id not in FAKE_DB:
        return {"id": user_id, "message": "User not found."}