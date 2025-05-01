class Solution:
    def myAtoi(self, s: str) -> int:
        f = ""
        started = False
        hasd = False
        for c in s:
            if (c == "-" or c == "+" or c.isdigit()):
                if not started:
                    if c == "-":
                        f += "-"
                    elif c == "+":
                        pass
                    else:
                        hasd = True
                        f += c
                    started = True
                else:
                    if c.isdigit():
                        f += c
                        hasd = True
                    else:
                        break
            else:
                if c == " " and not started:
                    continue
                else:
                    break
        if not hasd:
            return 0

        x = int(f)
        C = 2 ** 31
        if x < -C:
            return -C
        if x > C - 1:
            return C - 1
        return x