from fastapi import FastAPI
from . import models, database
from .routers import products

# Initialize the database
models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI
app = FastAPI()

# Include routers
app.include_router(products.router)
