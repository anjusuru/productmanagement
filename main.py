from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from db import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.get("/")
def list_products(db: Session = Depends(get_db)):
    product_list = db.query(models.Product).all()
    return product_list


@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    product = crud.create_product(
        db=db,
        name=product.name,
        brand=product.brand,
        price=product.price,
        quantity=product.quantity,
        category=product.category,
    )

    return {"product": product}


@app.get("/products/{id}")  # id is a path parameter
def get_product(id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db=db, id=id)
    if product:
        return product
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Product with id {id} does not exist"},
        )


@app.put("/products/{id}")  # id is a path parameter
def update_product(id: int, product: schemas.Product, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, id=id)

    if db_product:
        updated_product = crud.update_product(
            db=db,
            id=id,
            name=product.name,
            brand=product.brand,
            price=product.price,
            quantity=product.quantity,
            category=product.category,
        )
        return updated_product
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Product with id {id} does not exist"},
        )


@app.delete("/products/{id}")  # id is a path parameter
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, id=id)
    if db_product:
        return crud.delete_product(db=db, id=id)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Product with id {id} does not exist"},
        )
