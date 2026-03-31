from itertools import product
import sys
import os

# Set test database URL before importing anything
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db
from app.models import Product
from app.schemas import ProductCreate

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # Create tables
    Base.metadata.create_all(bind=engine)
    # Add test data
    db = TestingSessionLocal()
    test_product = Product(
        name="Test Saddle",
        category="Saddle",
        price=299.99,
        stock=5
    )
    db.add(test_product)
    db.commit()
    test_product2 = Product(
        name="Horse Bridle",
        category="Accessory",
        price=29,
        stock=0
    )
    db.add(test_product2)
    db.commit()
    db.close()
    yield
    # Clean up
    Base.metadata.drop_all(bind=engine)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2 
    assert "id" in data[0]
    assert data[0]["name"] == "Test Saddle"
    assert data[0]["category"] == "Saddle"
    assert data[0]["price"] == 299.99
    assert data[0]["stock"] == 5
    assert "created_at" in data[0]

def test_get_products_with_category_filter():
    response = client.get("/products?category=Saddle")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    for product in data:
        assert product["category"] == "Saddle"

def test_get_products_with_not_found_category():
    response = client.get("/products?category=Test")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_get_products_in_stock_only():
    response = client.get("/products?in_stock=true")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    for product in data:
        assert product["stock"] > 0

def test_get_product_by_id():
    # First get all products to find an ID
    response = client.get("/products")
    products = response.json()
    assert len(products) > 0
    product_id = products[0]["id"]

    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["name"] == products[0]["name"]
    assert data["category"] == products[0]["category"]

def test_get_product_not_found():
    response = client.get("/products/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

