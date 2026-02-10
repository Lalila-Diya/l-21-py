test_dict={'Codingal':2,'is':10,'best':2,'for':2,'coding':1}
print("The original dictionary: "+str(test_dict))
k=int(input("Enter the frequency number: "))
res=0
for key in test_dict:
    if test_dict[key]==k:
        res=res+1
print("Frequency is: "+str(res))