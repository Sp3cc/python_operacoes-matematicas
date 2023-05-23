from .soma import soma


def mult(num1, num2):
    acc = 0

    for i in range(num1):
        acc = soma(acc, num2)

    return acc