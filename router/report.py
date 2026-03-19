'''from sales import Sales,customer_name,phone,address,service
from expense import fixed_cost,fixed_value,operating_cost,operating_value
print("this expense tracker")
while True:
 print("select in this\n1.Sale\n2.Expense\n3.All\n4.Exit")
 user=int(input("Enter a choice::"))
 if user==1:
  Sales(customer_name,phone,address,service)
 elif user==2:
  print(f"Fixed Cost::{fixed_cost}\n Fixed value::{fixed_value}\n Operating cost::{operating_cost}\n operating value::{operating_value}")
 elif user==3:
  pass
 elif user==4:
  break
 else:
  print("wrong choice")''' 
#print(check)
'''import clinic_data
def show_financial_report():
    sales=clinic_data.get_sales()
    expenses=clinic_data.get_expense()
    total_sales=sum(s["amount"] for s in sales)
    total_expenses=sum(e["amount"] for e in expenses)
    profit=total_sales-total_expenses
    print("\n--- Dental report---")
    print("total treatment::")
    for s in sales:
        print(s["patience"],"-",s["treatment"],"-",s["amount"])

    print("\ntotal expense::")
    for e in expenses:
        print(e["item"],"-",e["amount"])
    print("total treatment::",total_sales)
    print("total expense::",total_expenses)    
    print("Net profit::",profit)
       '''
from fastapi import APIRouter
from router.expense import Expenses
from router.sales import Sales

router = APIRouter(
    prefix="/reports",
    tags=["Report"]
)

@router.get("/reports")
def report():
    total_sales = sum(s.get("amount", 0) for s in Sales)
    total_expenses = sum(e.get("amount", 0) for e in Expenses)
    profit = total_sales - total_expenses   

    return {
        "Total Sales": total_sales,
        "Total Expenses": total_expenses,
        "Profits": profit
    }

# report.py
