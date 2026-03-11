from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid

router = APIRouter()
images = {}

@router.post("/projects/{project_id}/images")
async def upload_image(project_id, file: UploadFile = File(...)):

    folder = os.path.join("storage", "images", project_id)
    os.makedirs(folder, exist_ok=True)

    image_id = str(uuid.uuid4())
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in [".jpg", ".jpeg", ".png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    path = os.path.join(folder, image_id + extension)

    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)

    images[image_id] = {
        "id": image_id,
        "project_id": project_id,
        "filename": file.filename,
        "path": path
    }

    return {"image_id": image_id, "filename": file.filename}
