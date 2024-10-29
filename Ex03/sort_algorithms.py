import numpy as np

def get_user_choice():
    while True:
        algorithms = ['quicksort','mergesort','heapsort']
        choice = input("Please select a sorting algorithm:\n 1) quicksort\n 2) mergesort\n 3) heapsort\nSelect an option: ")
        if choice.lower() in algorithms:
            return choice.lower()
        elif choice.isdigit():
            choice = int(choice)
            if choice in [1,2,3]:
                return algorithms[choice-1]
            else:
                print("Invalid choice. Please select again.")
        else:
            print("Invalid choice. Please select again.")

def get_user_input():
    while True:
        choice = input("Enter 'random' for random numbers or 'user' for user input: ")
        if choice.lower() == 'random':
            lower = int(input("Enter the lower bound for random numbers: "))
            upper = int(input("Enter the upper bound for random numbers: "))
            count = int(input("Enter the number of elements: "))
            return np.random.randint(lower, upper, count)
        elif choice.lower() == 'user':
            numbers = input("Enter the numbers separated by spaces: ")
            try:
                return np.array(list(map(int, numbers.split())))
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")
        else:
            print("Invalid input type. Please select again.")

def main():
    algorithm = get_user_choice()
    numbers = get_user_input()
    print(f"Original array: {numbers}")
    sorted_numbers = np.sort(numbers, kind=algorithm)
    print(f"Sorted array using {algorithm}: {sorted_numbers}")

if __name__ == "__main__":
    main()