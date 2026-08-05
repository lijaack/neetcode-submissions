class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Stores the length of the consecutive sequence at each number's boundary
        sequence_lengths = defaultdict(int)

        # Keep track of the longest sequence found
        longest_length = 0

        for num in nums:

            # Only process numbers we haven't seen before
            if sequence_lengths[num] == 0:

                # Get the length of the sequence immediately to the left and right
                left_sequence_length = sequence_lengths[num - 1]
                right_sequence_length = sequence_lengths[num + 1]

                # The current number connects both sides + itself
                current_sequence_length = (
                    left_sequence_length + right_sequence_length + 1
                )

                # Store the length at the current number
                sequence_lengths[num] = current_sequence_length

                # Update the left boundary of the sequence
                sequence_lengths[num - left_sequence_length] = current_sequence_length

                # Update the right boundary of the sequence
                sequence_lengths[num + right_sequence_length] = current_sequence_length

                # Update the global maximum
                longest_length = max(longest_length, current_sequence_length)

        return longest_length        