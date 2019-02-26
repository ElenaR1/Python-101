print("Hello World")#function
print(min(1,0,10,-9))
d={
	'key1':1,
	'key2':2.5
}
print(d['key2'])
xs=[1,2,3,4]
for x in xs:
	x=5
	print(x)

print(xs)
print("------")

xss=[1,2,3]
for x in xss:
	xss[0]=x
	print(x,xss)
#That's what we get 1 [1, 2, 3]
# 2 [2, 2, 3]
# 3 [3, 2, 3]

print("-----")
for x in xss:
    xss=[3,5,1] # = []
    print(x,xss)
#     3 [3, 5, 1] t.k kato gleda poslednata promqna ot gorniq cikul. Tam masivut veche e [3,2,3]
# 2 [3, 5, 1]
# 3 [3, 5, 1]


xs2=[1,2,3]
print("-----")
for x in xs2:
	xs2=[3,5,1] # = []
	print(x,xs2)
# 1 [3, 5, 1]
# 2 [3, 5, 1]
# 3 [3, 5, 1]


dict={
	'a':1,
	'b':2,
	'jackpot':40
}
for key in dict:
	print(key,dict[key])

for key in dict:
	if(key=='jackpot'):
		value=dict[key]

		if value%2==0:
			print("you win")


def dict_key(key,d): #function
	for d_key in d:
		if d_key==key:
			return True

	return False


print(dict_key('a',dict))
#print "hello" only in python2
#f(arg1,arg2,...,argn)

print('a' in dict)
print(3 in [1,2,3])
print(2 in[1,0,3] and 3 in [1,2,3])#False


def f():
	a=10

	def g():
		#global a
		a=20

	g()
	print(a)

f()#10

n=0
while True:
	print('looping')
	n+=1

	if n>5:
		break

for x in [1,2,3]:
	for y in [4,5,6]:
		flag=True
		break
	if flag:
		break
print(x)


numbers = []

for x in range(2, 5):
    numbers.append(x)

print(numbers)#[2, 3, 4]
# or numbers = [x for x in range(2,5)]

squares=[x**2 for x in range(2,5)]
print(squares)#[4, 9, 16]

def sum(a, b):
    return a + b
print(sum(10,20))

def all_in(xs,ys):
    for x in xs:
        if x not in ys:
            return False
    return True

print ("All in? ",all_in([1,2,3],[1,0,5,3]))

def p():
    pass

print(p()) # None

def ff():
    #a=25
    print(a)

a=15
ff()# with a=25 is 25 without iy is 15

