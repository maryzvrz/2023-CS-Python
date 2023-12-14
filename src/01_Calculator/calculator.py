from operator import add, mul, sub
from operator import truediv as div
from typing import List


def prefix_evaluate(prefix_evaluation: str) -> int:
    if prefix_evaluation == "":
        return None

    stack = []

    for i in reversed(prefix_evaluation.split()):
        if i not in "+-*/":
            stack.append(int(i))
        if i in "+-*/":
            a = stack.pop()
            b = stack.pop()
            if i == "+":
                otvet = add(a, b)
            if i == "-":
                otvet = sub(a, b)
            if i == "*":
                otvet = mul(a, b)
            if i == "/":
                otvet = div(a, b)
            stack.append(otvet)

    return stack[0]


def to_prefix(equation: str) -> str:
    vidznak = set("+-*/")
    prior = {"+": 1, "-": 1, "*": 2, "/": 2}
    itogo = []
    znaki = []

    for i in reversed(equation.split()):
        if i not in vidznak:
            if i != "(" and i != ")":
                itogo.append(i)
            if i == "(":
                while znaki and znaki[-1] != ")":
                    itogo.append(znaki.pop())
                znaki.pop()
            if i == ")":
                znaki.append(i)
        if i in vidznak:
            while znaki and znaki[-1] != ")" and prior[i] <= prior.get(znaki[-1], 0):
                itogo.append(znaki.pop())
            znaki.append(i)
    while znaki:
        itogo.append(znaki.pop())

    return " ".join(list(reversed(itogo)))


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
