def myLPN(dob):
    DOB=str(dob)
    res=0
    while dob>9:
        dob=int('0')
        for char in DOB:
            char=int(char)
            dob+=char
        res = str(dob)
        DOB=str(dob)
    return res
print("ENTER YOUR DATE OF BIRTH IN(DD/MM/YYY)FORMAT:") # enter 1/02/1987 as 1021987
dob=int(input().split('-'))
fn=myLPN(dob)
print("your life path number is:",fn)

# THE PROCESS GOES IN THE FOLLOWING WAY:
  # THE BDAY DATE IS 1-9-1997
   #IT ADDS ALL THE NUMBERS AS 1+9+1+9+9+7= 36 AND THIS 36 ADDS AS 3+6= 9 AND THIS IS FINAL ANSWER

if fn=='1':
    print("you are independent")
elif fn=='2':
    print("you are introvert")
elif fn=='3':
    print("you are helpful")
elif fn=='4':
    print("you are practical")
elif fn=='5':
    print("you are extrovert")
elif fn=='6':
    print("you are responsible")
elif fn=='7':
    print("you are pious")
elif fn=='8':
    print("you are ambitious")
elif fn=='9':
    print("you are leader")
else:
    print("eyes muskoni kaadu ra eyes terchukoni type ")





