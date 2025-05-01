class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        guess = 1
        while True:
            y = guess * guess
            if y >= x:
                if y == x:
                    return guess
                break
            guess *= 2
        # [guess / 2, guess) bin search
        def bin_search(bottom, top):
            mid = (top - bottom) // 2 + bottom
            y = mid * mid
            if x >= y:
                if x < y + 2 * mid + 1:
                    return mid
                else:
                    return bin_search(mid, top)
            else:
                return bin_search(bottom, mid)
        return bin_search(guess // 2 - 1, guess)
            
