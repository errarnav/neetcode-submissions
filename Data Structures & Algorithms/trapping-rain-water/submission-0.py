class Solution:
    def trap(self, height: List[int]) -> int:
        max_height_l = []
        max_height_r = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                max_height_l.append(0)
            
            else:
                new_max_height = max(max_height_l[i - 1], height[i - 1])
                max_height_l.append(new_max_height)

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                max_height_r[i] = 0
            
            else:
                new_max_height = max(height[i + 1], max_height_r[i + 1])
                max_height_r[i] = new_max_height

        res = [0] * len(height)

        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                water_trapped = 0
                res[i] = water_trapped

            else:
                water_trapped = min(max_height_r[i], max_height_l[i]) - height[i]

                if water_trapped < 0:
                    res[i] = 0
                else:
                    res[i] = water_trapped
        
        total = 0
        for i in range(len(res)):
            total += res[i]


        return total