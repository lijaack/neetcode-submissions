class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for num in hand:
            start = num
            while(count[start-1]):
                start = start-1
            
            while count[start]:

                for i in range(start, start+groupSize):
                    if not count[i]:
                        return False
                    count[i] = count[i]-1
        return True
        