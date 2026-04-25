class Solution:
    def dailyTemperatures(self, temperatures):
        st = []  # [index, temp]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][1]:
                stackind, stackT = st.pop()
                res[stackind] = i - stackind

            st.append([i, temp])

        return res