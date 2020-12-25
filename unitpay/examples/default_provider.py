from unitpay.iprovider import iprovider


def payment_exists(account: str) -> bool:
    return True


def check_sum(account: str, sum_param: float, currency: str) -> bool:
    return currency == "RUB" and sum_param >= 1.00


def update_payment_status(account: str, status: str) -> any:
    print("Обновлен статус платежа для " + account + " на " + status)


def give_item(account: str) -> bool:
    print("Успешная покупка для " + account)
    return True


class default_provider(iprovider):
    pass
