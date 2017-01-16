ask = input("Enter your expression: ")
#Тут я маю перетворити ask в float 
def variables(s):
    chrList = ['(',')','+','-','*','/','0','1','2','3','4','5','6','7','8','9']
    if s in chrList:
        return True
    else:
        return False
def jisuan(n1,n2,o):
    if o=='+':
        return n1+n2
    elif o=='-':
        return n1-n2
    elif o=='*':
        return n1*n2
    elif o=='/':
        return n1/n2
