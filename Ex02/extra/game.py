import numpy as np

class RandomArray:
    """
    RandomArray
    ===========

    Provides
    1. Generates a random number between 0 and 100
    2. Generates an array of random numbers between 0 and 100 based on the user input
    3. Identifies the result (Win or Fail) based on the maximum value in the arra
    """
    def __init__(self):
        pass
    
    def __repr__(self) -> str:
        return str(self.generate_random_number())

    def generate_random_number(self):
        """
        Generates a random number between 0 and 100.

        Returns:
            int: A random number.
        """
        return np.random.randint(0, 101)

    def generate_random_array(self, size:int):
        """
        Generates an array of random numbers between 0 and 100 based on the user input.

        Args:
            size (int): The size of the array to be generated.

        Returns
            out : ndarray of ints
            size-shaped array of random integers from the appropriate distribution
        """

        return np.random.randint(0, 101, size)

    def identify_result(self, max_value:int):
        """
        Identifies the result (Win or Fail) based on the maximum value in the array.

        Args:
            max_value (int): The maximum value in the generated array.

        Returns:
            str: The result (Win or Fail).
        """
        if max_value > 70:
            return "*****   Win   *****"
        else:
            return "-----  Fail   -----"
        