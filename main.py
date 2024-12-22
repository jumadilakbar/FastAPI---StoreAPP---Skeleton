import os
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from config.database import Base, engine
from routes import blog_routes, user_routes, store_routes, product_routes, auth_routes
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# Initialize Database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a global API Router with a default prefix
api_router = APIRouter(prefix="/api/v1")
api_router.include_router(user_routes.router, prefix="/users", tags=["Users"])
# api_router.include_router(role_routes.router, prefix="/roles", tags=["Roles"])
api_router.include_router(blog_routes.router, prefix="/blogs", tags=["Blogs"])
api_router.include_router(product_routes.router, prefix="/products", tags=["Products"])
api_router.include_router(store_routes.router, prefix="/stores", tags=["Stores"])
api_router.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])

# Include the global API router in the FastAPI app

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to the API",
        "version": "v1",
        "documentation_url": "/docs"
    }
app.include_router(api_router)
# Get application port from environment
APP_PORT = int(os.getenv("APP_PORT", 8000))
