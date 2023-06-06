from application.models import Entry
import datetime as datetime
import pytest
from flask import json

# Unexpected Failure Testing


@pytest.mark.parametrize("predictionList", [
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]
])
# 3: Write the test function pass in the arguments
def test_EntryClass(predictionList, capsys):
    with capsys.disabled():
        print(predictionList)
        now = datetime.datetime.utcnow()
        new_entry = Entry(
            cough=predictionList[0],
            muscle_aches=predictionList[1],
            tiredness=predictionList[2],
            sore_throat=predictionList[3],
            runny_nose=predictionList[4],
            stuffy_nose=predictionList[5],
            fever=predictionList[6],
            nausea=predictionList[7],
            vomiting=predictionList[8],
            diarrhea=predictionList[9],
            shortness_of_breath=predictionList[10],
            difficulty_breathing=predictionList[11],
            loss_of_taste=predictionList[12],
            loss_of_smell=predictionList[13],
            itchy_nose=predictionList[14],
            itchy_eyes=predictionList[15],
            itchy_mouth=predictionList[16],
            itchy_inner_ear=predictionList[17],
            sneezing=predictionList[18],
            pink_eye=predictionList[19],
            prediction=predictionList[20],
            predicted_on=now)
        assert new_entry.cough == predictionList[0]
        assert new_entry.muscle_aches == predictionList[1]
        assert new_entry.tiredness == predictionList[2]
        assert new_entry.sore_throat == predictionList[3]
        assert new_entry.runny_nose == predictionList[4]
        assert new_entry.stuffy_nose == predictionList[5]
        assert new_entry.fever == predictionList[6]
        assert new_entry.nausea == predictionList[7]
        assert new_entry.vomiting == predictionList[8]
        assert new_entry.diarrhea == predictionList[9]
        assert new_entry.shortness_of_breath == predictionList[10]
        assert new_entry.difficulty_breathing == predictionList[11]
        assert new_entry.loss_of_taste == predictionList[12]
        assert new_entry.loss_of_smell == predictionList[13]
        assert new_entry.itchy_nose == predictionList[14]
        assert new_entry.itchy_eyes == predictionList[15]
        assert new_entry.itchy_mouth == predictionList[16]
        assert new_entry.itchy_inner_ear == predictionList[17]
        assert new_entry.sneezing == predictionList[18]
        assert new_entry.pink_eye == predictionList[19]
        assert new_entry.prediction == predictionList[20]
        assert new_entry.predicted_on == now

# Expected Failure Testing
# What happens if output prediction is negative
# What happens if input contains values outside of 0 and 1 like negative or > 1


@pytest.mark.xfail(reason="arguments <= 0")
@pytest.mark.parametrize("predictionList", [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, -1],
    [-1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, -1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, -1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, -1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, -1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 2],
    [2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 2],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
])
def test_EntryValidation(predictionList, capsys):
    test_EntryClass(predictionList, capsys)

# Test Add API


@pytest.mark.parametrize("predictionList", [
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]])
def test_addAPI(client, predictionList, capsys):
    with capsys.disabled():
        # prepare the data into a dictionary
        predictData = {
            "cough": predictionList[0],
            "muscle_aches": predictionList[1],
            "tiredness": predictionList[2],
            "sore_throat": predictionList[3],
            "runny_nose": predictionList[4],
            "stuffy_nose": predictionList[5],
            "fever": predictionList[6],
            "nausea": predictionList[7],
            "vomiting": predictionList[8],
            "diarrhea": predictionList[9],
            "shortness_of_breath": predictionList[10],
            "difficulty_breathing": predictionList[11],
            "loss_of_taste": predictionList[12],
            "loss_of_smell": predictionList[13],
            "itchy_nose": predictionList[14],
            "itchy_eyes": predictionList[15],
            "itchy_mouth": predictionList[16],
            "itchy_inner_ear": predictionList[17],
            "sneezing": predictionList[18],
            "pink_eye": predictionList[19],
            "prediction": predictionList[20],
            "user": predictionList[-1]
        }
    response = client.post('/api/add',
                           data=json.dumps(predictData),
                           content_type="application/json",)
    # check the outcome of the action
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_body = json.loads(response.get_data(as_text=True))
    assert response_body["id"]

# Test get API


