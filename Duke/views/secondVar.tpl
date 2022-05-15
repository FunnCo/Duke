% rebase('layout.tpl', year=year)

<h1>Второй вариант</h1>
<div class="cards_container">
	<h2>Исходные данные</h2>
	<h2>Результат</h2>
</div>
<div class="cards_container">
	 <div class="solution_card">
		Количество вершин графа<br>
		<div class="small-padding-top" class="fill_horizontally">
			<input class="fill_horizontally text" type="text" name="n" value=""><br>
		</div>
		<table id="table">
		  <tr>
			<th>1</th>
			<th>2</th> 
			<th>3</th>
		  </tr>
		  <tr>
			<td>4</td>
			<td>5</td> 
			<td>6</td>
		  </tr>
		  <tr>
			<td>7</td>
			<td>8</td> 
			<td>9</td>
		  </tr>
		</table>
		<button class="button button-padding">Посчитать</button>
	</div>

	<div class="solution_card">
		<table id="table1">
			<tr>
				<th>1</th>
				<th>2</th> 
				<th>3</th>
			</tr>
			<tr>
				<td>4</td>
				<td>5</td> 
				<td>6</td>
			</tr>
			<tr>
				<td>7</td>
				<td>8</td> 
				<td>9</td>
			</tr>
		</table>
		 <div class="padding-top">
		 	Свойства<br>
			<div class="small-padding-top" class="fill_horizontally">
				<textarea class="fill_horizontally text" name="text" rows="3"></textarea>
			</div>
		</div>
	</div>
</div>