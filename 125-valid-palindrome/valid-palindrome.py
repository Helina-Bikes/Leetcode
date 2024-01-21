class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Function to check if a character is alphanumeric
        def is_alphanumeric(char):
            return char.isalnum()

        # Convert the string to lowercase and filter out non-alphanumeric characters
        cleaned_s = list(filter(is_alphanumeric, s.lower()))

        # Use two pointers to check if the string is a palindrome
        left, right = 0, len(cleaned_s) - 1
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1

        return True
