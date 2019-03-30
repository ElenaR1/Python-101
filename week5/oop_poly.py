import re

class Polynomial:
    def __init__(self,expr):
        self.expr=expr

    def read_expr(self):
        if self.expr[0]=='-':
            self.expr=self.expr[1:]
        terms = self.expr.replace('-','+').split('+')
        #print(re.split('+ |- ',self.expr))
        print(terms)
        equation = [re.split('x\^?', t) for t in terms]
        print('equation',equation)
        eq_map = []
        for e in equation:
            try:
                coeff = int(e[0])
            except ValueError:
                coeff = 1
            try:
                power = int(e[1])
            except ValueError:
                #print('ValueError',e[1])
                power = 1#if it is only x without power
            except IndexError:# if it is only one element in the list - it is not multiplyed by x
                power = 0
            eq_map.append((coeff, power))
        return eq_map

class Derivative:
    def __init__(self,lst,expr):
        self.lst=lst
        self.expr=expr

    def eval_derivative(self):
        #print('len',len(self.lst))
        if len(self.lst)==1:
            if self.lst[0][1]==0:
                return 0
            elif self.lst[0][1]==1:
                return self.lst[0][0]

        coeff=self.lst[0][0]*self.lst[0][1]
        xpow=self.lst[0][1]-1
        #print(coeff,xpow)
        if xpow==1:
            res=str(coeff)+'*x'
        elif xpow==0:
            res='+'+str(coeff)
        elif xpow==-1:
            res='' 
        else:
            #res=''
            res=str(coeff)+'*x'+'^'+str(self.lst[0][1]-1)
        for i in range(1,len(self.lst)):
            #print(self.lst[i],self.lst[i][0],self.lst[i][1])
            coeff=self.lst[i][0]*self.lst[i][1]
            xpow=self.lst[i][1]-1
            #print(str(self.lst[i][0]))
            #print(coeff,xpow)
            if xpow==1:
                res+='+'+str(coeff)+'*x'
                continue
            elif xpow==0:
                res+='+'+str(coeff)
                continue
            elif xpow==-1:
                continue
            else:
                res+='+'+str(coeff)+'*x'+'^'+str(xpow)
        return res
def main():

    eq="2x^2+3x+1"
    poly=Polynomial(eq)
    l=poly.read_expr()
    print(eq,'->',l)

    deriv=Derivative(l,eq)
    print(eq,'->',deriv.eval_derivative())

    print('===============')
    eq2="x^3+2x^2+1"
    poly2=Polynomial(eq2)
    l2=poly2.read_expr()
    print(eq2,'->',l2)

    deriv2=Derivative(l2,eq2)
    print(eq2,'->',deriv2.eval_derivative())

    print('===============')
    eq3='x^2+1'
    poly3=Polynomial(eq3)
    l3=poly3.read_expr()
    print(eq3,'->',l3)

    deriv3=Derivative(l3,eq3)
    print(eq3,'->',deriv3.eval_derivative())

    print('===============')
    eq4='x^4+10x^3'
    poly4=Polynomial(eq4)
    l4=poly4.read_expr()
    print(eq4,'->',l4)

    deriv4=Derivative(l4,eq4)
    print(eq4,'->',deriv4.eval_derivative())

    print('===============')
    eq5='1'
    poly5=Polynomial(eq5)
    l5=poly5.read_expr()
    print(eq5,'->',l5)

    deriv5=Derivative(l5,eq5)
    print(eq5,'->',deriv5.eval_derivative())

    print('===============')
    eq6='x'
    poly6=Polynomial(eq6)
    l6=poly6.read_expr()
    print(eq6,'->',l6)

    deriv6=Derivative(l6,eq6)
    print(eq6,'->',deriv6.eval_derivative())

    print('===============')
    eq7='2x'
    poly7=Polynomial(eq7)
    l7=poly7.read_expr()
    print(eq7,'->',l7)

    deriv7=Derivative(l7,eq7)
    print(eq7,'->',deriv7.eval_derivative())

    print('===============')
    eq8='5x^2+2x^4-9' #'-2x+5x^3-9'
    poly8=Polynomial(eq8)
    l8=poly8.read_expr()
    print(eq8,'->',l8)

    deriv8=Derivative(l8,eq8)
    print(eq8,'->',deriv8.eval_derivative())



