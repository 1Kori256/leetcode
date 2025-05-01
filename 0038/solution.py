class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for i in range(2, n + 1):
            new = ""
            current_count = 0
            current_c = ""
            for i, c in enumerate(num):
                if i == 0:
                    current_count = 1
                    current_c = c
                elif i > 0 and c == num[i-1]:
                    current_count += 1
                else:
                    new += str(current_count) + current_c
                    current_count = 1
                    current_c = c
            new += str(current_count) + current_c
            num = new                
        return num