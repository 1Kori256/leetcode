class Solution:
    def intToRoman(self, num: int) -> str:
        f = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        s = [x.replace("X", "C").replace("V", "L").replace("I", "X") for x in f]
        t = [x.replace("X", "M").replace("V", "D").replace("I", "C") for x in f]

        number_of_ms = num // 1000
        a = (num % 1000) // 100
        b = (num % 100) // 10
        c = num % 10

        return "M" * number_of_ms + t[a] + s[b] + f[c]
        


