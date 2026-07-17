class Solution:
    def frequencySort(self, nums):

        # Building a frequency map
        hashmap = dict()
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        # Custom sort function:
        # Returns a tuple (-frequency, number).
        # Python sorts tuples in ascending order.
        # -frequency ensures numbers with higher frequency come first.
        # If two numbers have the same frequency, the smaller number comes first.

        def custom_sort(n):
            return (-hashmap[n], n)

        # Sorting the array using the custom key
        nums.sort(key=custom_sort)   # Note : Here we use key=custom_sort and not custom_sort() . We don't use () in key paramater just like we don't use () in Tkinter 'Button's  "command" parameter

        # Returning the sorted array
        return nums
