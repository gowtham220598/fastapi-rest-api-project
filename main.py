from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI application"
    }


@app.get("/about")
def about():
    return {
        "name": "Gowtham",
        "course": "Generative AI",
        "role": "AI/Backend Developer"
    }