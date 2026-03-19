from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  router.sales import router as sales_router
app = FastAPI()
app.include_router(sales_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API Running"}
