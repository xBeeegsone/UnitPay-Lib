from unitpay.protocol import unitpay_response
from unitpay.protocol.handlers.unitpay_method_handler import method_handler
from unitpay import unitpay_lib


def handle(ip: str, args) -> dict:
    unitpay_lib.provider.update_payment_status(args["params[account]"], "ERROR")
    return unitpay_response.error(args["params[errorMessage]"])


class unitpay_method_error(method_handler):
    pass
