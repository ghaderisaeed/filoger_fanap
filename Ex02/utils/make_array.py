from .random_number import generate_random_number
import numpy as np

def generate_random_array(size):
    return np.array([generate_random_number() for _ in range(size)])


