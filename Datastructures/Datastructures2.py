class Solution:
	def braces(self, A):
        st = []

        for ch in A:
            if ch == ')':
                top = st[-1]
                st.pop()

                flag = True

                while top != '(':
                    if top in ['+', '-', '*', '/']:
                        flag = False

                    top = st[-1]
                    st.pop()

                if flag:
                    return 1
            else:
                 st.append(ch)
        return 0