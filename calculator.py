"""
Модуль «Калькулятор комиссий».
"""

MIN_AMOUNT = 100
MAX_AMOUNT = 50_000
LIMIT_1 = 1_000
LIMIT_2 = 20_000
HIGH_AMOUNT_LIMIT = 40_000


def calculate_commission(amount: int) -> float:
    """
    Рассчитывает комиссию для денежного перевода.

    Args:
        amount: Сумма перевода от 100 до 50 000 руб.

    Returns:
        float: Размер комиссии.

    Raises:
        ValueError: Если сумма не входит в допустимый диапазон.
        TypeError: Если передано нечисловое значение.
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма перевода должна быть числом")

    if amount < MIN_AMOUNT or amount > MAX_AMOUNT:
        raise ValueError("Сумма перевода должна быть от 100 до 50 000 руб.")

    if amount <= LIMIT_1:
        return 50.0

    if amount <= LIMIT_2:
        return 100.0

    # Новое правило из Части 4:
    # для сумм свыше 40 000 руб. комиссия фиксированная — 500 руб.
    if amount > HIGH_AMOUNT_LIMIT:
        return 500.0

    return 200.0 + amount * 0.01