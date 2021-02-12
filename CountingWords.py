intro=input("Write About yourself: ")
print(intro)


characterCount=0
wordCount=1
for i in intro:
    characterCount=characterCount+1
    
    if(i==' '):
        wordCount=wordCount+1
print("number Of characters in your introduction are : ")
print(characterCount)
print("number Of words in your introduction are : ")
print(wordCount)
