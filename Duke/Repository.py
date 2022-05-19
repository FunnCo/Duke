from bottle import post, request, response
from RelationHandler import BinaryRelation, Features
import json
from MaxFlow import solve_max_flow

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

    return {'features' : features, 'isEquivalent' : isEquivalent, 'additionalRelation': additionalRelation}


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

    return {'features' : features, 'isEquivalent' : isEquivalent, 'inversedRelation': inversedRelation}

@post("/calculate_maxflow")
def calulateMaxFlow():
    requestBody = json.load(request.body).get('result')
    inputArray = requestBody.get('inputArray')
    source = requestBody.get('source')
    sink = requestBody.get('sink')
    result = solve_max_flow(inputArray, source, sink)
    return{'result': result}
