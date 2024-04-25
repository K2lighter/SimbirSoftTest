# 4) Вычислить N-е число Фибоначчи, где N - это текущий день месяца + 1.
from datetime import datetime


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


day_number = int(datetime.utcnow().strftime("%d")) + 1

my_fibo = fibonacci(day_number)
