class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        result = 0

        def count_valid_substrings(start):
            vowel_count = {v: 0 for v in vowels}
            consonants = 0
            count = 0

            for i in range(start, n):
                if word[i] in vowels:
                    vowel_count[word[i]] += 1
                else:
                    consonants += 1

                if consonants > k:
                    break

                if consonants == k and all(vowel_count.values()):
                    count += 1

            return count

        for i in range(n):
            result += count_valid_substrings(i)

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.countOfSubstrings("aeioqq", 1) == 0
    assert s.countOfSubstrings("aeiou", 0) == 1
    assert s.countOfSubstrings("ieaouqqieaouqq", 1) == 3

    print("All Passed!")
