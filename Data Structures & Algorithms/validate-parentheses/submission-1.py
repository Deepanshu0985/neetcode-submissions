class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in "({[":
                st.append(char)
            else:
                if not st:
                    return False
                
                top = st[-1]

                if (top=='(' and char ==')') or (top=='{' and char =='}') or (top=='[' and char ==']'):
                    st.pop()
                else:
                    return False
        return len(st)==0
        