def calculate_monthly_budget(
    income: float,
    fixed_expenses: dict,
    variable_expenses: dict
) -> dict:
    """
    Returns a summary dict:
      - total_fixed
      - total_variable
      - total_expenses
      - surplus
      - percentages: {
          "fixed": x%,
          "variable": y%,
          "surplus": z%
        }
    """
    total_fixed = sum(fixed_expenses.values())
    total_variable = sum(variable_expenses.values())
    total_expenses = total_fixed + total_variable
    surplus = income - total_expenses

    def pct(amount):
        return (amount / income * 100) if income else 0

    percentages = {
        "fixed": pct(total_fixed),
        "variable": pct(total_variable),
        "surplus": pct(surplus),
    }

    return {
        "total_fixed": total_fixed,
        "total_variable": total_variable,
        "total_expenses": total_expenses,
        "surplus": surplus,
        "percentages": percentages
    }

