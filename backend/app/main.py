from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

app = FastAPI()

@app.get("/products")
def get_products(
    category: Optional[str] = None, 
    in_stock: bool = False,
    db: Session = Depends(get_db)
):
    query = db.query(models.Product)
    if category:
        query = query.filter(models.Product.category == category)
    if in_stock:
        query = query.filter(models.Product.stock > 0)
    return query.all()