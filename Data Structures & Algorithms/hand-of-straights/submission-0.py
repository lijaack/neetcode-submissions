class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            #find the lowest card
            while count[start - 1]:
                start -= 1
            
            #this loop make sure we get all duplicates
            while count[start]:
                #start card# + last card of hand
                for i in range(start, start + groupSize):
                    #if card dont exist its false
                    if not count[i]:
                        return False
                    # we remove the card from count
                    count[i] -= 1
                #
        return True