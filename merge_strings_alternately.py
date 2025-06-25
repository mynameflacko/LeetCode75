# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
    result: str = ""
    
    len_1 = len(word1)
    len_2 = len(word2)
    
    if len_1 == len_2:
        for i in range(len_1):
            result += word1[i] + word2[i]
    elif len_1 < len_2:
        for i in range(len_1):
            result += word1[i] + word2[i]
        result += word2[len_1:len_2]
    else:
        for i in range(len_2):
            result += word1[i] + word2[i]
        result += word1[len_2:len_1]
        
    return result
                


print(mergeAlternately("abcd", "pq"))
