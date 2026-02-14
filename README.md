# Виджет банковских операций 
 
Проект для обработки и отображения банковских операций клиента. 
 
## Описание 
 
Проект содержит функции для фильтрации и сортировки банковских операций по различным параметрам. 
 
## Функции 
 
- `filter_by_state(operations, state="EXECUTED")` - фильтрует операции по статусу 
- `sort_by_date(operations, reverse=True)` - сортирует операции по дате 
 
## Установка 
 
1. Клонируйте репозиторий: 
   ```bash 
   git clone https://github.com/ваш-username/банк-операции.git 
   ``` 
 
2. Установите зависимости: 
   ```bash 
   pip install flake8 mypy black 
   ``` 
 
## Зависимости 
 
- Python 3.8+ 
- flake8==7.3.0 
- mypy==1.19.1 
- black==26.1.0 
 
## Проверка кода 
 
```bash 
# flake8 проверка стиля 
python -m flake8 src/ 
 
# mypy проверка типов 
python -m mypy src/ 
 
# black форматирование 
python -m black src/ 
``` 
 
## Пример использования 
 
```python 
from src.processing import filter_by_state, sort_by_date 
 
# Пример данных 
operations = [ 
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, 
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, 
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"} 
] 
 
# Фильтрация 
executed_ops = filter_by_state(operations, "EXECUTED") 
print(executed_ops) 
 
# Сортировка 
sorted_ops = sort_by_date(operations) 
print(sorted_ops) 
``` 
