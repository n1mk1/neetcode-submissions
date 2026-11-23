class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1]<t: #[(index, temperture)]
                stack_i, stack_t = stack.pop()
                result[stack_i] = i - stack_i

            stack.append((i, t)) # if stack empty
            
        return result
                
                