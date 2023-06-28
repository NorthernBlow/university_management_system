from fastapi import FastAPI, status, Response
from router import blog


app = FastAPI()
app.include_router(blog.router)

@app.get("/")
def home():
    return {"message": "its a main page"}



