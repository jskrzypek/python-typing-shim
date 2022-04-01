import math


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))
