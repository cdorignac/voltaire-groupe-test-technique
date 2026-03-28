
from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas import Product as ProductSchema, ProductCreate

app = FastAPI()

@app.get("/products", response_model=List[ProductSchema])
def get_products(
    category: Optional[str] = None, 
    in_stock: bool = False,
    db: Session = Depends(get_db)
) -> List[ProductSchema]:
    query = db.query(models.Product)
    if category:
        query = query.filter(models.Product.category == category)
    if in_stock:
        query = query.filter(models.Product.stock > 0)
    products = query.all()
    return [ProductSchema.model_validate(product) for product in products]

@app.get("/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)) -> ProductSchema:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return ProductSchema.model_validate(product)

@app.post("/products", response_model=ProductSchema)
def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> ProductSchema:
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return ProductSchema.model_validate(db_product)

@app.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)) -> ProductSchema:
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return ProductSchema.model_validate(db_product)