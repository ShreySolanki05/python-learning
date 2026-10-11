python_class = {"Asha", "Ravi", "Meera", "Kabir"}
sql_class = {"Meera", "Kabir", "Tara", "Dev"}
both = (python_class &  sql_class)
either = (python_class | sql_class)
only_python = (python_class - sql_class)
exactly_one = (python_class ^ sql_class)

print(f"In both classes : {sorted(both)}")
print(f"In either of the classes : {sorted(either)}")
print(f"Only in python class : {sorted(only_python)}")
print(f"In exactly one of the classes : {sorted(exactly_one)}")

