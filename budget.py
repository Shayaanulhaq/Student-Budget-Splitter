def calculate_split(expenses: dict, roommates: list) -> dict:
    """
    expenses: dict of expense_name → amount, e.g. {"rent": 1200, "utilities": 300}
    roommates: list of names, e.g. ["Alice", "Bob"]
    returns: dict mapping each roommate to their share
    """
    total = sum(expenses.values())
    per_person = total / len(roommates) if roommates else 0
    return {name: per_person for name in roommates}

