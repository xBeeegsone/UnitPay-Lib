from unitpay import unitpay_lib
from unitpay.examples import example_provider
from unitpay.protocol import unitpay_request_controller

unitpay_lib.provider = example_provider
unitpay_lib.PUBLIC_KEY = "EXAMPLE-KEY-1337"
unitpay_lib.PRIORITY_PAYMENT_METHOD = "card"

controller: unitpay_request_controller = unitpay_request_controller


check = controller.handle("52.19.56.234", args={
    "method": "check",
    "params[account]": "test",
    "params[sum]": 10.00,
    "params[orderCurrency]": "RUB",
    "params[orderSum]": 1.00
})

pay = controller.handle("52.19.56.234", args={
    "method": "pay",
    "params[account]": "test",
    "params[sum]": 10.00,
    "params[orderCurrency]": "RUB",
    "params[orderSum]": 10.00
})

error = controller.handle("52.19.56.234", args={
    "method": "error",
    "params[account]": "test",
    "params[sum]": 10.00,
    "params[orderCurrency]": "RUB",
    "params[orderSum]": 10.00,
    "params[errorMessage]": "Недостаточно средств"
})

link = unitpay_lib.provider.generate_payment_link("test", 1.00, "Покупка камней")


print("")
print("")
print("метод                        json-ответ")
print("")
print("check                        " + str(check))
print("pay                          " + str(pay))
print("error                        " + str(error))
print("")
print("")
print("Платёжная ссылка: " + link)
