class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = []
        for string in strs:
            final_str.append(str(len(string)))
            final_str.append('#')
            final_str.append(string)

        stringg = "".join(final_str)
        return stringg
       
    def decode(self, main_string: str) -> List[str]:
        
        main_list = []
        i = 0
        
        while i < len(main_string):
            j = i

            while main_string[j] != '#':
                j += 1

            length = int(main_string[i : j])

            current_string = main_string[j + 1: j + 1 + length]

            main_list.append(current_string)

            i = j + 1 + length

        return main_list


            

        
