function handleResize() {
    $(function () {

        var verticies = $('.input-verticies-count').val();
        $(".verticies_table").each(function () {
            var table = $(this);
            for (var r = 0; r < verticies; r++) {
                var tr = $('<tr>');
                for (var c = 0; c < verticies; c++)
                    if (table.attr("id") == "table1") {
                        $('<td><input type="text" class="table-input" value="0" readonly></td>').appendTo(tr);
                    } else {
                        $('<td><input type="text" class="table-input" value="0"></td>').appendTo(tr);
                    }
                tr.appendTo(table);
            }
        })

        $('.input-verticies-count').on('input', function () {

            var verticiesInput = $('.input-verticies-count');
            if (isNaN(verticiesInput.val()) || verticiesInput.val() < 2 || verticiesInput.val() > 9) {
                verticiesInput.val(2);
                verticiesInput.select();
            }
            verticiesInput.select();
            var verticies = verticiesInput.val();
            $(".verticies_table tbody > tr").remove();
            $(".verticies_table").each(function () {
                var table = $(this);
                for (var r = 0; r < verticies; r++) {
                    var tr = $('<tr>');
                    for (var c = 0; c < verticies; c++)
                        if (table.attr("id") == "table1") {
                            $('<td><input type="text" class="table-input" value="0" readonly></td>').appendTo(tr); //fill in your cells with something meaningful here
                        } else {
                            $('<td><input type="text" class="table-input" value="0"></td>').appendTo(tr);
                        }
                    tr.appendTo(table);
                }
                $('.table-input').on('click', function () {
                    $(this).select()
                })
            })
        })

        $('.input-verticies-count').on('click', function () {
            $(this).select()
        })
    });
}