def decor(fun):
    def insdide(marks):
        for i in marks:
            if i>75:
                print("distinston")
        fun(marks)
    return insdide

@decor
def markcheck(marks):
        for i in marks:
            if i>35:
                print("pass")
                break
            else:
                print("fail")
                break
markcheck([34,75,65,85,45])
