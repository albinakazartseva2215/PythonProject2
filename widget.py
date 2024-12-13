import typing
from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция mask_account_card умеет обрабатывать информацию как о картах, так и о счетах.
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером."""
    type_ = []
    digit_ = []
    for char in account_card:
        if char.isdigit():
            digit_.append(char)
        else:
            type_.append(char)

    type_card = "".join(type_)
    digit_card = "".join(digit_)

    mask_digit_card = (
        get_mask_card_number(int(digit_card))
        if len(digit_card) == 16
        else get_mask_account(int(digit_card))
    )
    return f"{type_card} {mask_digit_card}"


def get_date(date_str: str) -> str:
    """Функция get_date, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"


print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
