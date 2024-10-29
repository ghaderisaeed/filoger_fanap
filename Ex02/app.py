# app.py
from utils.random_number import generate_random_number
from utils.make_array import generate_random_array
from utils.identify import identify_result
import numpy as np

def main():
    user_input = 0
    while user_input==0:
        try:
            user_input = int(input("Please enter a number: "))
            if user_input < 1:
                print(f'**************  Error  **************\n', 'Please enter a natural number (1, 2, 3, etc.).')
                # print('*'*20 + '  Error  ' +'*'*20, '\nPlease enter a natural number (1, 2, 3, etc.).')
                user_input = 0
            else:
                random_array = generate_random_array(user_input)
                print(f"random array = {random_array}")

                max_value = np.max(random_array)
                print(f"Maximum value = {max_value}")

                result = identify_result(max_value)
                print(result)

        except ValueError:
            print('**************  Error  **************\n', "Please enter a number.")


if __name__ == "__main__":
    main()
