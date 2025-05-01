class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        used = [0 for _ in range(len(words))]
        max_score = 0
        valid_letters = [0 for _ in range(26)]
        for letter in letters:
            valid_letters[ord(letter) - ord("a")] += 1
        current_index = 0
        current_score = 0

        while True:
            if current_index >= len(words):
                found = False
                for i in range(len(words) - 1, -1, -1):
                    if used[i] == 1:
                        current_index = i
                        found = True
                        break
                if found:
                    continue
                else:
                    break
            if used[current_index] == 0:
                word_letters = [0 for _ in range(26)]
                for letter in words[current_index]:
                    word_letters[ord(letter) - ord("a")] += 1
                if not all(valid_letters[i] >= word_letters[i] for i in range(26)):
                    current_index += 1
                    continue
                for i in range(26):
                    valid_letters[i] -= word_letters[i]
                    current_score += word_letters[i] * score[i]
                used[current_index] = 1
                max_score = max(max_score, current_score)
                current_index += 1
            else:
                for letter in words[current_index]:
                    valid_letters[ord(letter) - ord("a")] += 1
                    current_score -= score[ord(letter) - ord("a")]
                used[current_index] = 0
                current_index += 1


        return max_score
                




                