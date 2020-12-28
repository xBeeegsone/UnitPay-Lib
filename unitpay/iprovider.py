def payment_exists(account: str) -> bool:
    pass


def check_sum(account: str, sum_param: float, currency: str) -> bool:
    pass


def update_payment_status(account: str, status: str) -> any:
    pass


def give_item(account: str) -> bool:
    pass


def generate_payment_link(account: str, sum: float, desc: str) -> str:
    from unitpay import unitpay_lib
    return "https://unitpay.ru/pay/" + unitpay_lib.PUBLIC_KEY + "/" + unitpay_lib.PRIORITY_PAYMENT_METHOD + "?sum=" + str(sum) + "&account=" + account + "&desc=" + desc


class iprovider:
    @classmethod
    def generate_payment_link(cls, account, sum, desc):
        return generate_payment_link(account, sum, desc)
