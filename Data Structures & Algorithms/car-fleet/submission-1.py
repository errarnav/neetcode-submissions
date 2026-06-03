class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0]*len(position)

        dict1 = {}

        for i in range(len(position)):
            dict1[position[i]] = i

        position.sort()
        speeds = []

        for i in range(len(position)):
            index = dict1[position[i]]
            curr_speed = speed[index]
            speeds.append(curr_speed)
        

        for i in range(len(position)):
            miles_rem = target - position[i]
            time[i] = round(miles_rem/speeds[i], 1)

        count = 1 # 3 4.5 10 3

        for i in range(len(time) - 1, -1, -1):
            if i == len(time) - 1:
                currentMax = time[i]
            else:
                if time[i] > currentMax:
                    count += 1
                    currentMax = time[i]
                else:
                    continue

        return count