def describe_person(name, age=30):
    return F'Имя:{name} Возраст:{age}'
print(describe_person('Nikolay', 21))