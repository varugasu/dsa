import brute_force

test_cases = [
    {"input": "a", "expected": "a"},
    {"input": "babad", "expected": "bab"},
    {"input": "abcddcba", "expected": "abcddcba"},
    {"input": "fasaabbaaheqw", "expected": "aabbaa"},
]

def test_brute_force():
    for test_case in test_cases:
        assert brute_force.solution(test_case["input"]) == test_case["expected"]

