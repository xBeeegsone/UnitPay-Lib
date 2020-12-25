from unitpay.protocol import unitpay_response
from unitpay.protocol.handlers import unitpay_method_check, unitpay_method_error, unitpay_method_pay, unitpay_method_handler

method_registry = {
    "check": unitpay_method_check,
    "error": unitpay_method_error,
    "pay": unitpay_method_pay
}


def get_method(method) -> unitpay_method_handler:
    if method not in method_registry:
        return None
    return method_registry[method]


def handle(ip, args) -> any:
    from unitpay.protocol import unitpay_allowed_ips
    if ip not in unitpay_allowed_ips.ip_list:
        return unitpay_response.error("Неизвестный IP-Адрес, не принадлежащий UnitPay.")
    method = args['method']
    try:
        return get_method(method).handle(ip, args)
    except SyntaxError | TypeError:
        return unitpay_response.error("Неизвестный метод -> " + method)
