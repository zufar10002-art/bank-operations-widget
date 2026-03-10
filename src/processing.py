"""
Модуль для обработки банковских операций.
"""

from typing import Dict, List, Any
from datetime import datetime


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations: Список словарей с операциями
        state: Статус для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список операций
    """
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(
    operations: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список словарей с операциями
        reverse: Порядок сортировки
                (True - по убыванию, False - по возрастанию)

    Returns:
        Отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda x: datetime.fromisoformat(
            x.get("date", "0001-01-01T00:00:00.000000")
        ),
        reverse=reverse
    )


if __name__ == "__main__":
    test_operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]

    print("Тестирование filter_by_state:")
    print("1. Со статусом 'EXECUTED':")
    result = filter_by_state(test_operations, "EXECUTED")
    for op in result:
        print(f"   {op}")

    print("\n2. Со статусом 'CANCELED':")
    result = filter_by_state(test_operations, "CANCELED")
    for op in result:
        print(f"   {op}")

    print("\nТестирование sort_by_date:")
    print("1. По убыванию (reverse=True):")
    result = sort_by_date(test_operations, True)
    for op in result:
        print(f"   {op}")

    print("\n2. По возрастанию (reverse=False):")
    result = sort_by_date(test_operations, False)
    for op in result:
        print(f"   {op}")