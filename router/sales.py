from fastapi import APIRouter
from pydantic import BaseModel
#from patient import Database

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)
Sales=[]
class Sale(BaseModel):
    patient: str
    amount: int
@router.post("/")
def add_sales(sale: Sale):
    Sales.append({
        "patient": sale.patient,
        "amount": sale.amount
    })
    return {"message": "Bill recorded"}
@router.get("/")
def get_sales():
    return Sales
# sales.py
