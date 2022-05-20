from bottle import post, request, response
from relation_handler import BinaryRelation, Features
import json
from max_flow import solve_max_flow
from datetime import datetime

def assertLists(list1, list2):
    return all(item in list1 for item in list2) and all(item in list2 for item in list1)

@post("/calculate_relation1")
def calulateRelation1():
    requestBody = json.load(request.body)
    inputArray = requestBody.get('inputArray')

    relation = BinaryRelation(inputArray)
    features = relation.checkForFeatures()
    for item in features:
        item = json.dumps(item)
    isEquivalent = assertLists([Features.REFLECTIVE, Features.SYMMETRIC, Features.TRANSITIVE], features)
    additionalRelation = relation.getAdditionalRelation()

    result = {'features' : features, 'isEquivalent' : isEquivalent, 'additionalRelation': additionalRelation}
    log(requestBody, result, "calulateRelation1")
    return result


@post("/calculate_relation2")
def calulateRelation2():
    requestBody = json.load(request.body)
    inputArray = requestBody.get('inputArray')

    relation = BinaryRelation(inputArray)
    features = relation.checkForFeatures()
    for item in features:
        item = json.dumps(item)
    isEquivalent = assertLists([Features.ASYMMETRIC, Features.ANTI_TRANSITIVE], features)
    inversedRelation = relation.getInversedRelation()

    result = {'features' : features, 'isEquivalent' : isEquivalent, 'inversedRelation': inversedRelation}
    log(requestBody, result, "calulateRelation2")
    return result

@post("/calculate_maxflow")
def calulateMaxFlow():
    requestBody = json.load(request.body).get('result')
    inputArray = requestBody.get('inputArray')
    source = requestBody.get('source')
    sink = requestBody.get('sink')
    result = solve_max_flow(inputArray, source, sink)
    log(requestBody, result, "calulateMaxFlow")
    return{'result': result}

def log(input_data, output_data, method):
    with open("log.txt", "a") as myfile:
        myfile.write("Input: " + str(input_data) + "\nOutput: " + str(output_data) + "\nMethod: " + method + "\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n")
