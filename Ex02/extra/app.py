from game import RandomArray
import argparse
import numpy as np

def get_user_input():
    user_input = False
    while user_input==False:
        try:
            user_input = int(input("Please enter a number: "))
            if user_input < 1:
                print('**************  Error  **************\n', 'Please enter a natural number (1, 2, 3, etc.).')
                user_input = False
            else:
                return user_input
        except ValueError:
            print('**************  Error  **************\n', "Please enter a number.")

def main():

    parser = argparse.ArgumentParser(description='Generate random array and determine the outcome.')
    parser.add_argument('--number', type=int, help='Enter a number')
    
    args = parser.parse_args()

    if args.number is not None:
        user_number = args.number

    else:
        user_number = get_user_input()

    if user_number is not None:
        RA = RandomArray()
        random_array = RA.generate_random_array(user_number)
        print(f"random array = {random_array}")

        max_value = np.max(random_array)
        print(f"Maximum value = {max_value}")

        result = RA.identify_result(max_value)
        print(result)


if __name__ == "__main__":
    main()