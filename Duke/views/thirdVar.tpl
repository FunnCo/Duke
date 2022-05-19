% rebase('layout.tpl', year=year)

<h1>Калькулятор максимального потока</h1>
<p class="description">Требуется найти максимальный поток в сети от источника s к стоку t. </p>
<div class="center">
	<div class="third_cards_subcontainer">
		 <h2>Исходные данные</h2>
		 <div class="solution_card">
		 	<div class="top_padding_05">
			Координаты источника<br>
			</div>
			<div class="top_padding_05">
				<input class="fill_horizontally text" type="text" name="n" id="source" value=""><br>
			</div>
			<div class="top_padding_05">
			Координаты стока<br>
			</div>
			<div class="top_padding_05">
				<input class="fill_horizontally text" type="text" name="n" id="sink" value=""><br>
			</div>
			<div class="top_padding_05">
			Количество вершин графа<br>
			</div>
			<div class="top_padding_05">
				<input class="fill_horizontally text input-verticies-count" type="text" name="n" value="3"><br>
			</div>
			<table id="table" class="verticies_table non-binary-table input-table">
			</table>
			<button class="button top_margin_2" id="calculate">Посчитать</button>
		</div>

		<h2>Результат</h2>
		<div class="solution_card">
			<div class="top_padding_05" class="fill_horizontally">
				<input class="fill_horizontally text" id="flow-result" type="text" name="n" value=""><br>
			</div>
		</div>
	</div>
</div>

<script>
	handleResize();

	var verticiesElement = $(".input-verticies-count")

	$('#sink').on('click', function() {
		$(this).select()
	})

	$('#sink').on('input', function() {

		if(isNaN($(this).val()) || $(this).val() < 0 || $(this).val() > verticiesElement.val()){
			$('#sink').val(1)
		}
		$(this).select()
	})

	$('#source').on('click', function() {
		$(this).select()
	})

	$('#source').on('input', function() {
		var currentValue = $(this).val()

		if(currentValue < 1 || currentValue > verticiesElement.val()){
			$('#source').val(1)
		}
		$(this).select()
	})

	$('#calculate').on('click', function() {
		var body = {}

		var graph = []
		var verticies = $(".input-verticies-count").val();
		var table = $('.input-table');
        for (var r = 0; r < verticies; r++) {
            var currentRow = []
            for (var c = 0; c < verticies; c++){
                currentRow.push(parseInt($(`#input-item${r}${c}`).val()))
			}
            graph.push(currentRow)
        }
		body["inputArray"] = graph
		body["source"] = parseInt($("#source").val())-1
		body["sink"] = parseInt($("#sink").val())-1
			console.log(body)
		calculateMaxFlow(body, function(data){
			console.log(data)
			
			var resultBox = $('#flow-result')
			console.log(data['result'])
			resultBox.val(data['result'])
		})
	})
</script>