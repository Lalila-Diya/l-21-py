student={
    "id1":{"name":"Diya","class":"VII","age":"12"},
    "id2":{"name":"Riya","class":"VIII","age":"13"},
    "id3":{"name":"Diya","class":"VII","age":"12"},
    "id4":{"name":"Miya","class":"X","age":"15"}
}
result={}
for key,value in student.items():
    if value not in result.values():
        result[key]=value
print(result)