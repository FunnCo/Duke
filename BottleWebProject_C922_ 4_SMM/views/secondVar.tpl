% rebase('layout.tpl', year=year)

<h1>Калькулятор свойств отношений (с нахождением обратного)</h1>
<p class="description">Требуется определить, обладает ли данное бинарное отношение 
одновременно свойствами асимметричности и антитранзитивности. Найти обратное к данному отношение.</p>
<div class="cards_container">
	<h2>Исходные данные</h2>
	<h2>Результат</h2>
</div>
<div class="cards_container">
	 <div class="solution_card">
		Количество вершин графа<br>
		<div class="top_padding_05">
			<input class="fill_horizontally text input-verticies-count" type="text" name="n" value="3"><br>
		</div>
		<table id="table" class="verticies_table input-table">
		</table>
		<button id="calculate" class="button top_margin_2">Посчитать</button>
	</div>

	<div class="solution_card">
		Обратное отношение<br>
		<table id="table1" class="verticies_table top_margin_1 output-table">
		</table>
		 <div class="top_padding_1">
		 	Свойства<br>
			<div class="top_padding_05" class="fill_horizontally">
				<textarea class="fill_horizontally text" id="features-result" name="text" rows="4"></textarea>
			</div>
		</div>
	</div>
</div>

<script>
	handleResize();

	$('#calculate').on('click', function() {
		var body = []

		var verticies = $(".input-verticies-count").val();
		var table = $('.input-table');
        for (var r = 0; r < verticies; r++) {
            var currentRow = []
            for (var c = 0; c < verticies; c++){
                currentRow.push(parseInt($(`#input-item${r}${c}`).val()))
			}
            body.push(currentRow)
        }

		calculateRelation2(body, function(data){
			console.log(body)
			table = $('.output-table');
			for (var r = 0; r < verticies; r++) {				
				for (var c = 0; c < verticies; c++){
					$(`#output-item${r}${c}`).val(data['inversedRelation'][r][c])
				}
			}
			var resultBox = $('#features-result')
			resultBox.val('')
			if(data['isEquivalent']){
				resultBox.val(resultBox.val() + "Соответсвует условиям задачи\n\n")
			} else {
				resultBox.val(resultBox.val() + "Не соответсвует условиям задачи\n\n")
			}
			resultBox.val(resultBox.val() + "Свойства введенного графа:\n")
			data['features'].forEach(element => resultBox.val(resultBox.val() + element + " "))
		})
	})
</script>