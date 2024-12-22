def matchwords(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)
    print("The list of all the words which had their last and first letter the same",lst)
    return ctr
count = matchwords(['abc','cccc','dad','dog','madam','racecar'])
print("Number of words having their first and last letters the same",count)