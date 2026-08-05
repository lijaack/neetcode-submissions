class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        # Count how many of each character we need from t
        required_counts = {}

        for character in t:
            required_counts[character] = (
                required_counts.get(character, 0) + 1
            )

        # Count characters inside our current window
        window_counts = {}

        # Number of character requirements currently satisfied
        satisfied_requirements = 0

        # Number of different characters we need to satisfy
        total_requirements = len(required_counts)

        left = 0

        # Keep track of the smallest valid window we've found
        best_window_start = 0
        best_window_end = 0
        smallest_window_length = float("infinity")

        # Expand the window with the right pointer
        for right in range(len(s)):

            current_character = s[right]

            # Add the new character to the window
            window_counts[current_character] = (
                window_counts.get(current_character, 0) + 1
            )

            # Did adding this character completely satisfy
            # one of the requirements from t?
            if (
                current_character in required_counts
                and window_counts[current_character]
                == required_counts[current_character]
            ):
                satisfied_requirements += 1

            # Try shrinking the window while it remains valid
            while satisfied_requirements == total_requirements:

                current_window_length = right - left + 1

                # Is this the smallest valid window we've seen?
                if current_window_length < smallest_window_length:

                    best_window_start = left
                    best_window_end = right
                    smallest_window_length = current_window_length

                # Remove the leftmost character
                left_character = s[left]
                window_counts[left_character] -= 1

                # Did removing it make the window invalid?
                if (
                    left_character in required_counts
                    and window_counts[left_character]
                    < required_counts[left_character]
                ):
                    satisfied_requirements -= 1

                left += 1

        # Return the smallest valid window
        if smallest_window_length == float("infinity"):
            return ""

        return s[best_window_start : best_window_end + 1]