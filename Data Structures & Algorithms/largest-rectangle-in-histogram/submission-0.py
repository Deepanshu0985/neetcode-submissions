class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = []
        right = [0] * n
        st = []
        ans = float('-inf')

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if not st:
                left.append(-1)
            else:
                left.append(st[-1])
            
            st.append(i)

        st.clear()

        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if not st:
                right[i] = n   
            else:
                right[i] = st[-1]
            
            st.append(i)

        for i in range(n):
            width = right[i] - left[i] - 1
            ans = max(ans, heights[i] * width)

        return ans