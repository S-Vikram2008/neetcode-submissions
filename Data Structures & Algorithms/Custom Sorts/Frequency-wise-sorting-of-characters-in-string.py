# Custom sort function:

# Note :
'''
Returns a tuple (-frequency, character).
Python sorts tuples in ascending order.
-frequency ensures numbers with higher frequency come first.
 If two characters have the same frequency, then any character can be placed first. - No restrictions

'''

def custom_sort(n):
    return (-hashmap[n],n)

s='tree'

# Building a frequency map
hashmap=dict()
for i in s:
    if i not in hashmap:
        hashmap[i]=1
    else:
        hashmap[i]+=1

# Using custom sort using python default sort by using key parameter
new=sorted(s,key=custom_sort)

# Finally printing nums
print(''.join(new))
