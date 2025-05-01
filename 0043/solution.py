class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s = [0] * (len(num1) + len(num2))

        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                current = int(num1[i]) * int(num2[j]) + s[i + j + 1]
                s[i + j] += current // 10
                s[i + j + 1] = current % 10

        if all(x == 0 for x in s):
            return '0'
       
        nonzeros_index = next((i for i, x in enumerate(s) if x), None)
        return ''.join(map(str, s[nonzeros_index:]))