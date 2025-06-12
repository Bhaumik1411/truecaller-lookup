from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your GitHub Pages URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/lookup")
def lookup(phone: str):
    url = f"https://truecaller.ntmain.com/api/truecaller?phone={phone}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
