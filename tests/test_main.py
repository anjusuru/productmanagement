import json

import pytest


def test_create_product(client_test):

    test_request_payload = {
        "name": "new",
        "brand": "brand",
        "price": 0,
        "quantity": 0,
        "category": "category",
    }

    test_response_payload = {
        "product": {
            "price": 0,
            "id": 1,
            "category": "category",
            "quantity": 0,
            "name": "new",
            "brand": "brand",
        }
    }
    response = client_test.post(
        "/products",
        data=json.dumps(test_request_payload),
    )
    assert response.status_code == 201
    assert response.json() == test_response_payload
    # assert response.json()["id"] is not None
    # assert response.json()["brand"] == "brandtest"
    # assert response.json()["price"] == 128
    # assert response.json()["quantity"] == 45
    # assert response.json()["category"] == "testcategory"
    # assert response.json()["id"] is not None


def test_create_product_invalid_json(client_test):
    response = client_test.post("/products", data=json.dumps({"name": "something"}))
    assert response.status_code == 422


def test_read_product_incorrect_id(client_test):

    response = client_test.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product does not exist"


def test_read_all_notes(client_test):
    # test_data = [
    #     {
    #         "price": 0,
    #         "id": 1,
    #         "category": "category",
    #         "quantity": 0,
    #         "name": "new",
    #         "brand": "brand",
    #     }
    # ]

    response = client_test.get("/")
    assert response.status_code == 200
    # assert response.json() == test_data
