\# Проект обработки транзакций



\## Модуль generators



Модуль содержит функции-генераторы для работы с транзакциями:



\### filter\_by\_currency(transactions, currency\_code)

Фильтрует транзакции по заданной валюте. Возвращает итератор.



Пример:

```python

usd\_transactions = filter\_by\_currency(transactions, "USD")

for \_ in range(2):

&nbsp;   print(next(usd\_transactions))

