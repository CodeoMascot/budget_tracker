from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User schemas
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

# Budget schemas
class BudgetBase(BaseModel):
    name: str
    amount: float
    recurring: bool

class BudgetCreate(BudgetBase):
    pass

class BudgetResponse(BudgetBase):
    id: int
    user_id: int
    created_at: datetime

class BudgetUpdate(BudgetBase):
    pass

# Expense schemas
class ExpenseBase(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    budget_id: int

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int
    budget_id: int
    created_at: datetime

class ExpenseUpdate(ExpenseBase):
    pass

# Category schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

# Combined responses
class UserDashboard(BaseModel):
    total_budget: float
    total_expenses: float
    remaining_balance: float
    budgets: List[BudgetResponse]
    expenses: List[ExpenseResponse]