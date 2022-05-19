from bottle import post, request, response
from RelationHandler import BinaryRelation, Features
import json
from MaxFlow import solve_max_flow

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

    # Возвращение результата обработки в JSON формате
    return {'features' : features, 'isEquivalent' : isEquivalent, 'additionalRelation': additionalRelation}

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

    # Возвращение результата обработки в JSON формате
    return {'features' : features, 'isEquivalent' : isEquivalent, 'inversedRelation': inversedRelation}

# Контроллер, обрабатывающий POST запрос на вычисление максимального потока
@post("/calculate_maxflow")
def calulateMaxFlow():
    # Получение входных данных
    requestBody = json.load(request.body).get('result')
    inputArray = requestBody.get('inputArray')
    source = requestBody.get('source')
    sink = requestBody.get('sink')

    # Поулчение резлуьтатов обработки входных данных
    result = solve_max_flow(inputArray, source, sink)

    # Возвращение результата обработки в JSON формате
    return{'result': result}