if __name__=='__main__':
    main()import re

class Polynomial:
    def __init__(self,expr):
        self.expr=expr

    def read_expr(self):
        if self.expr[0]=='-':
            self.expr=self.expr[1:]
        terms = self.expr.replace('-','+').split('+')
        #print(re.split('+ |- ',self.expr))
        print(terms)
        equation = [re.split('x\^?', t) for t in terms]
        print('equation',equation)
        eq_map = []
        for e in equation:
            try:
                coeff = int(e[0])
            except ValueError:
                coeff = 1
            try:
                power = int(e[1])
            except ValueError:
                #print('ValueError',e[1])
                power = 1#if it is only x without power
            except IndexError:# if it is only one element in the list - it is not multiplyed by x
                power = 0
            eq_map.append((coeff, power))
        return eq_map

class Derivative:
    def __init__(self,lst,expr):
        self.lst=lst
        self.expr=expr

    def eval_derivative(self):
        #print('len',len(self.lst))
        if len(self.lst)==1:
            if self.lst[0][1]==0:
                return 0
            elif self.lst[0][1]==1:
                return self.lst[0][0]

        coeff=self.lst[0][0]*self.lst[0][1]
        xpow=self.lst[0][1]-1
        #print(coeff,xpow)
        if xpow==1:
            res=str(coeff)+'*x'
        elif xpow==0:
            res='+'+str(coeff)
        elif xpow==-1:
            res='' 
        else:
            #res=''
            res=str(coeff)+'*x'+'^'+str(self.lst[0][1]-1)
        for i in range(1,len(self.lst)):
            #print(self.lst[i],self.lst[i][0],self.lst[i][1])
            coeff=self.lst[i][0]*self.lst[i][1]
            xpow=self.lst[i][1]-1
            #print(str(self.lst[i][0]))
            #print(coeff,xpow)
            if xpow==1:
                res+='+'+str(coeff)+'*x'
                continue
            elif xpow==0:
                res+='+'+str(coeff)
                continue
            elif xpow==-1:
                continue
            else:
                res+='+'+str(coeff)+'*x'+'^'+str(xpow)
        return res
def main():

    eq="2x^2+3x+1"
    poly=Polynomial(eq)
    l=poly.read_expr()
    print(eq,'->',l)

    deriv=Derivative(l,eq)
    print(eq,'->',deriv.eval_derivative())

    print('===============')
    eq2="x^3+2x^2+1"
    poly2=Polynomial(eq2)
    l2=poly2.read_expr()
    print(eq2,'->',l2)

    deriv2=Derivative(l2,eq2)
    print(eq2,'->',deriv2.eval_derivative())

    print('===============')
    eq3='x^2+1'
    poly3=Polynomial(eq3)
    l3=poly3.read_expr()
    print(eq3,'->',l3)

    deriv3=Derivative(l3,eq3)
    print(eq3,'->',deriv3.eval_derivative())

    print('===============')
    eq4='x^4+10x^3'
    poly4=Polynomial(eq4)
    l4=poly4.read_expr()
    print(eq4,'->',l4)

    deriv4=Derivative(l4,eq4)
    print(eq4,'->',deriv4.eval_derivative())

    print('===============')
    eq5='1'
    poly5=Polynomial(eq5)
    l5=poly5.read_expr()
    print(eq5,'->',l5)

    deriv5=Derivative(l5,eq5)
    print(eq5,'->',deriv5.eval_derivative())

    print('===============')
    eq6='x'
    poly6=Polynomial(eq6)
    l6=poly6.read_expr()
    print(eq6,'->',l6)

    deriv6=Derivative(l6,eq6)
    print(eq6,'->',deriv6.eval_derivative())

    print('===============')
    eq7='2x'
    poly7=Polynomial(eq7)
    l7=poly7.read_expr()
    print(eq7,'->',l7)

    deriv7=Derivative(l7,eq7)
    print(eq7,'->',deriv7.eval_derivative())

    print('===============')
    eq8='5x^2+2x^4-9' #'-2x+5x^3-9'
    poly8=Polynomial(eq8)
    l8=poly8.read_expr()
    print(eq8,'->',l8)

    deriv8=Derivative(l8,eq8)
    print(eq8,'->',deriv8.eval_derivative())



if __name__=='__main__':
    main()oop
