"""
These are the classed you need to implement. Read the tutorial in the Section 3 - Python Review and follow the instructions in it to
implement the classes below. 
"""
class Square:
    """
    Square class:
    Args:
        name (str): The name of the square
        length (int): The length of the square

    Returns:
        None
    """
    def __init__(self):
        pass


class Multiplier:
    """
    Multiplier class
    Args:
        None
    """
    def __call__(self):
        """
        Implement the __call__ method here
        Args:
            num1 (int): The first number
            num2 (int): The second number

        Returns:
            result (int): The result of the multiplication
        """
        pass


class LoggingTape:
    """
    LoggingTape class to record the logs
    """
    def __init__(self):
        """
        Initialize variables
        """
        self.logs = ...

    def __enter__(self):
        """
        Called when entering the context
        """
        pass

    def __exit__(self, *args):
        """
        Called when exiting the context
        """
        pass

    def add_to_log(self, new_log):
        """
        Add a new log to the logs
        """
        pass

    def print_logs(self):
        """
        Print the logs
        """
        for log in self.logs: print(log)


class Logger:
    """
    Logger class to record the logs
    """
    # Define the logging_tape here
    logging_tape: LoggingTape | None = None


class Car(Logger):
    def travel(self, distance):
        self.logging_tape.add_to_log(f"Traveled Distance {distance}")


# Local tests
if __name__ == "__main__":
    # Create a square object
    square1 = Square("square1", 5)
    assert square1.name == "square1"
    assert square1.length == 5

    # Create a multiplier object
    multiplier = Multiplier()
    assert multiplier(5, 10) == 50

    # Create a logging tape object
    with LoggingTape() as tape: #runs LoggingTape's __enter__()
        #Logger.logging_tape is now defined as tape (from line 1)!
        tape.add_to_log("Hi!")
    #runs LoggingTape's __exit__()
    #Now Logger.logging_tape is defined as None
    tape.print_logs()

    # Create a car object
    car = Car()
    with LoggingTape() as tape:
        car.travel(5)
    tape.print_logs()