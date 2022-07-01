
def zad1(x,y):
    x1= x.split('-')
    y1= y.split('-')
    x2=''
    y2=''
    start =x2.join(x1)
    end =y2.join(y1)
    for i in range(int(start), int(end)):
        j = str(i)
        s= j[:2]+"-"+j[1:]
        print(s)

#zad1("79-900", "80-155")

x= [1,2,3,4,5,10]
y= [2,3,5,10,11]
def zad2(x,y):
    print(set(x).difference(y))

#zad2([1,2,3,4,5,10],[2,3,5,10,11])

