def preprocess_string(s: str) -> str:
    if not s:
        return "^$"
    result = "^"
    for char in s:
        result += f"#{char}"
    result += "#$"
    return result


def solution(s: str) -> str:
    T = preprocess_string(s)
    n = len(T)
    P = [0] * n
    center = 0
    right = 0
    for i in range(1, n - 1):
        # T[mirror] and T[i] only start to match when we have a center
        mirror = 2 * center - i
        if i < right:
            # this line ensures we expand over what was already computed
            P[i] = min(right - i, P[mirror])

        # expand
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > right:
            center = i
            right = i + P[i]

    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    start = (center_index - max_len) // 2
    return s[start : start + max_len]


solution("testaaaabbaaaagnere")
