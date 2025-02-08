from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    budgets = relationship("Budget", back_populates="owner")
    expenses = relationship("Expense", back_populates="owner")

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Float)
    recurring = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="budgets")
    expenses = relationship("Expense", back_populates="budget")

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    category = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    budget_id = Column(Integer, ForeignKey('budgets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    budget = relationship("Budget", back_populates="expenses")
    owner = relationship("User", back_populates="expenses")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)