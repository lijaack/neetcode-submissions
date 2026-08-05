class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_until_warmer = [0] * len(temperatures)

        # Stores (temperature, day_index) waiting for a warmer day
        decreasing_stack = []

        for current_day, current_temp in enumerate(temperatures):

            # Current temperature solves previous colder days
            while decreasing_stack and current_temp > decreasing_stack[-1][0]:
                previous_temp, previous_day = decreasing_stack.pop()

                days_until_warmer[previous_day] = current_day - previous_day

            # Current day waits for a future warmer day
            decreasing_stack.append((current_temp, current_day))

        return days_until_warmer