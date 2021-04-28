# About:
This function was developed in Python 3.8 by Sean Gilmore (s1gilmore) using PyCharm as an IDE

## calculate_total
The calculate_total function takes two arguments:<br>
state as a 2 letter abbreviation, and a list of dataclass items<br>
The dataclass is defined as item name (str), item price (float), and item type (int)<br>
The possible types (and corresponding integers) are as follows:<br>
1-“Wic Eligible food” 2-Clothing, 3-"everything else"<br>
Only for the states Maine-ME, Massachusetts-MA, and New Hampshire-NH<br>
Maine taxes clothing and "everything else" at 5.5%, “Wic Eligible food” has no sales tax<br>
Massachusetts does not tax “Wic Eligible food”, or clothing items up to $175,<br>
the cost over $175 is taxed at 6.25%, "everything else" is taxed at 6.25%<br>
New Hampshire has no sales tax on “Wic Eligible food”, clothing, or "everything else"<br>
Assuming the function is passed proper arguments, it will calculate the customer total including applicable taxes<br>
Floats will not be rounded to "two decimal USD notation" until end of calculation.<br>
Unavailable states or attempts at a negative price will result in a 0.00 total with an error message.<br>
<br>
## test_calculate_total
Tests written for pytest. In PyCharm right click tests folder and choose "Run 'pytest in tests'"
