from dataclasses import dataclass
from typing import List

@dataclass
class SaleItem:
    item_name: str
    item_price: float
    item_type: int

def calculate_total(state: str, item_list) -> float:
    state = state.upper()
    total=0.0
    if state=="MA":
        return total
        #if item is "everything else" or clothing over $175 tax at 6.25%
    elif state=="ME":
        return total
        #if item is "everything else" or clothing tax at 5.5%
    elif state=="NH":
        for item in item_list:
            total += item.item_price
        #0% tax rate
    else:
        print("Invalid state, please try again")
    if total==0.0:
        print("Invalid list, please try again")
    return total

def main():
    number_one = SaleItem("Banana", .75, 1)
    number_two = SaleItem("Expensive Shirt", 300.00, 2)
    number_three = SaleItem("Skateboard", 75.00, 3)
    test_list = [number_one, number_two, number_three]
    total = calculate_total("ma", test_list)
    print(total)
    total = calculate_total("me", test_list)
    print(total)
    total = calculate_total("nh", test_list)
    print(total)

if __name__ == '__main__':
    main()
