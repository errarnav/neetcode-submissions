class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0]*len(position)

        dict1 = {}

        for i in range(len(position)):
            if position[i] in dict1:
                dict1[position[i]].append(i)
            else:
                dict1[position[i]] = [i]

        position.sort()
        speeds = []

        for i in range(len(position)):
            index = dict1[position[i]][0]
            del dict1[position[i]][0]
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