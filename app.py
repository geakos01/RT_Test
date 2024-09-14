from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/echo")
async def echo(text: str = None):
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "message": f"Pinging FastAPI {text}",
        "received_at": current_time
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)