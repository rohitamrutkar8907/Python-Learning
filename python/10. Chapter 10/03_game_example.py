
def getSecondMostFreq(str) :

 NO_OF_CHARS = 256

 count = [0] * NO_OF_CHARS


 for i in range(len(str)) :
  count[ord(str[i])] += 1

 first, second = 0, 0


 for i in range(NO_OF_CHARS) :


  if count[i] > count[first] :

   second = first
   first = i

 
  elif (count[i] > count[second] and
   count[i] != count[first] ) :
   
   second = i

 
 return chr(second)



str = input()
 
if(len(str)>100):
    print("invalid")
    
res = getSecondMostFreq(str)
if res != '\0' :
  print("Second most frequent char is", res)
else :
  print("No second most frequent character")