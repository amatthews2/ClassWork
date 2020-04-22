from flask import Flask, request, jsonify
import datetime
import logging

logging.basicConfig(filename="HR_log.txt", level=logging.DEBUG)

db = []

app = Flask(__name__)


def add_pat_to_db(ids, email, age):
    new_pat_test = {"patient_id": ids,
                    "attending_email": email,
                    "patient_age": age}
    db.append(new_pat_test)
    return True


def init_db():
    add_pat_to_db("919", "email@gmail.com", 23)
    add_pat_to_db("920", "email@gmail.com", 50)
    add_pat_to_db("921", "email@gmail.com", 2)


def verify_info(in_dict, expected_keys, expected_type):
    for i, key in enumerate(expected_keys):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 408
        if type(in_dict[key]) is not expected_type[i]:
            if in_dict[key].isdigit() is False:
                return "{} is wrong type".format(key), 400
            else:
                in_dict[key] = int(in_dict[key])
    return in_dict, True


def is_tachy(age, hr, patient_id, email):
    if 1 <= age <= 2 and hr > 151:
        logging.info(
            "Patient {} has a tachycardic HR of {}. Contacted {}".format(
                patient_id, hr, email))
        return "tachycardic"
    elif 3 <= age <= 4 and hr > 137:
        logging.info(
            "Patient {} has a tachycardic HR of {}. Contacted {}".format(
                patient_id, hr, email))
        return "tachycardic"
    elif 5 <= age <= 7 and hr > 133:
        logging.info(
            "Patient {} has a tachycardic HR of {}. Contacted {}".format(
                patient_id, hr, email))
        return "tachycardic"
    elif 8 <= age <= 11 and hr > 130:
        logging.info(
            "Patient {} has a tachycardic HR of {}. Contacted {}".format(
                patient_id, hr, email))
        return "tachycardic"
    elif 12 <= age <= 15 and hr > 119:
        logging.info(
            "Patient {} has a tachycardic HR of {}. Contacted {}".format(
                patient_id, hr, email))
        return "tachycardic"
    elif age > 15 and hr > 100:
        logging.info(
            "Patient {} has a tachycardic HR of {}. Contacted {}".format(
                patient_id, hr, email))
        return "tachycardic"
    else:
        return "not tachycardic"


@app.route("/", methods=["GET"])
def say():
    return "hi"


@app.route("/api/new_patient", methods=["POST"])
def add_patient():
    new_patient = request.get_json()
    expected_keys = ("patient_id", "attending_email", "patient_age")
    expected_type = (int, str, int)
    pat, valid = verify_info(new_patient, expected_keys, expected_type)
    if valid is not True:
        return pat, 400
    pat["heart_rate"] = []
    pat["status"] = []
    pat["timestamp"] = []
    db.append(pat)
    logging.info(
        "Patient {} has been added".format(jsonify(pat["patient_ID"])))
    return jsonify(pat["patient_ID"]), 200


@app.route("/api/heart_rate", methods=["POST"])
def import_HR():
    patient_HR = request.get_json()
    expected_keys = ("patient_id", "heart_rate")
    expected_type = (int, int)
    pat, valid = verify_info(patient_HR, expected_keys, expected_type)
    if valid is not True:
        return jsonify(pat), 400
    hr = find_pat_HR(pat)
    logging.info(
        "Patient {} heart rate {} has been added".format(
            jsonify(pat["patient_id"]),
            jsonify(hr)))
    return "Heart Rate added", 200


def find_pat_HR(pat):
    for i, item in enumerate(db):
        if item["patient_id"] == pat["patient_id"]:
            item["heart_rate"].append(pat["heart_rate"])
            item["status"].append(
                is_tachy(item["patient_age"], pat["heart_rate"],
                         pat["patient_id"], item["attending_email"]))
            item["timestamp"].append(datetime.datetime.now())
            return jsonify(pat["heart_rate"])
        elif i == (len(db) - 1):
            return error(500, "User does not exist.", "ValueError")


@app.route("/api/status/<patient_id>/", methods=["GET"])
def measurements(patient_id):
    for i, item in enumerate(db):
        if item["patient_id"] == patient_id:
            status_dict = {"heart_rate": item["heart_rate"][-1],
                           "status": item["status"][-1],
                           "timestamp": item["timestamp"][-1]}
            return jsonify(status_dict), 400
        elif i == (len(db) - 1):
            return error(500, "User does not exist.", "ValueError")


@app.route("/api/heart_rate/average/<patient_id>/", methods=["GET"])
def find_average(patient_id):
    for i, item in enumerate(db):
        if item["patient_id"] == patient_id:
            HR_list = item["heart_rate"]
            avgHR = average(HR_list)
            return jsonify(patient_id), jsonify(avgHR)
        elif i == (len(db) - 1):
            return error(500, "User does not exist.", "ValueError")


def average(list_heart):
    avgHR = sum(list_heart) / len(list_heart)
    return avgHR


@app.route("/api/heart_rate/interval_average/", methods=["POST"])
def import_int_avg():
    patient_int_avg = request.get_json()
    expected_keys = ("patient_id", "heart_rate_average_since")
    expected_type = (int, str)
    pat, valid = verify_info(patient_int_avg, expected_keys, expected_type)
    if valid is not True:
        return jsonify(pat), 400
    int_avg, valid = find_pat(pat)
    return jsonify(int_avg), 200


def find_pat(pat):
    for i, record in enumerate(db):
        if record["patient_id"] == pat["patient_id"]:
            input_time = datetime.strptime(pat["heart_rate_average_since"],
                                           '%Y-%m-%d %H:%M:%S.%f')
            int_avg = find_int_avg(input_time, record)
            return int_avg, True
        elif i == (len(db) - 1):
            return "No matching patient_id", 400


def find_int_avg(input_time, item):
    result = []
    stamps = []
    hr_list = []
    for j, timestamp in item["timestamp"]:
        if input_time >= timestamp:
            result.append(j)
            stamps.append(timestamp)
    for j, HR in item["heart_rate"]:
        for k in result:
            if j == k:
                hr_list.append(HR)
    int_avg = average(hr_list)
    return int_avg


def error(status_code, text, err_type):
    error_output = {
        "status_code": status_code,
        "reason": text,
        "error_type": err_type
    }
    return jsonify(error_output)


if __name__ == "__main__":
    init_db()
    app.run(debug=False)
