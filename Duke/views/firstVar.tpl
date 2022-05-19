% rebase('layout.tpl', year=year)

<h1>Калькулятор свойств отношений (с нахождением дополнительного)</h1>
<p class="description">Требуется определить, является ли заданное бинарное отношение 
отношением эквивалентности, т.е., является ли оно одновременно рефлексивным, симметричным и транзитивным. 
Найти дополнительное отношение к данному.</p>
<div class="cards_container">
	<h2>Исходные данные</h2>
	<h2>Результат</h2>
</div>
<div class="cards_container">
	<div class="solution_card">
		Количество вершин графа<br>
		<div class="small-padding-top">
			<input class="fill_horizontally text input-verticies-count" type="text" name="n" value="3"><br>
		</div>
		<table id="table" class="verticies_table input-table">
		</table>
		<button class="button button-padding" id="calculate">Посчитать</button>
	</div>

	<div class="solution_card">
		Дополнительное отношение<br>
		<table id="table1" class="verticies_table small-margin-top output-table">
		</table>
		<div class="padding-top">
		 	Свойства<br>
			<div class="small-padding-top" class="fill_horizontally">
				<textarea class="fill_horizontally text" name="text" id="features-result" rows="4"></textarea>
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

		calculateRelation1(body, function(data){
			console.log(body)
			table = $('.output-table');
			for (var r = 0; r < verticies; r++) {				
				for (var c = 0; c < verticies; c++){
					$(`#output-item${r}${c}`).val(data['additionalRelation'][r][c])
				}
			}
			var resultBox = $('#features-result')
			resultBox.val('')
			if(data['isEquivalent']){
				resultBox.val(resultBox.val() + "Данный граф эквивалентен\n\n")
			} else {
				resultBox.val(resultBox.val() + "Данный граф не эквивалентен\n\n")
			}
			resultBox.val(resultBox.val() + "Свойства введенного графа:\n")
			data['features'].forEach(element => resultBox.val(resultBox.val() + element + " "))
		})
	})
</script>