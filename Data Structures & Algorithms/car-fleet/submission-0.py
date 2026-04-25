class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        pairs = [[p,s] for p,s in zip(position,speed)]

        for p,s in sorted(pairs)[::-1]:
            t = (target-p)/s
            st.append(t)
            if (len(st)>=2 and st[-2]>=st[-1]):
                st.pop()
        return len(st)