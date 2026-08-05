class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dayToWarm=[0]*len(temperatures)

        dayStack=[]

        #loop through temperatures. we can track day and temp
        for  day,temp in enumerate(temperatures):

        #we can stack [temp,day] into day stack
        #we will compare future temp to dayStack[-1][temp] to todays temp
            while dayStack and  dayStack[-1][0] < temp:
        #if todays temp is higher, we use todays day and - daystack[-1][day] to get the days to warm day
        #we will push daytowarm[daystack[-1][day]] = todays day and - daystack[-1][day]
                dayToWarm[dayStack[-1][1]] = day - dayStack[-1][1]
                dayStack.pop()
        # it will while loop until todays temp is less than the daystack[-1][temp]
            dayStack.append([temp,day])
        return dayToWarm