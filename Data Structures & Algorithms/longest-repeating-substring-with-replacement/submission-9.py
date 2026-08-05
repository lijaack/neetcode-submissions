class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_length = 0
        # Counts of each character inside the current window
        character_counts = {}
        left = 0
        # Highest frequency character count in the current window
        highest_frequency = 0
        # Expand the window with the right pointer
        for right in range(len(s)):
            current_character = s[right]
            # Add current character to the window
            character_counts[current_character] = (character_counts.get(current_character, 0) + 1)
            
            # Update the most common character count in this window
            highest_frequency = max(highest_frequency,character_counts[current_character])

            window_length = right - left + 1
            # Characters that need replacing = everything except the most common character
            replacements_needed = window_length - highest_frequency

            # Shrink window if we need too many replacements
            while replacements_needed > k:

                left_character = s[left]

                character_counts[left_character] -= 1
                left += 1

                window_length = right - left + 1
                replacements_needed = window_length - highest_frequency

            # Current window is valid
            longest_length = max(longest_length, window_length)

        return longest_length
        