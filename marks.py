class main:
    def method(self):
	name=raw_input("enter name")
	l=[]
	print "enter marks"
	for i in range(6):
	    a=int(raw_input(">"))
	    l.append(a)
	avg=sum(l)/6
	print "name of student is: ",name
	print "total marks: ",sum(l)
	print "average of: ",avg

a=main()
no_students=int(raw_input("enter no of stuents"))
for n in range(no_students):
    a.method()
