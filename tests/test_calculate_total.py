import pytest
import calculate_total
from dataclasses import dataclass

@dataclass
class SaleItem:
    item_name: str
    item_price: float
    item_type: int

@pytest.fixture
def good_list_fixture():
    item_number_one = SaleItem("Banana", .75, 1)
    item_number_two = SaleItem("Expensive Shirt", 300.00, 2)
    item_number_three = SaleItem("Skateboard", 75.00, 3)
    item_number_four = SaleItem("Cheap Shirt", 12.50, 2)
    test_list = [item_number_one, item_number_two, item_number_three, item_number_four]
    return test_list

@pytest.fixture
def bad_list_fixture():
    item_number_one = SaleItem("Banana", -.75, 1)
    item_number_two = SaleItem("Expensive Shirt", -300.00, 2)
    item_number_three = SaleItem("Skateboard", -75.00, 3)
    item_number_four = SaleItem("Cheap Shirt", -12.50, 2)
    test_list = [item_number_one, item_number_two, item_number_three, item_number_four]
    return test_list



def test_maine(good_list_fixture):
    total = calculate_total.calculate_total("me", good_list_fixture)
    assert total == 409.56
    assert total != 0.00


def test_massachusetts(good_list_fixture):
    total = calculate_total.calculate_total("ma", good_list_fixture)
    assert total == 400.75
    assert total != 0.00


def test_new_hampshire(good_list_fixture):
    total = calculate_total.calculate_total("nh", good_list_fixture)
    assert total == 388.25
    assert total != 0.00

def test_maine_return_attempt(bad_list_fixture):
    total = calculate_total.calculate_total("me", bad_list_fixture)
    assert total == 0.00
    assert total != -409.56


def test_massachusetts_return_attempt(bad_list_fixture):
    total = calculate_total.calculate_total("ma", bad_list_fixture)
    assert total == 0.00
    assert total != -400.75


def test_new_hampshire_return_attempt(bad_list_fixture):
    total = calculate_total.calculate_total("nh", bad_list_fixture)
    assert total == 0.00
    assert total != 388.25

def test_invalid_state(good_list_fixture):
    total = calculate_total.calculate_total("qr", good_list_fixture)
    assert total == 0.00

def test_invalid_state_return_attemp(bad_list_fixture):
    total = calculate_total.calculate_total("qr", bad_list_fixture)
    assert total == 0.00
