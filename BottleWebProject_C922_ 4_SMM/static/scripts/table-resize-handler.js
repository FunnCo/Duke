/**
 * Функция для обработки изменения размера таблицы. Вызывается при инциализации таблицы,
 * и при измении количества вершин в графе
 * */
function handleResize() {
    $(function () {
        // Первичная генерация таблицы, с размером по умолчанию
        generateTable()

        // При изменении количества вершин в графе происходит перегенерация таблицы
        $('.input-verticies-count').on('input', function () {
            generateTable()
        })

        // При клике на поле для количества вершин, оно автоматически выбирается
        $('.input-verticies-count').on('click', function () {
            $(this).select()
        })
    });
}

/**
 * Функция генерации таблицы
 * */
function generateTable() {

    // Обработка случае при некорректном количстве вершин
    var verticiesInput = $('.input-verticies-count');
    if (isNaN(verticiesInput.val()) || verticiesInput.val() < 2 || verticiesInput.val() > 9 || !verticiesInput.val()) {
        verticiesInput.val(2);
        verticiesInput.select();
    }

    // Автоматическое выделение значения в поле ввода количества вершин, для удобства пользователя
    verticiesInput.select();

    // Поулчение количества вершин в графе
    var verticies = verticiesInput.val();

    // Удаление всех ячеек во всех таблицах на странице
    $(".verticies_table tbody > tr").remove();

    // Генерация новых ячеек для всех таблицах на странице
    $(".verticies_table").each(function () {
        
        var table = $(this);
        for (var r = 0; r < verticies; r++) {
            var tr = $('<tr>');
            for (var c = 0; c < verticies; c++)

                // Если таблица предназначена для вывода результата, то для нее устанавливается аттрибут readonly, иначе значение можно редактировать
                if (table.attr("id") == "table1") {
                    $(`<td><input type="text" id="output-item${r}${c}" class="table-input" value="0" readonly></td>`).appendTo(tr);
                } else {
                    $(`<td><input type="text" id="input-item${r}${c}" class="table-input" value="0"></td>`).appendTo(tr);
                }
            tr.appendTo(table);
        }

        // Выделение значения ячейки, при клике на нее
        $('.table-input').on('click', function () {
            $(this).select()
        })

        // Обработка ввода в ячейки, и изменение их значения, если введен некорректный результат
        $('.table-input').on('input', function () {

            // Если таблица, в которой нахдодится эта ячейка, не является матрицей для бинарного отношения,
            // то необходимо автоматически выделять значения поля, для удобства пользователя
            var isBinary = $(this).parents().hasClass('non-binary-table');
            if (!isBinary) {
                $(this).select();
            }

            // Обработка некорректного ввода
            if (isNaN($(this).val()) || $(this).val() < 0 || $(this).val() > 1 && !isBinary || !$(this).val()) {
                $(this).val(0);
            }

        })
    })
}