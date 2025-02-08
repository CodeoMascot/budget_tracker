from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, budgets, expenses, users
from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(budgets.router, prefix="/budgets", tags=["budgets"])
app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Budget Tracking API!"}