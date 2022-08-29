# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import gauss


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    temp = [[1, 1, 2], [0, 1, -5], [0, 0, 1]]
    sol = [8, -9, 2]

    print(gauss.lower_triangular_matrix_solve(temp, sol))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
