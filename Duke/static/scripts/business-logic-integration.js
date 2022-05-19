function calculateRelation1(body, callback) {
    $(function () {
        $.ajax({
            url: '/calculate_relation1',
            dataType: 'json',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({ 'inputArray': body }),
            success: function (data) {
                callback(data)
            }
        })
    })
}

function calculateRelation2(body, callback) {
    $(function () {
        $.ajax({
            url: "/calculate_relation2",
            dataType: 'json',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({ 'inputArray': body }),
            success: function (data) {
                callback(data)
            }
        })
    })
}

function calculateMaxFlow(body, callback) {
    $(function () {
        $.ajax({
            url: "/calculate_maxflow",
            dataType: 'json',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({ 'result': body }),
            success: function (data) {
                callback(data)
            }
        })
    })
}