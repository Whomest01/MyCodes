"""
SimpleCalc.py

This program is simulating a simple calculator with some ascii art and the four basic arithmetic operations:
add, subtract, multiply, division.

The ASCII art was generated using this site:
http://patorjk.com/software/taag/

I wrote this program using object oriented programming, although I could also write it without object oriented.
I simply liked it more this way.

This program was created by Nativ Weiss.
email: nativsemail@gmail.com
"""


class SimpleCalc:
    """ Class and methods definitions for the objects. """
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def add(self, num1, num2):
        return self._num1 + self._num2

    def sub(self, num1, num2):
        return self._num1 - self._num2

    def mul(self, num1, num2):
        return self._num1 * self._num2

    def div(self, num1, num2):
        return self._num1 / self._num2


def clear_screen(wait_time=0):
    """
    This function clears the screen. It will run the appropriate clear screen commands based on the OS (Windows or
    Unix).
    Unless other value specified for wait_time parameter, the default timeout is 0 seconds.
    :param wait_time: how many seconds to wait before clearing the screen.
    :type wait_time: int.
    :return: none.
    """
    # Import the necessary functions to determine which OS we're using.
    from os import system, name

    # Import the sleep function to wait before clearing the screen.
    from time import sleep
    sleep(wait_time)

    # Check if the OS is Windows or Unix, in order to run the appropriate clear screen command.
    if name == "nt":  # for Windows OS
        _ = system("cls")
    else:  # for Mac and Linux OS
        _ = system("clear")


def GetFirstNum():
    """ Reads the first number and checks if it's valid. The input must be a float number. """
    is_float = False
    while not is_float:
        try:
            firstnum = float(input("Enter first number: "))
        except ValueError:
            print("Number must be float. Try again.")
        else:
            is_float = True
            return firstnum


def GetSecondNum():
    """ Reads the second number and checks if it's valid. The input must be a float number."""
    is_float = False
    while not is_float:
        try:
            secondnum = float(input("Enter second number: "))
        except ValueError:
            print("Number must be float. Try again.")
        else:
            is_float = True
            return secondnum


def DisplayMenu():
    """
    Displays the menu and waiting for the user's input.
    Will also perform a check that the option selected is valid, and from the input.
    The menu will be displayed as long as the input is not valid.
    """
    menu_art = ("""   
    ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗ ██████╗ █████╗ ██╗      ██████╗
    ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ███████╗██║██╔████╔██║██████╔╝██║     █████╗  ██║     ███████║██║     ██║     
    ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██║     ██╔══██║██║     ██║     
    ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗╚██████╗██║  ██║███████╗╚██████╗
    ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝""")
    choice = 6  # Just used a number that is outside of the range as initial value to force displaying the menu.
    while choice not in range(5):
        print(menu_art)
        print("\n")
        print("Select one of the options\n"
              "=========================\n\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Division\n"
              " \n"
              "0. Exit\n")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("You must select one option from the menu. Please try again.")
            clear_screen(5)
        else:
            if choice not in range(5):
                print("You must select one option from the menu. Please try again.")
                clear_screen(5)
            else:
                return choice


def main():
    clear_screen()
    selection = 9
    while selection != 0:
        selection = DisplayMenu()
        if selection == 0:
            print("Exiting...")
            clear_screen(5)
            break

        num1 = GetFirstNum()
        num2 = GetSecondNum()
        while num2 == 0 and selection == 4:
            print("Error detected: Division by zero. Choose another number.")
            num2 = GetSecondNum()
        calc = SimpleCalc(num1, num2)

        if selection == 1:
            print("Result:", calc.add(num1, num2), "\n")
            clear_screen(5)
        elif selection == 2:
            print("Result:", calc.sub(num1, num2), "\n")
            clear_screen(5)
        elif selection == 3:
            print("Result:", calc.mul(num1, num2), "\n")
            clear_screen(5)
        elif selection == 4:
            print("Result:", calc.div(num1, num2), "\n")
            clear_screen(5)


if __name__ == '__main__':
    main()
