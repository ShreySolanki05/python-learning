import json
def load_expenses(filename):
    try :
        with open(filename,"r") as f:
            a = json.load(f)
            return a
    except FileNotFoundError:
        return []
def save_expenses(filename, data):
    with open(filename,"w") as f:
        json.dump(data,f)
   

f = load_expenses("expenses.json")
print(f)
c = {"item": "coffee", "amount": 150}
f.append(c)
save_expenses("expenses.json",f)
d = load_expenses("expenses.json")
print(d)
