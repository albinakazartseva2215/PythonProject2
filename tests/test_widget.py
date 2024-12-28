import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def account_card():
    return ["Счет 73654108430135874305", "Visa Platinum 7000792289606361"]

@pytest.mark.parametrize("account_card, expected", [("Счет 73654108430135874305", "Счет  **4305"),
                                                    ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 6361")])
def test_get_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_get_mask_invalid_account_card():
    with pytest.raises(ValueError):
        mask_account_card(account_card="Счет 7365410843013587430")


@pytest.fixture
def date_str():
    return "2024-03-11T02:26:18.671407"


@pytest.mark.parametrize("date_str, expected", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected

