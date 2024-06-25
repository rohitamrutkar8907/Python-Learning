list1=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
list2=sorted(list([i[1] for i in list1]))
print(list2)