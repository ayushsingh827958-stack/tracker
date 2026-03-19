#expense={fixed cost,operating cost}
#fixed_cost{furniture,machine}
#operating_cost[staff spray blade]
'''while True:
 print("\nAdd Sale \n2.Exit")
 user=int(input("Enter a choice::"))
 if user==1:
  fixed_cost=input("write your fixed assest::")
  fixed_value=int(input("enter a total amount::"))
  operating_cost=input("write your operating cost::")
  operating_value=int(input("enter a total amount::"))
 elif user==2:
  break
 else:
  print("wrong")
'''
'''
import clinic_data
def add_clinic_expense():
    item=input("expense item::")
    amount=int(input("expense amount::"))
    clinic_data.add_expense(item,amount)
    print("Expense recorded")
'''
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/expenses",
    tags=["Expense"]
)
Expenses=[]
#class model add
class Expense(BaseModel):
    item: str
    amount: int

@router.post("/")
def create_expense(expense: Expense):
    Expenses.append({
        "item": expense.item,
        "amount": expense.amount
    })
    return {"message": "Expense recorded"}

@router.get("/")
def get_expenses():
    return Expenses