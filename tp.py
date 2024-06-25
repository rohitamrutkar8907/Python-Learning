"""listw=[]
n=int(input())
for i in range(0,n):
    ele=input()
    listw.append(ele)
print(listw)
diction={}

n=int(input())
my_dict = {}
for i in range (n):
  key=input("Enter key :")
  value=len(key)
  my_dict.update({key: value})
print(my_dict) 

N=int(input())
if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
    
if __name__ == '__main__':
    list1=[]
    n = int(input())
    for i in range(0,n):
        ele=input()
        list1.append(ele)
    list1.sort()
    print(list1[-2])
    """
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())