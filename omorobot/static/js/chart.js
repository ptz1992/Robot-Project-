var ctx = document.getElementById('myChart2');
	  
	var config = {
		type: 'line',
		data: {
			labels: [ // Date Objects
				'30',
				'60',
				'90',
				'120',
				'150',
				// 'data6',
				// 'data7'
			],
			datasets: [
			// 	{
			// 	label: 'My First dataset',
			// 	backgroundColor: 'rgba(75, 192, 192, 1)',
			// 	borderColor: 'rgba(75, 192, 192, 1)',
			// 	fill: false,
			// 	data: [
					

			// 	],
			// }, {
			// 	label: 'My Second dataset',
			// 	backgroundColor: 'rgba(255, 99, 132, 1)',
			// 	borderColor: 'rgba(255, 99, 132, 1)',
			// 	fill: false,
			// 	data: [
					

			// 	],
			// },
			// {
			// 	label: '90RPM',
			// 	backgroundColor: 'rgba(255, 99, 132, 1)',
			// 	borderColor: 'rgba(255, 99, 132, 1)',
			// 	fill: false,
			// 	data: [
					
			// 	],
			// }
		]
		},
		options: {
			
				
			maintainAspectRatio: false,
			title: {
				text: 'Chart.js Time Scale'
			},
			scales: {
				xAxes: [{
					ticks:{
						fontColor : 'black',
						fontSize: 24
					}
				}],

				yAxes: [{
					ticks:{
						fontColor : 'black',
						fontSize: 24
					},
					scaleLabel: {
						display: true,
						labelString: ''
					}
				}]
			},
		}
	};
	 
//차트 그리기
var myChart2 = new Chart(ctx, config);
	  
//-----------//-----------//-----------//-----------//-----------//-----------//-----------
	//데이터 추가
	document.getElementById('addData').onclick = function(){
		
		$('#inputzone').append('<input class="chart-value" type="text" value=""><br>')


		//라벨추가
		config.data.labels.push('data'+config.data.labels.length)
		
		//데이터셋 수 만큼 반복
		var dataset = config.data.datasets;
		for(var i=0; i<dataset.length; i++){
			//데이터셋의 데이터 추가
		}
		myChart2.update();	//차트 업데이트
	}
	//-----------//-----------//-----------//-----------//-----------//-----------//-----------
	//데이터셋 추가
	document.getElementById('set-chart').onclick = function(){
		// console.log("함수 실행됨")

		var color1 = Math.floor(Math.random() * 256);
		var color2 = Math.floor(Math.random() * 256);
		var color3 = Math.floor(Math.random() * 256);
		
		console.log(color1 + " " + color2 + " " + color3)
		
		var newDataset = {
			label: $("#speed1").val() +"-"+ $("#encoder1").val(),
			// borderColor : 'rgba('+color1+', '+color2+', '+color3+', 1)',
			borderColor: 'rgb(255, 255, 255)',
			// backgroundColor : 'rgba('+color1+', '+color2+', '+color3+', 1)',
			bacgroundColor: 'rgb(255, 255, 255)',
			data: [],
			fill: false
		}
		
		// newDataset에 데이터 삽입
		for(let i=0; i<$(".chart-value").length;i++){
			if($(".chart-value")[i].value > 0){
			 newDataset.data.push($(".chart-value")[i].value);
		 }
	 }

		// chart에 newDataset 푸쉬
		config.data.datasets.push(newDataset);
		
		myChart2.update();	//차트 업데이트
		console.log($(".chart-value"))
	}
	//-----------//-----------//-----------//-----------//-----------//-----------//-----------
	//데이터 삭제
	document.getElementById('delData').onclick = function(){


		console.log($('.chart-value')[$('.chart-value').length - 1])

		$('.chart-value')[$('.chart-value').length - 1].remove()
		$('#inputzone br')[$('#inputzone br').length - 1].remove()
		

		
		config.data.labels.splice(-1,1);//라벨 삭제
		
		//데이터 삭제
		config.data.datasets.forEach(function(dataset) {
			dataset.data.pop();
		});
		
		myChart2.update();	//차트 업데이트
	}

//-----------//-----------//-----------//-----------//-----------//-----------//-----------

	//데이터셋 삭제
	document.getElementById('delDataset').onclick = function(){
		config.data.datasets.splice(-1,1);
		myChart2.update();	//차트 업데이트
		console.log($(".chart-value"))

}



document.getElementById('del_line_dset').onclick = function(){
	config.data.datasets.splice(-10,10);
	myChart2.update();	//차트 업데이트
	console.log($(".chart-value"))
}




	
	
	//데이터 적용