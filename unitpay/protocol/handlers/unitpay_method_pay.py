from unitpay.protocol import unitpay_response
from unitpay.protocol.handlers.unitpay_method_handler import method_handler
from unitpay import unitpay_lib


def handle(ip, args) -> any:
    account: str = args["params[account]"]
    if unitpay_lib.provider.give_item(account):
        unitpay_lib.provider.update_payment_status(account, "SUCCESS")
        return unitpay_response.result()
    else:
        return unitpay_response.error("Проблема при выдаче товара. Повторите попытку позже.")


class unitpay_method_pay(method_handler):
    pass
