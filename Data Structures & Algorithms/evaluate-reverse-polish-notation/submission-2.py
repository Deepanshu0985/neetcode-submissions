class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for num in tokens:
            if num not in "+-*/":
                st.append(int(num))   # convert here
            else:
                a = st.pop()
                b = st.pop()

                if num == '+':
                    st.append(b + a)
                elif num == '-':
                    st.append(b - a)
                elif num == '*':
                    st.append(b * a)
                else:
                    st.append(int(b / a))   # fix here

        return st.pop()