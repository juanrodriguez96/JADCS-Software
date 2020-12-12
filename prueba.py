x ={
    "camilo":[1,2,3,4],
    "pepe":[9,8,7,6]
}
print(x["camilo"])



lista=x["camilo"]
for i in range(len(lista)):
    if lista[i] == 2:
        del x["camilo"][i]


print(x)