@pytest.mark.parametrize("predictionList", [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 10],
])
def test_getAPI(client, predictionList, capsys):
    with capsys.disabled():
        response = client.get(f'/api/get/{predictionList[-1]}')
        ret = json.loads(response.get_data(as_text=True))
        # check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["id"] == predictionList[-1]
        assert response_body["cough"] == predictionList[0]
        assert response_body["muscle_aches"] == predictionList[1]
        assert response_body["tiredness"] == predictionList[2]
        assert response_body["sore_throat"] == predictionList[3]
        assert response_body["runny_nose"] == predictionList[4]
        assert response_body["stuffy_nose"] == predictionList[5]
        assert response_body["fever"] == predictionList[6]
        assert response_body["nausea"] == predictionList[7]
        assert response_body["vomiting"] == predictionList[8]
        assert response_body["diarrhea"] == predictionList[9]
        assert response_body["shortness_of_breath"] == predictionList[10]
        assert response_body["difficulty_breathing"] == predictionList[11]
        assert response_body["loss_of_taste"] == predictionList[12]
        assert response_body["loss_of_smell"] == predictionList[13]
        assert response_body["itchy_nose"] == predictionList[14]
        assert response_body["itchy_eyes"] == predictionList[15]
        assert response_body["itchy_mouth"] == predictionList[16]
        assert response_body["itchy_inner_ear"] == predictionList[17]
        assert response_body["sneezing"] == predictionList[18]
        assert response_body["pink_eye"] == predictionList[19]
        assert response_body["prediction"] == predictionList[20]

# Test delete API


@pytest.mark.parametrize("predictionList", [
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]
])
def test_deleteAPI(client, predictionList, capsys):
    with capsys.disabled():
        predictData = {
            "cough": predictionList[0],
            "muscle_aches": predictionList[1],
            "tiredness": predictionList[2],
            "sore_throat": predictionList[3],
            "runny_nose": predictionList[4],
            "stuffy_nose": predictionList[5],
            "fever": predictionList[6],
            "nausea": predictionList[7],
            "vomiting": predictionList[8],
            "diarrhea": predictionList[9],
            "shortness_of_breath": predictionList[10],
            "difficulty_breathing": predictionList[11],
            "loss_of_taste": predictionList[12],
            "loss_of_smell": predictionList[13],
            "itchy_nose": predictionList[14],
            "itchy_eyes": predictionList[15],
            "itchy_mouth": predictionList[16],
            "itchy_inner_ear": predictionList[17],
            "sneezing": predictionList[18],
            "pink_eye": predictionList[19],
            "prediction": predictionList[20],
            "user": predictionList[-1]
        }
        response = client.post(
            '/api/add', data=json.dumps(predictData), content_type="application/json",)
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["id"]
        id = response_body["id"]
        response2 = client.get(f'/api/delete/{id}')
        ret = json.loads(response2.get_data(as_text=True))

        # check the outcome of the action
        assert response2.status_code == 200
        assert response2.headers["Content-Type"] == "application/json"
        response2_body = json.loads(response2.get_data(as_text=True))
        assert response2_body["result"] == "ok"

# Consistency Test
# Test Predict API


@pytest.mark.parametrize("bigPredictionList", [
    [[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1], ],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ],
    [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], ]
])
def test_predictAPI(client, bigPredictionList, capsys):
    predictOutput = []
    for predictionList in bigPredictionList:
        with capsys.disabled():
            # prepare the data into a dictionary
            predictData = {
                "cough": predictionList[0],
                "muscle_aches": predictionList[1],
                "tiredness": predictionList[2],
                "sore_throat": predictionList[3],
                "runny_nose": predictionList[4],
                "stuffy_nose": predictionList[5],
                "fever": predictionList[6],
                "nausea": predictionList[7],
                "vomiting": predictionList[8],
                "diarrhea": predictionList[9],
                "shortness_of_breath": predictionList[10],
                "difficulty_breathing": predictionList[11],
                "loss_of_taste": predictionList[12],
                "loss_of_smell": predictionList[13],
                "itchy_nose": predictionList[14],
                "itchy_eyes": predictionList[15],
                "itchy_mouth": predictionList[16],
                "itchy_inner_ear": predictionList[17],
                "sneezing": predictionList[18],
                "pink_eye": predictionList[19],
                "id": predictionList[-1]  # User ID
            }
        response = client.post('/api/predict',
                               data=json.dumps(predictData),
                               content_type="application/json",)
        # check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["id"]
        predictOutput.append(response_body["prediction"])
    assert len(set(predictOutput)) <= 1
