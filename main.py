from collections import defaultdict
def group_anagrams(strs):
  groups = defaultdict(list)
  for word in strs: # O(N)
    # s_word = str(sorted(word)) # O(M log M), make this O(M)
    # make a string to represent sorted(word)
    # use ascii 
    chars = [0] * 26
    for c in word:
      char_idx = ord(c) - ord("a")
      chars[char_idx] +=1

    key = ""
    for c in chars:
      key += str(c)
    #print(key)
    groups[key].append(word)
  #print(groups)

  return list(groups.values())

words = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(words))