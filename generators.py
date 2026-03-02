# -*- coding: utf-8 -*-
def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction.get("operationAmount"):
            currency = transaction["operationAmount"].get("currency", {})
            if currency.get("code") == currency_code:
                yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        num_str = str(number).zfill(16)
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
