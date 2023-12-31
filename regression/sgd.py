### Algunos intentos de escribir un Gradient Descent Algorithm
import numpy as np

def gradient_descent(gradient, start, learn_rate, n_iter):
    vector = start
    for _ in range(n_iter):
        diff = learn_rate * gradient(vector)
        vector += diff
    return vector