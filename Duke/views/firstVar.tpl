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
		<table id="table" class="verticies_table">
		</table>
		<button class="button button-padding" id="calculate">Посчитать</button>
	</div>

	<div class="solution_card">
		Дополнительное отношение<br>
		<table id="table1" class="verticies_table small-margin-top">
		</table>
		<div class="padding-top">
		 	Свойства<br>
			<div class="small-padding-top">
				<textarea class="fill_horizontally text" name="text" rows="4"></textarea>
			</div>
		</div>
	</div>
</div>

<script>
	handleResize();
</script>