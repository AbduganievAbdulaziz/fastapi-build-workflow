import uvicorn
from fastapi import FastAPI
from pathlib import Path

def get_version():
    version_file = Path(__file__).parent.parent / "VERSION.md"
    print(version_file)
    if version_file.exists():
        return version_file.read_text().strip()
    return "0.0.0-unknown"

app = FastAPI(title="Simple Demo App", version=get_version())

@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "status": "active",
        "version": app.version
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="debug"
    )