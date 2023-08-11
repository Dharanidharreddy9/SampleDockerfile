from uvicorn import run
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def main_function():
    return {"Data": "successfully docker is running"}


if __name__ == "__main__":
    run(app, port=8080, host="0.0.0.0")
