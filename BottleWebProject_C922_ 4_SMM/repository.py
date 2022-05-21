from bottle import post, request
from relation_handler import BinaryRelation, Features
import json
from max_flow import solve_max_flow
from datetime import datetime
import copy

# Метод для сравнения 2 спсиков, возвращает True, если спсики совпадают, и False в ином случае
def assertLists(list1, list2):
    return all(item in list1 for item in list2) and all(item in list2 for item in list1)


# Контроллер, обрабатывающий POST запрос на работу первого калькулятора свойств графа
@post("/calculate_relation1")
def calulateRelation1():
    
    # Получение входных данных
    requestBody = json.load(request.body)
    inputArray = requestBody.get('inputArray')
    
    # Поулчение резлуьтатов обработки входных данных
    relation = BinaryRelation(inputArray)
    features = relation.checkForFeatures()

    # Запись результата работы калькулятора в JSON
    for item in features:
        item = json.dumps(item)
    isEquivalent = assertLists([Features.REFLECTIVE, Features.SYMMETRIC, Features.TRANSITIVE], features)
    additionalRelation = relation.getAdditionalRelation()

    # Логирование действий, и возвращение результата в JSON формате
    result = {'features' : features, 'isEquivalent' : isEquivalent, 'additionalRelation': additionalRelation}
    log(requestBody, result, "calulateRelation1")
    return result


# Контроллер, обрабатывающий POST запрос на работу второго калькулятора свойств графа
@post("/calculate_relation2")
def calulateRelation2():
    # Получение входных данных
    requestBody = json.load(request.body)
    inputArray = requestBody.get('inputArray')

    # Поулчение резлуьтатов обработки входных данных
    relation = BinaryRelation(inputArray)
    features = relation.checkForFeatures()

    # Запись результата работы калькулятора в JSON
    for item in features:
        item = json.dumps(item)
    isEquivalent = assertLists([Features.ASYMMETRIC, Features.ANTI_TRANSITIVE], features)
    inversedRelation = relation.getInversedRelation()

    # Логирование действий, и возвращение результата в JSON формате
    result = {'features' : features, 'isEquivalent' : isEquivalent, 'inversedRelation': inversedRelation}
    log(requestBody, result, "calulateRelation2")
    return result


# Контроллер, обрабатывающий POST запрос на вычисление максимального потока
@post("/calculate_maxflow")
def calulateMaxFlow():
    # Получение входных данных
    inputJSON = json.load(request.body).get('result')
    requestBody = copy.deepcopy(inputJSON)
    inputArray = requestBody.get('inputArray')
    source = requestBody.get('source')
    sink = requestBody.get('sink')
    # Логирование действий, и возвращение результата в JSON формате
    result = solve_max_flow(inputArray, source, sink)
    log(inputJSON, result, "calulateMaxFlow")
    return{'result': result}


def log(input_data, output_data, method):
    with open("log.txt", "a") as myfile:
        myfile.write("Input: " + str(input_data) + "\nOutput: " + str(output_data) + "\nMethod: " + method + "\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n")
