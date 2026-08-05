class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest_window = 0

        # Try making the entire window one specific character
        for target_character in set(s):

            left_pointer = 0
            target_count = 0

            # Expand the window
            for right_pointer in range(len(s)):

                # Count how many target characters are in the window
                if s[right_pointer] == target_character:
                    target_count += 1

                # Number of characters we need to replace
                window_size = right_pointer - left_pointer + 1
                replacements_needed = window_size - target_count

                # Shrink the window if we need too many replacements
                while replacements_needed > k:

                    if s[left_pointer] == target_character:
                        target_count -= 1

                    left_pointer += 1

                    window_size = right_pointer - left_pointer + 1
                    replacements_needed = window_size - target_count

                # Current window is valid
                longest_window = max(longest_window, window_size)

        return longest_window