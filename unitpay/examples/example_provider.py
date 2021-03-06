from unitpay.iprovider import iprovider


def payment_exists(account: str) -> bool:
    return True


def check_sum(account: str, sum_param: float, currency: str) -> bool:
    return currency == "RUB" and sum_param == 1337.00


def update_payment_status(account: str, status: str) -> any:
    print("Обновлен статус платежа для " + account + " на " + status)


def give_item(account: str) -> bool:
    print("Успешная покупка для " + account)
    return True


def generate_payment_link(account: str, sum: float, desc: str) -> str:
    return iprovider.generate_payment_link(account, sum, desc)


class example_provider(iprovider):
    pass
