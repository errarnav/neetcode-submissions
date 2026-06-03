class Solution:

    def encode(self, strs: List[str]) -> str:
        main_string = ""
        for string in strs:
            length = len(string)
            main_string += str(length) + '#' + string
        return main_string

    def decode(self, main_string: str) -> List[str]:
        main_list = []
        pointer = 0

        while pointer < len(main_string):
            right_pointer = pointer

            while main_string[right_pointer] != '#':
                right_pointer += 1

            length_of_next_string = int(main_string[pointer : right_pointer])
            
        
            next_string = main_string[right_pointer + 1 : right_pointer + 1 + length_of_next_string]
            main_list.append(next_string)

            pointer = right_pointer + length_of_next_string + 1

        return main_list

