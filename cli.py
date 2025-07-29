from budget import calculate_split

def parse_expenses(text: str) -> dict:
    """
    Converts a string like "rent:1200,utilities:300"
    into {"rent": 1200.0, "utilities": 300.0}.
    """
    expenses = {}
    if not text.strip():
        return expenses
    for pair in text.split(","):
        name, amt = pair.split(":")
        expenses[name.strip()] = float(amt)
    return expenses

def parse_roommates(text: str) -> list:
    """
    Converts "Alice,Bob,Carol" into ["Alice", "Bob", "Carol"].
    """
    if not text.strip():
        return []
    return [name.strip() for name in text.split(",")]

def main():
    print("=== Student Budget Splitter ===\n")
    exp_input = input("Enter expenses (name:amount, comma-separated):\n> ")
    room_input = input("Enter roommate names (comma-separated):\n> ")

    expenses = parse_expenses(exp_input)
    roommates = parse_roommates(room_input)
    result = calculate_split(expenses, roommates)

    print("\n— Split Results —")
    if not roommates:
        print("No roommates given. Nothing to split.")
    else:
        for name, share in result.items():
            print(f"{name}: {share:.2f}")

if __name__ == "__main__":
    main()

