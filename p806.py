class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_width = 0
        line_count = 0

        for c in s:
            char_width = widths[ord(c) - ord('a')]
            total_width += char_width

            if total_width > 100:
                line_count += 1
                total_width = char_width

        return [line_count + 1, total_width]
