
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return product