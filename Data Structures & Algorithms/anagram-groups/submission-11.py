class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        list_final = []
        for item in strs:
            print(item)
            list1 = sorted(item)
            print(list1)
            sorted_item = "".join(list1)
            print(sorted_item)

            if sorted_item in dict1.keys():
                dict1[sorted_item].append(item)
            else:
                dict1[sorted_item] = [item]

        for value in dict1.values():
            list_final.append(value)

        return list_final