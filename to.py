name="rohitamrutkar"
temp=" "
i=0
for i in range(len(name)):
        if name[i] not in temp:
            temp=name[i]
        print(f"{name[i]}={name.count(name[i])}")
        