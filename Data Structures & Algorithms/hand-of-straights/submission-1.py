class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False

        freq = {}

        for i in range(len(hand)):
            freq[hand[i]] = freq.get(hand[i], 0) + 1

        minH = list(freq.keys())
        heapq.heapify(minH)
        
        
        while minH:
            start = minH[0]
            
            for i in range(start, start + groupSize):
                if i not in freq:
                    return False

                freq[i] -= 1
                if freq[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
