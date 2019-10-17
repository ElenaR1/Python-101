import math
def areParanthesisBalanced(expr):
    s=[]
    n=len(expr)
    for i in range(n):
        if expr[i]=='(' or expr[i]=='[' or expr[i]=='{':
            s.append(expr[i])
            continue
        if len(s)==0: # pri tozi sluchai : expr = "{()}]";  
            print('ccc')
            return False
        if expr[i]==')':
            x=s.pop()
            if x=='[' or x=='{':
                return False
        elif expr[i]==']':
            x=s.pop()
            if x=='(' or x=='{':
                return False
        elif expr[i]=='}':
            x=s.pop()
            if x=='(' or x=='[':
                return False
    if len(s)==0:
        return True
    else:#pri tozi sluchai expr = "{()}[";  
        print('ddd')
        return False



def main():

     expr = "{()}[[]]";  
  
     if (areParanthesisBalanced(expr)) : 
        print("Balanced");  
     else : 
        print("Not Balanced");  

    
  

if __name__=='__main__':
    main()
