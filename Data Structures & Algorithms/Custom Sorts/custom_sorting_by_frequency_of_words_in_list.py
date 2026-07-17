words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4

def custom_sort(word):
    return (-hashmap[word],word)

# Creating a hashmap and iterating over the list 'words' and storing its frequencies in hashmap
hashmap=dict()
for i in words:
    if i not in hashmap:
        hashmap[i]=1
    else:
        hashmap[i]+=1

# Here we sort the hashmap (dictionary) keys and then slice the first k values from the whole sorted list.
k_list=sorted(hashmap,key=custom_sort)[:k]

print(k_list)
