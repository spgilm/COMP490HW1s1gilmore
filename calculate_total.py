def calculate_total(state: str, item_list) -> float:
    state = state.upper()
    total = 0.00
    if state == "MA":
        for item in item_list:
            if item.item_price > 0.00:
                if item.item_type == 1:
                    total += item.item_price
                elif item.item_type == 2:
                    total += item.item_price
                    if item.item_price > 175.00:
                        total += ((item.item_price - 175.00) * .0625)
                elif item.item_type == 3:
                    total += (item.item_price + (item.item_price * .0625))
                else:
                    print("Invalid item type. Ending function. Please try again with valid entries.")
                    return 0.00
            else:
                print("Invalid negative price. No returns. Ending function. Please try again with valid entries.")
                return 0.00

    elif state == "ME":
        for item in item_list:
            if item.item_price > 0.00:
                if item.item_type == 1:
                    total += item.item_price
                elif (item.item_type == 2) or (item.item_type == 3):
                    total += (item.item_price + (item.item_price * .055))
                else:
                    print("Invalid item type. Ending function. Please try again with valid entries.")
                    return 0.00
            else:
                print("Invalid negative price. No returns. Ending function. Please try again with valid entries.")
                return 0.00

    elif state == "NH":
        for item in item_list:
            if item.item_price > 0.00:
                if (item.item_type == 1) or (item.item_type == 2) or (item.item_type == 3):
                    total += item.item_price
                else:
                    print("Invalid item type. Ending function. Please try again with valid entries.")
                    return 0.00
            else:
                print("Invalid negative price. no returns. Ending function. Please try again with valid entries.")
                return 0.00

    else:
        print("Invalid state. Ending function. Please try again")
        return 0.00
    if total == 0.00:
        print("Invalid list, please try again")

    return round(total, 2)
