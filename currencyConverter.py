with open('currencyData.txt') as f:
    lines=f.readlines()

currencyDict={}
for line in lines :
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]

amount=int(input("Enter the amount:\t"))
print("Choose the currency name you want from the options available below:\n")
# print(currencyDict.keys)
[print(item) for item in currencyDict.keys()]

Convert_from=input("Enter the currency you want your amount to get converted from: ")
Convert_to=input("Enter the currency you want your amount to converted to: ")

print(f"{amount} {Convert_from} = {amount*(float(currencyDict[Convert_to]))/(float(currencyDict[Convert_from]))} {Convert_to}")
