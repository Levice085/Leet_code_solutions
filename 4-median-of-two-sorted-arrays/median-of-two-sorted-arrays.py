class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        left = 0
        right = len(nums1)

        while left <= right:
            part_1 = (right + left) // 2
            part_2 = half_len - part_1

            max_left1 = float("-inf") if part_1 == 0 else nums1[part_1 - 1]
            min_right1 = float("inf") if part_1 == len(nums1) else nums1[part_1]
            max_left2 = float("-inf") if part_2 == 0 else nums2[part_2 - 1]
            min_right2 = float("inf") if part_2 == len(nums2) else nums2[part_2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total_len % 2 == 0:
                    median = (
                        max(max_left1, max_left2) + min(min_right1, min_right2)
                    ) / 2
                else:
                    median = min(min_right1, min_right2)
                return median
            elif max_left1 > min_right2:
                right = part_1 - 1
            else:
                left = part_1 + 1
