from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/echo")
async def echo(text: str = None):
    return {"message": f"Pinging FastAPI {text}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)