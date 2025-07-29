import pytest
from monthly_planner import calculate_monthly_budget

def test_basic_budget():
    result = calculate_monthly_budget(
        1000.0,
        {"rent": 500.0},
        {"food": 200.0}
    )
    assert result["total_fixed"] == 500.0
    assert result["total_variable"] == 200.0
    assert result["total_expenses"] == 700.0
    assert result["surplus"] == 300.0
    # percentages
    pct = result["percentages"]
    assert pytest.approx(pct["fixed"], 0.1) == 50.0
    assert pytest.approx(pct["variable"], 0.1) == 20.0
    assert pytest.approx(pct["surplus"], 0.1) == 30.0

def test_zero_income():
    result = calculate_monthly_budget(
        0.0,
        {"rent": 100.0},
        {"food": 50.0}
    )
    # avoid division by zero: all percentages = 0
    assert result["percentages"] == {"fixed": 0, "variable": 0, "surplus": 0}

