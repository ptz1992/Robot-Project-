const api = "https://a81debe7-314e-4eff-8e49-ee08c2237318.mock.pstmn.io/test"

// document.getElementById("demo1").innerHTML = json.quiz.sport.q1.question[0];

let xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function () {
	if(xhttp.readyState == 4 && xhttp.status == 200){
		jsonfunc(this.responseText); //this = xhttp
//		jsonfunc(xhttp.responseText); // 둘다 가능
	}
}
xhttp.open("GET", api, true);
xhttp.send();

function jsonfunc( jsonText ) {

	let json = JSON.parse(jsonText); // String -> json으로 변환
	
	let txt = "";
  let arr = []
	for(i=0; i<1; i++){
		for(key in json[i]){ // key값은 name, bat, rgb
      // txt += key + ":" + json[i][key]; 
		}
    if (key = "bat"){
      txt += json[i][key]
    }
	}
  if(txt = 60){
    document.getElementById('omo').innerHTML = "<div class='pie-chart pie-chart2'><span class='center'>60%</span></div>"
  }
}

//<span class='center'>50%</span>