from dataclasses import replace
from subprocess import _TXT


a="hello ,world !"
txt ="hello" in a
print("testing")
myvariable ="abc {}"
myvariable1=4
# printing
print(type(myvariable))
print(myvariable)
print(a[1])
print(a[1:3])
print(len(a))
print(a.upper())
print(txt)
print(myvariable.format(myvariable1))

#reversing
txt="hello"[::-1]
print(txt)

#casting
txt1="123"
typec = int(txt1)
print(type(typec))

#check presenvce
i=3
y=[2,3,4]
print(i in y)

#input a number
b= input("enter number:")
print("number is"+b)
