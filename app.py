from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Token Counter", version="v1")

class Health(BaseModel):
    ok: bool

class TokenCountResponse(BaseModel):
    input: str
    token_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/token-count", response_model=TokenCountResponse)
def token_count(text: str = Query(..., description="Text to tokenize and count tokens")):
    # Tokenization: split on whitespace, strip surrounding punctuation
    raw_tokens = re.findall(r"\S+", text)
    tokens = [re.sub(r"^[^\w]+|[^\w]+$", "", t) for t in raw_tokens if re.sub(r"^[^\w]+|[^\w]+$", "", t)]
    return {"input": text, "token_count": len(tokens)}
