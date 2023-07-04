import random


def account_no():
    minimum = pow(10, 10 - 1)
    maximum = pow(10, 10) - 1
    return random.randint(minimum, maximum)
