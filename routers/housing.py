from fastapi import APIRouter

router = APIRouter(
    prefix="/housing",
    tags=["housing"]
)


@router.get("/")
def index():
    return {
        "message": "Housing router activo"
    }
