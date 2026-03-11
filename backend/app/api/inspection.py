from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random 
from backend.app.api.images import images

router = APIRouter()

class InspectRequest(BaseModel):
    image_id: str

@router.post("/projects/{project_id}/inspect")
def inspect_image(project_id: str, request: InspectRequest):

    image_id = request.image_id

    image_data = images[image_id]

    possible_defects = [
        "torn_box",
        "crushed_corner",
        "bad_label",
        "seal_open"
    ]

    detections = []

    num_detections = random.choice([0, 1, 2])

    for _ in range(num_detections):
        label = random.choice(possible_defects)
        confidence = round(random.uniform(0.6, 0.95), 2)

        x1 = round(random.uniform(0.0, 0.6), 2)
        y1 = round(random.uniform(0.0, 0.6), 2)
        x2 = round(random.uniform(x1 + 0.1, 1.0), 2)
        y2 = round(random.uniform(y1 + 0.1, 1.0), 2)

        detections.append({
            "label": label,
            "confidence": confidence,
            "bbox": [x1, y1, x2, y2]
        })

        decision = "PASS" if len(detections) == 0 else "FAIL"

        return {
            "project_id": project_id,
            "image_id": image_id,
            "detections": detections,
            "decision": decision
        }
        
    