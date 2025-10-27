# main.py — development entry point
import budget
from budget import create_spend_chart
from unittest import main

# Create categories
food = budget.Category("Food")
clothing = budget.Category("Clothing")
auto = budget.Category("Auto")

# Transactions
food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant and dessert")

clothing.deposit(0, "Start")
food.transfer(50, clothing)
clothing.withdraw(25.55, "T-shirt")
clothing.withdraw(100, "Shoes")

auto.deposit(1000, "Initial deposit")
auto.withdraw(15, "Gas")

# Display balances and charts
print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))

# Run unit tests
main(module="test_module", exit=False)
