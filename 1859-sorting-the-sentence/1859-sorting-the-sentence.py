class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = sorted(words, key=lambda word: int(word[-1]))
        original_sentence = [word[:-1] for word in sorted_words]
        result = ' '.join(original_sentence)
        return result
