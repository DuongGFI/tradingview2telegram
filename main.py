from pydantic_core import Url
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import os

TOKEN = os.environ.get("TOKEN")
chat_id = os.environ.get("chat_id")

class Signal(BaseModel):
    mes: str | None = ""
app = FastAPI()
@app.post("/telegram")
async def telegram(signal: Signal):
    Url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={signal.mes}"
    requests.get(Url) # this sends the message
    print(Url)
    return {"status": "Success"}
