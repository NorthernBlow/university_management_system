from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return "its a main page"
