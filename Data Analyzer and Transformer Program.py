print("welcome to the data analyzer and transformer program ")

dataset_summary = {}

def input_data():
    """Accept 1D or 2D list data from the user."""
    global data

    print("Choose Data Type:")
    print("1. 1D Array")
    print("2. 2D Array")

    choice = input("Enter your choice: ")

    if choice == "1":
        values = input( "Enter data for a 1D array (separated by spaces):" )
        data = [int(x) for x in values.split()]
        print("Data has been stored successfully!")

    elif choice == "2":
        rows = int(input("Enter the number of rows: "))
        data = []

        for i in range(rows):
            row = input(
                f"Enter values for row {i + 1} (separated by spaces): "
            )
            data.append([int(x) for x in row.split()])

        print("Data has been stored successfully!")

        print("2D Array:")
        for row in data:
            print(" ".join(map(str, row)))

    else:
        print("Invalid choice! Please select 1 or 2.")


def flatten_data(data):
    """Convert 2D list into a 1D list for calculations."""
    if not data:
        return []

    if isinstance(data[0], list):
        return [item for row in data for item in row]

    return data.copy()


def calculate_sum(*args):
    """Calculate the sum of multiple values using *args."""
    return sum(args)


def display_summary(data):
    """Display basic statistics using built-in functions."""
    numbers = flatten_data(data)

    if not numbers:
        print("No data available. Please enter data first.")
        return

    global dataset_summary

    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)

    dataset_summary = {
        "Total Elements": len(numbers),
        "Minimum": minimum,
        "Maximum": maximum,
        "Sum": total,
        "Average": round(average, 2)
    }

    print("Data Summary:")
    print("- Total elements:", len(numbers))
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", calculate_sum(*numbers))
    print("- Average value:", f"{average:.2f}")


def factorial(n):
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def filter_data(data):
    """Filter values using lambda, map and filter."""
    numbers = flatten_data(data)

    if not numbers:
        print("\nNo data available. Please enter data first.")
        return

    threshold = int(
        input("\nEnter a threshold value to filter out data below this value:\n")
    )
    filtered_data = list(
        filter(lambda x: x >= threshold, numbers)
    )
    transformed_data = list(
        map(lambda x: x, filtered_data)
    )

    print(f"Filtered Data (values >= {threshold}):")
    print(", ".join(map(str, transformed_data)))


def sort_data(data):
    """Sort 1D data or sort rows in a 2D list."""
    numbers = flatten_data(data)

    if not numbers:
        print("No data available. Please enter data first.")
        return

    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        numbers.sort()
        print("\nSorted Data in Ascending Order:")

    elif choice == "2":
        numbers = sorted(numbers, reverse=True)
        print("\nSorted Data in Descending Order:")

    else:
        print("Invalid sorting choice!")
        return

    print(", ".join(map(str, numbers)))

    if isinstance(data[0], list):
        print("\nSorted 2D Array (each row sorted):")

        for row in data:
            sorted_row = sorted(row, reverse=(choice == "2"))
            print(" ".join(map(str, sorted_row)))


def get_statistics(*args):
    """Return minimum, maximum, sum and average values."""
    if not args:
        return None, None, 0, 0

    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)

    return minimum, maximum, total, average


def display_statistics(data):
    """Display dataset statistics and a **kwargs summary."""
    numbers = flatten_data(data)

    if not numbers:
        print("No data available. Please enter data first.")
        return

    minimum, maximum, total, average = get_statistics(*numbers)

    print("Dataset Statistics:")
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total)
    print("- Average value:", f"{average:.2f}")

    # **kwargs accepts keyword arguments
    show_summary(
        minimum=minimum,
        maximum=maximum,
        total=total,
        average=round(average, 2)
    )


def show_summary(**kwargs):
    """Display dataset information using **kwargs."""
    print("Dataset Characteristics Summary:")

    for key, value in kwargs.items():
        print(f"{key.title()}: {value}")


def main():
    """Display the main menu and run the Data Analyzer."""
    global data

    data = []

    while True:
        print("Welcome to the Data Analyzer and Transformer Program")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            display_summary(data)

        elif choice == "3":
            try:
                number = int(
                    input("\nEnter a number to calculate its factorial: ")
                )
                print(
                    f"Factorial of {number} is: {factorial(number)}"
                )
            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "4":
            filter_data(data)

        elif choice == "5":
            sort_data(data)

        elif choice == "6":
            display_statistics(data)

        elif choice == "7":
            print(
                "Thank you for using the Data Analyzer "
                "and Transformer Program. Goodbye!"
            )
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
