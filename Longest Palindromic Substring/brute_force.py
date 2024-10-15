def solution(s: str) -> str:
    if len(s) <= 1:
        return s

    longest_palindrome = s[0]
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            current_substring = s[i : j + 1]
            potential_palindrome = current_substring[::-1]
            if (
                len(current_substring) > len(longest_palindrome)
                and current_substring == potential_palindrome
            ):
                longest_palindrome = current_substring
    return longest_palindrome
