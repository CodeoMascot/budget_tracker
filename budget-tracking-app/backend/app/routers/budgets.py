from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Budget)
def create_budget(budget: schemas.BudgetCreate, db: Session = Depends(get_db)):
    return crud.create_budget(db=db, budget=budget)

@router.get("/", response_model=list[schemas.Budget])
def read_budgets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    budgets = crud.get_budgets(db=db, skip=skip, limit=limit)
    return budgets

@router.get("/{budget_id}", response_model=schemas.Budget)
def read_budget(budget_id: int, db: Session = Depends(get_db)):
    db_budget = crud.get_budget(db=db, budget_id=budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return db_budget

@router.put("/{budget_id}", response_model=schemas.Budget)
def update_budget(budget_id: int, budget: schemas.BudgetUpdate, db: Session = Depends(get_db)):
    db_budget = crud.get_budget(db=db, budget_id=budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return crud.update_budget(db=db, budget_id=budget_id, budget=budget)

@router.delete("/{budget_id}", response_model=schemas.Budget)
def delete_budget(budget_id: int, db: Session = Depends(get_db)):
    db_budget = crud.get_budget(db=db, budget_id=budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return crud.delete_budget(db=db, budget_id=budget_id)