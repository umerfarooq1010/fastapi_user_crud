# Importing FastAPI packages
from fastapi import APIRouter

# Importing from project files
from routers import auth, user


# Router Object to Create Routes
router = APIRouter()


# -----------------------------------------------------------------------------


# Include all file routes
router.include_router(auth.router)
router.include_router(user.router)
