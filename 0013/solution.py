class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        special = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        while s:
            skip = False
            for x in special:
                if s.endswith(x):
                    num += special[x]
                    s = s[:-2]
                    skip = True
            if skip:
                continue
            num += m[s[-1]]
            s = s[:-1]
        return num

