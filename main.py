class Main:
    def handle(self, input_str):
        """
        ***********************************************
        * This method parses the input string and     *
        * extracts the required value.                *
        ***********************************************

        Format of input_str: "Input"
        Example: "Hello"

        The input string is split by spaces and the first value
        is retrieved and stored in the variable `input`.

        Once retrieved, it is available as string data for you
        to implement the solution. You may need to typecast it
        depending on the problem statement.

        Your final output needs to be printed to the console.
        """

        input_list = input_str.strip().split(" ")
        input = input_list[0]

        # Start your implementation from here.
        print("Input String:", input)