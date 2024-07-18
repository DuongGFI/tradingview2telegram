from pydantic_core import Url
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import os
# database_url = os.environ.get('DATABASE_URL')

TOKEN = os.environ.get(TOKEN)
chat_id = os.environ.get(chat_id)

class Signal(BaseModel):
    mes: str | None = ""
app = FastAPI()
@app.post("/telegram")
async def telegram(signal: Signal):
    message = signal.order_id
    Url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(Url) # this sends the message
    print(Url)
    return {"status": "Success"}
