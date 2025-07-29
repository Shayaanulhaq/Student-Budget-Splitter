from flask import Flask, request, jsonify
from monthly_planner import calculate_monthly_budget

app = Flask(__name__)

@app.route("/api/budget", methods=["POST"])
def budget_api():
    data = request.get_json() or {}
    # Extract inputs (default to 0 or empty dict)
    income = float(data.get("income", 0))
    fixed = data.get("fixed_expenses", {})
    variable = data.get("variable_expenses", {})
    # Compute summary
    summary = calculate_monthly_budget(income, fixed, variable)
    return jsonify(summary), 200

if __name__ == "__main__":
    # Starts server on http://127.0.0.1:5000
    app.run(debug=True)

