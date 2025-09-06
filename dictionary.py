#Dictionary DS

yash = {"name" : "yash" , "class" : 3 , "maths" : 34 , "english" : 45}
print(yash["name"])

song = {"name" : "Hello" , "Lyrics" : "Lata" , "year" : 2005 , "genre" : "workout" , }

yash.pop("maths")
print(yash)

yash.update({"name" : "O mere dil k chain "})
print(yash)

yash["name"] = "High Heels"
print(yash)

print(yash.values())

print(yash.keys())

print(yash.items())

print(yash.get("name"))

yash1 = yash
yash1["name"] = "Mercy"
print(yash["name"])

yash2 = yash.copy()
print(yash2)
yash2["name"] = "Sirra"
print(yash["name"])

yash.setdefault("name" ,98)
print(yash)

for key in yash:
    print(key , " " , yash[key])