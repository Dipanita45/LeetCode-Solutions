class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)

        i = 0
        res = ""
        C_in = 0

        while i < max(n1, n2) or C_in > 0:
            A = 0
            B = 0
            if i < n1:
                A = int(a[n1 - i - 1])
            if i < n2:
                B = int(b[n2 - i - 1])
            S = (A ^ B) ^ C_in
            C_out = ((A ^ B) & C_in) | (A & B)

            res = str(S) + res
            C_in = C_out
            i += 1
        return res
