def get_mask_card_number(card_number: int) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску"""

    card_number_str = str(card_number)

    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску"""

    account_str = str(account)

    return f"**{account_str[-4:]}"


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
