
# Diccionarios
# {"clave": "valor",}

teacher = {
    "name": "Francisco",
    "l_name": "Lopez",
    "phone": "2224858093",
    "groups": ["3BDSM"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3CDSM")
teacher["phone"] = "2471070644"
teacher["city"] = "Huamantla"
print(teacher)