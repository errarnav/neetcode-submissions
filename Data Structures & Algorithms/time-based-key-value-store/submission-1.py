class TimeMap:

    def __init__(self):
        self.collection = {}
        


    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.collection:
            self.collection[key].append([value, timestamp])

        else:
            self.collection[key] = [[value, timestamp]]
        


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.collection:
            return ''

        relevant_list = self.collection[key]

        target = timestamp
        
        l = 0
        r = len(relevant_list) - 1  # 1 3 5 8

        if timestamp < relevant_list[0][1]:
            return ''
        elif timestamp > relevant_list[-1][1]:
            return relevant_list[-1][0]

        while l <= r:
            
            if timestamp > relevant_list[r][1]:
                index = r
                break
            elif timestamp < relevant_list[l][1]:
                index = l - 1
                break

            m = l + ((r - l) // 2)

            if timestamp > relevant_list[m][1]:
                l = m + 1

            elif timestamp < relevant_list[m][1]:
                r = m - 1
            
            else:
                index = m
                break

        return relevant_list[index][0]

        
