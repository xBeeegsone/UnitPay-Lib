from unitpay.protocol import unitpay_response
from unitpay.protocol.handlers.unitpay_method_handler import method_handler
from unitpay import unitpay_lib


def update_and_get_result(account: str, reason: str):
    unitpay_lib.provider.update_payment_status(account, "ERROR")
    return unitpay_response.error(reason)


def handle(ip: str, args) -> dict:
    account: str = args["params[account]"]
    sum_param: float = args["params[sum]"]
    currency: str = args["params[orderCurrency]"]
    if not unitpay_lib.provider.payment_exists(account):
        return unitpay_response.error("Такого платежа не существует")
    if sum_param != args["params[orderSum]"] or not unitpay_lib.provider.check_sum(account, sum_param, currency):
        return update_and_get_result(account, "Сумма заказа не равна сумме списания или реальной цене товара")
    unitpay_lib.provider.update_payment_status(account, "CHECKED")
    return unitpay_response.result()


class unitpay_method_check(method_handler):
    pass
