# def rpn_calculate(expr):
#     split_expr=expr.split(' ')
#     if len(split_expr)==1:
#         return int(split_expr[0])
#     operator=split_expr[2]
#     if operator=='-':
#         return int(split_expr[0])-int(split_expr[1])
#     if operator=='+':
#         return int(split_expr[0])+int(split_expr[1])
import math  


def rpn_calculate(expr):
    ops = {'+','-','*','/','SQRT'}
    split_expr=expr.split(' ') 
    if len(split_expr)==1:
        return int(split_expr[0])
    st=[]
    num=int(split_expr[0])
    st.append(num)
    for tk in split_expr[1:]:
      #print(st)
      if tk in ops:
        #print("if",tk)
        if tk == '+':
            y,x = st.pop(),st.pop()
            z=x+y    
        if tk == '-':
            y,x = st.pop(),st.pop()
            z=x-y   
        if tk == '/':
            y,x = st.pop(),st.pop()
            z=x/y   
        if tk == '*':
            y,x = st.pop(),st.pop()
            z=x*y
        if tk == 'SQRT':
            y=st.pop()
            z=math.sqrt(y)
      else:
        #print("else",tk)
        z = int(tk)
      st.append(z)
    return z

#print(rpn_calculate("4 8 +"))
# print(rpn_calculate("3 20 4 6 + / *"))#6
# print(rpn_calculate('20 4 /'))#5
# print(rpn_calculate('4 2 + 3 -'))#3
# print(rpn_calculate('3 5 8 * 7 + *'))#141
# print(rpn_calculate('9 SQRT'))
# print(rpn_calculate('169 SQRT'))