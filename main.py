from fastapi import FastAPI
#import router.expense as expense, router.report as report
from fastapi.middleware.cors import CORSMiddleware
#from router.sales import router as sales_router

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
#app.include_router(sales_router)
#app.include_router(sales.router)
#app.include_router(expense.router)
#app.include_router(report.router)


@app.get("/")
def home():
    return {"message": "API Running"}