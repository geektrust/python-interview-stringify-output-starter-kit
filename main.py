import json


class Main:
    def handle(self, input_str):
        # Do not modify the code below this line
        input_list = input_str.strip().split()                    
        result = self.group_anagrams(input_list)
        print(self.stringify(result))

    def group_anagrams(self, input_list: list[str]) -> list[list[str]]:
        result = []
        # Implement the logic to group anagrams here
        return result
    
    def stringify(self, value):
        return json.dumps(value, separators=(",", ":"))
