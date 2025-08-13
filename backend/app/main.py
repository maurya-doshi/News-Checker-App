from fastapi import FastAPI

app = FastAPI(
    title="News Checker API",
    description="API for probabilistic fact-checking of text and social media links.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"status": "API is running"}