from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
