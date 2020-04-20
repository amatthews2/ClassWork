import requests

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(type(r))
print(r)
print(r.text)
#given in json format, change it with below
answer = r.json()
print(type(answer)) #converts to a list
print(answer)

## for loop to break apart
for branch in answer:
    print("Name of branch is {}".format(branch["name"]))
