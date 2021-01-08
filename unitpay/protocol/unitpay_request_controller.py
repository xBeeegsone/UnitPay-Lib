from unitpay.protocol import unitpay_response
from unitpay.protocol.handlers import unitpay_method_check, unitpay_method_error, unitpay_method_pay, unitpay_method_handler

method_registry = {
    "check": unitpay_method_check,
    "error": unitpay_method_error,
    "pay": unitpay_method_pay
}


def get_method(method: str) -> unitpay_method_handler:
    return method_registry[method] if method in method_registry else None


def handle(ip: str, args) -> dict:
    from unitpay.protocol import unitpay_allowed_ips
    if ip not in unitpay_allowed_ips.ip_list:
        return unitpay_response.error("Неизвестный IP-Адрес, не принадлежащий UnitPay.")
    method: unitpay_method_handler = get_method(args['method'])
    return method.handle(ip, args) \
        if method is not None \
        else unitpay_response.error("Неизвестный метод -> " + args['method'])
