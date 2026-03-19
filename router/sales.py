'''from fastapi import APIRouter
from pydantic import BaseModel
from patient import Database

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
    return Sales'''
# sales.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from router.patient import Database  # Safe to import now

router = APIRouter(prefix="/sales", tags=["Sales"])
db = Database()

class Sale(BaseModel):
    patient_id: int
    service_id: int
    amount: int

@router.post("/")
def add_sales(sale: Sale):
    patient = db.fetch_one("SELECT * FROM Patient WHERE id = ?", (sale.patient_id,))
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    service = db.fetch_one("SELECT * FROM Services WHERE id = ?", (sale.service_id,))
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    db.execute(
        "INSERT INTO sales (patient_id, service_id, amount) VALUES (?, ?, ?)",
        (sale.patient_id, sale.service_id, sale.amount)
    )
    return {"message": "Bill recorded"}

@router.get("/")
def get_sales():
    return db.fetch_all("""
        SELECT s.id, p.name AS patient_name, sv.service_name AS service_name, s.amount
        FROM sales s
        JOIN Patient p ON s.patient_id = p.id
        JOIN Services sv ON s.service_id = sv.id
    """)