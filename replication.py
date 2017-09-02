# Copy your FrequentWords function (along with all required subroutines) from Replication.py
# You will need to copy FrequentWords, CountDict, and PatternCount
def FrequentWords(Text, k):
    FrequentPatterns = [] # output variable
    # your code here
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

def remove_duplicates(list):
  ItemsNoDuplicates = []
  for i in list:
    if i not in ItemsNoDuplicates:
      ItemsNoDuplicates.append(i)
  return ItemsNoDuplicates
      

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict
def CountDict(Text, k):
    Count = {} # output variable
    # your code here
    Count = {} 
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    # your code here
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Then, call your FrequentWords function, passing in "GATCCAGATCCCCATAC" for Text and 2 for k,
# and store the result as a variable named words.
words = FrequentWords('GATCCAGATCCCCATAC',2)



# Finally, print the words variable.
print (words)

import sys
lines = sys.stdin.read().splitlines()
print(' '.join(FrequentWords(lines[0],int(lines[1]))))
