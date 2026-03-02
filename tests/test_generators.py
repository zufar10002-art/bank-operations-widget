# -*- coding: utf-8 -*-
import pytest
from generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод 1"
        },
        {
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод 2"
        },
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод 3"
        },
        {
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "Перевод 4"
        },
        {},
        {"operationAmount": {}},
    ]


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_matches(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "GBP"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),
    ("RUB", 1),
    ("EUR", 1),
    ("GBP", 0),
])
def test_filter_by_currency_parametrized(
    sample_transactions, currency, expected_count
):
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод 1",
        "Перевод 2",
        "Перевод 3",
        "Перевод 4",
        "",
        ""
    ]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


def test_card_number_generator_range():
    cards = list(card_number_generator(1, 3))
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_start_end_equal():
    cards = list(card_number_generator(5, 5))
    assert cards == ["0000 0000 0000 0005"]


def test_card_number_generator_format():
    card = next(card_number_generator(12345, 12345))
    parts = card.split()
    assert len(parts) == 4
    assert all(len(part) == 4 for part in parts)
    assert all(part.isdigit() for part in parts)
