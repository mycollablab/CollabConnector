import re


class Regex:
    pattern = None

    class Pattern:
        pattern = ""
        regex = "^"
        score = 0

        def __init__(self, pattern: str = None):
            if pattern:
                self.update(pattern)

        def update(self, pattern):
            self.pattern = pattern
            pattern = iter(pattern)
            for char in pattern:
                if char in [".", "\\"]:
                    continue
                elif char.isnumeric():
                    self.regex += char
                    self.score = self.score + 10  # Exact Match
                elif char == r"+":
                    self.regex += r"\\\+"
                    self.score = self.score + 10  # Exact Match
                elif char == "!":
                    self.regex += r"\d*"
                    self.score = self.score + 6  # Match single digit plus any more counts
                elif char == "X":
                    self.regex += r"\d"
                    self.score = self.score + 5  # match single digit
                elif char == r"[":
                    regex_range = char
                    while (char := next(pattern)) and char != r"]":
                        regex_range += char
                    regex_range += char
                    self.regex += regex_range
                    self.score = self.score + 8  # match Regex range
            self.regex += "$"

    def __init__(self, pattern: str = None):
        self.pattern = self.Pattern(pattern)

    def match(self, test_pattern: str, regex_pattern: str = None) -> int:
        if test_pattern[0] == r"+":
            test_pattern = f"\\{test_pattern}"
        if regex_pattern:
            return self.match_one(test_pattern, self.Pattern(regex_pattern))
        else:
            return self.match_one(test_pattern, self.pattern)

    @staticmethod
    def match_one(test_pattern: str, pattern: Pattern) -> int:
        test_pattern = str(test_pattern)
        if re.match(pattern.regex, test_pattern):
            return pattern.score
        else:
            return 0
