class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        result = ""
        for c in order:
            if c in freq:
                result += c * freq[c]
                del freq[c]
        for c, f in freq.items():
            result += c * f
        return result
