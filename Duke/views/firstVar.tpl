% rebase('layout.tpl', year=year)

<h1>Первый вариант</h1>
<div class="cards_container">
	<h2>Исходные данные</h2>
	<h2>Результат</h2>
</div>
<div class="cards_container">
	<div class="solution_card">
		Количество вершин графа<br>
		<div class="small-padding-top" class="fill_horizontally">
			<input class="fill_horizontally text input-verticies-count" type="text" name="n" value="3"><br>
		</div>
		<table id="table">
		  <tr>
			<td><input type="text" class="table-input" placeholder="0"></td>
			<td><input type="text" class="table-input" placeholder="0"></td> 
			<td><input type="text" class="table-input" placeholder="0"></td>
		  </tr>
		  <tr>
			<td><input type="text" class="table-input" placeholder="0"></td>
			<td><input type="text" class="table-input" placeholder="0"></td> 
			<td><input type="text" class="table-input" placeholder="0"></td>
		  </tr>
		  <tr>
			<td><input type="text" class="table-input" placeholder="0"></td>
			<td><input type="text" class="table-input" placeholder="0"></td> 
			<td><input type="text" class="table-input" placeholder="0"></td>
		  </tr>
		</table>
		<button class="button button-padding" id="calculate">Посчитать</button>
	</div>

	<div class="solution_card">
		<table id="table1">
			<tr>
				<td><input type="text" class="table-input" placeholder="0"></td>
				<td><input type="text" class="table-input" placeholder="0"></td> 
				<td><input type="text" class="table-input" placeholder="0"></td>
			</tr>
			<tr>
				<td><input type="text" class="table-input" placeholder="0"></td>
				<td><input type="text" class="table-input" placeholder="0"></td> 
				<td><input type="text" class="table-input" placeholder="0"></td>
			</tr>
			<tr>
				<td><input type="text" class="table-input" placeholder="0"></td>
				<td><input type="text" class="table-input" placeholder="0"></td> 
				<td><input type="text" class="table-input" placeholder="0"></td>
			</tr>
		</table>
		<div class="padding-top">
		 	Свойства<br>
			<div class="small-padding-top" class="fill_horizontally">
				<textarea class="fill_horizontally text" name="text" rows="4"></textarea>
			</div>
		</div>
	</div>
</div>

<script>
	$(function() {
		
		$('.input-verticies-count').on('input', function() {

			   var verticiesInput = $('.input-verticies-count');
			   if(isNaN(verticiesInput.val()) || verticiesInput.val() < 2){
				   verticiesInput.val(2)
			   }

		})				
	});
</script>