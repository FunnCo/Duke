% rebase('layout.tpl', year=year)

<h1>Третий вариант</h1>
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
			<table id="table">
				<tbody>
				  <tr>
					<td>
						<input type="text" class="table-input" placeholder="0">
					</td>
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
			  <tbody>
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

