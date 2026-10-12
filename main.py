import json


class Main:
    def handle(self, input_str):
        """
        ***********************************************
        * This method parses the input string and     *
        * prints the result as a string.              *
        ***********************************************

        Format of input_str: "<space-separated values>"
        Example: "1 2 3"

        The input string is split by spaces and the values are
        stored in the list `input_list`. You may need to typecast
        them depending on the problem statement.

        Store your final answer in `result`. It can be any value:
        a number, a string, a boolean, a list, a nested list or a
        dictionary. The last line prints it as a string, e.g.
            [[1, 2], [3]]      -> [[1,2],[3]]
            ["a", "b"]         -> ["a","b"]
            {"count": 2}       -> {"count":2}
            True               -> true
        Don't change that line.
        """

        input_list = input_str.strip().split()
        result = None

        # Start your implementation from here.

        print(self.stringify(result))

    def stringify(self, value):
        return json.dumps(value, separators=(",", ":"))
