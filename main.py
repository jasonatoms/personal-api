from fastapi import FastAPI
from app.routes import router
from app.models import Base, engine

# Initialize FastAPI app
app = FastAPI(title="Personal API", description="An AI-powered interactive knowledge API", version="1.0")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to your personal API!"}
