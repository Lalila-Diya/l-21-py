code={
    "India":"+91",
    "Australia":"+61",
    "USA":"+1",
    "UK":"+44",
    "Germany":"+49",
    "Pakisthan":"+92",
    "China":"+86",
    "Japan":"+81",
    "France":"+33",
    "Bangladesh":"+880"
}
c=input("Enter any country: ")
print("Country code for: ",c)
print(code.get(c," not found "))

