from fastapi import FastAPI
from backend.app.api import inspection, projects, images

app = FastAPI(title="BoxInspect API", version="0.1.0",openapi_version="3.0.2")

app.include_router(projects.router)
app.include_router(images.router)
app.include_router(inspection.router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "boxinspect"}