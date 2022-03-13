strng = input('enter the string')
count = 0
wordcount = 1
for i in strng:
    count = count+1
    if(i==' '):
           wordcount = wordcount+1
print('number of word in the string')
print(wordcount)
print('number of character in the string')
print(count)