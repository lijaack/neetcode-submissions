class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res=self.store[key]
        l=0
        r=len(res)-1
        val = ''
        while l <= r:

            mid = (l+r)//2
            if res[mid][0]==timestamp:
                return res[mid][1]
            if res[mid][0] < timestamp:
                val=res[mid][1]
                l=mid+1
            else:
                r=mid-1
        return val


        
