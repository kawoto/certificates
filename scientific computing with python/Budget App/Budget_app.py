class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self._balance = 0.0

    def __repr__(self):
        title = self.description.center(30, "*") + "\n"
        lines = ""

        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"[:7]
            lines += f"{desc}{amt}\n"

        total = f"Total: {self._balance:.2f}"
        return title + lines + total

    def deposit(self, amount, description=""):
        """Add money to the category."""
        self.ledger.append({"amount": amount, "description": description})
        self._balance += amount

    def withdraw(self, amount, description=""):
        """Remove money if sufficient funds exist."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def transfer(self, amount, category):
        """Transfer funds between categories."""
        if self.withdraw(amount, f"Transfer to {category.description}"):
            category.deposit(amount, f"Transfer from {self.description}")
            return True
        return False

    def check_funds(self, amount):
        return self._balance >= amount


def create_spend_chart(categories):
    """Return a formatted spend chart showing percentage spent per category."""
    # Calculate spent amounts
    spent = [sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
             for cat in categories]
    total_spent = sum(spent)

    # Convert to percentage (nearest lower 10)
    percentages = [int((amount / total_spent) * 100) // 10 * 10 for amount in spent]

    # Chart header
    chart = "Percentage spent by category\n"

    # Build percentage lines
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for p in percentages:
            chart += " o " if p >= level else "   "
        chart += " \n"

    # Separator line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Category name labels
    names = [cat.description for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += "    "
        for name in names:
            chart += f"{name[i] if i < len(name) else ' ':^3}"
        chart += " \n"

    return chart.rstrip("\n")
