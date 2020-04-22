import requests


m = requests.get("http://vcm-7631.vm.duke.edu:5000/regions")
print(m.json())
# can do get request directly in the browser but has to put the port (because it not 80
# cannot do a post request in the browser

request_json = {"one": "Spain", "two": "Canada"}
r = requests.post("http://vcm-7631.vm.duke.edu:5000/compare",
                  json=request_json)
print(r.text)
print(r.status_code)
if r.status_code == 200:
    print(r.json())
else
    print("there is an error with the status code of {}".format(r.status_code))