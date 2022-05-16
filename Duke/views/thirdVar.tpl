% rebase('layout.tpl', year=year)

<h1>Калькулятор максимального потока</h1>
<p class="description">Требуется найти максимальный поток в сети от источника s к стоку t. </p>
<div class="center">
	<div class="third_cards_subcontainer">
		 <h2>Исходные данные</h2>
		 <div class="solution_card">
			Координаты источника<br>
			<div class="small-padding-top" class="fill_horizontally">
				<input class="fill_horizontally text" type="text" name="n" value=""><br>
			</div>
			Координаты стока<br>
			<div class="small-padding-top" class="fill_horizontally">
				<input class="fill_horizontally text" type="text" name="n" value=""><br>
			</div>
			Количество вершин графа<br>
			<div class="small-padding-top" class="fill_horizontally">
				<input class="fill_horizontally text input-verticies-count" type="text" name="n" value="3"><br>
			</div>
			<table id="table" class="verticies_table">
			</table>
			<button class="button button-padding" id="calculate">Посчитать</button>
		</div>

		<h2>Результат</h2>
		<div class="solution_card">
			<div class="small-padding-top" class="fill_horizontally">
				<input class="fill_horizontally text" type="text" name="n" value=""><br>
			</div>
		</div>
	</div>
</div>

<script>
	handleResize();
</script>