import random
print("comp:Snake (S ),Water(W) or gun(G)?")
ranOM=random.randint(1,3)
if ranOM==1:
    comp='S'
elif ranOM==2:
    comp='W'
elif ranOM==3:
    comp='G'
print(ranOM)
# print(ranOM)
# S="snake"
# W="Water"
# G="Gun"
# comp=int (input("Snake (S ),Water(W) or gun(G)? : "))
user = input("User:Snake (S ),Water(W) or gun(G)? : ")
def game(comp,user):
    if comp==user:
        return None
    elif comp=='S':
        if user=='W':
            return False
        elif user=='G':
            return True
    elif comp=='W':
        if user=='G':
            return False
        elif user=='S':
            return True
    elif comp=='G':
        if user=='S':
            return False
        elif user=='W':
            return True
c=game(comp,user)
if c==None:
    print("Game is a tie")
elif c:
    print("User win")
else:
    print("User lose")
    