import requests

# server_name = "vcm-14488.vm.duke.edu:5004"
server_name = "http://127.0.0.1:5000"


def add_some_pat():
    new_patient = {"patient_id": "1",
                   "attending_email": "r_user_id@yourdomain.com",
                   "patient_age": 50}
    r = requests.post(server_name + "/api/new_patient/",
                      json=new_patient)
    print(r.status_code)
    print(r.text)


def add_some_patient_HR():
    new_p = {"patient_id": "1", "heart_rate": "200"}
    req = requests.post(server_name + "/api/heart_rate/",
                        json=new_p)
    if req.status_code != 200:
        print("Error: {} - {}".format(req.status_code, req.text))
    else:
        print("success {}".format(req.text))


'''
    patient_data = {"patient_id": "1", "heart_rate": "100"}
    r2 = requests.post(server_name + "/api/heart_rate/",
                       json=patient_data)
    print(r2.status_code)
    print(r2.text)

    patient_data = {"patient_id": "919", "heart_rate": "90"}
    r2 = requests.post(server_name + "/api/heart_rate/",
                       json=patient_data)
    print(r2.status_code)
    print(r2.text)
'''

if __name__ == '__main__':
    add_some_pat()
    add_some_patient_HR()
