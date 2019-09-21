var turn;
var pscore=0;
var cscore=0;
var check=['012','036','048','345','147','246','678','258'];
var array_of_none=[];
var array_of_player=[];
var array_to_check=[];
var array_of_cpu=[];
var player="TickTackToe_Image/o.png";
var cpu="TickTackToe_Image/x.jpg";
var y;
var i;
var miss=0;

function adding(){
	var array_of_td=document.getElementsByTagName('td');
	for(x=0;x<9;x++){
		array_of_td[x].setAttribute('class','none');
		array_of_td[x].setAttribute('onclick','Update(this,player);');
   }
}
function removing(){
	array_of_player=[];
	array_of_cpu=[];
	var item =document.getElementsByTagName('img');
	while(item.length!=0){
		item[0].parentNode.removeChild(item[0]);
	}
	adding();
}
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function Update(pass,who){
	var element=document.createElement('img');
	element.setAttribute('style','width:100px;height:100px;');
	element.setAttribute('src',who);
	if(who.search(cpu)==-1){
		turn='P';//now turn for player
		pass.setAttribute('class','player');
	}
    else {
		turn='C';//now turn for CPU
		pass.setAttribute('class','cpu');}
		pass.setAttribute('onclick','alert("already clicked")');
		pass.appendChild(element);
	   chance(pass,who);
}
function chance(pass,who){
	sleep(100);
	array_to_check=[];
    if(turn=='P'){// collecting all attempts of player OR cpu
			array_of_player.push((pass.id).toString());
			array_to_check=array_of_player;
	}
    else{
			array_of_cpu.push((pass.id).toString());
			array_to_check=array_of_cpu;
		
	}
    if(array_to_check.length>=3){
		for(i=0;i<check.length;i++){
			hit=0;
			for(y=0;y<array_to_check.length;y++){
				if(check[i].search((array_to_check[y]))!=-1)
					hit++;
				}
		   if(hit==3){// checking if there is any combination
			   if(turn=='C'){
			   turn='N';
			   document.getElementById("cscores").lastChild.innerHTML= 1+parseInt(document.getElementById("cscores").lastChild.innerHTML);  
			   alert("cpu win");break;
			   }
			   else{
			   turn='N';
			   document.getElementById("pscores").lastChild.innerHTML= 1+parseInt(document.getElementById("pscores").lastChild.innerHTML);
			   alert("player win");break;
			   }
			}   
		}  //close of loop that generate all check elements
	 
	}
	if(turn=='N')
		removing();
	array_of_none=document.getElementsByClassName("none");
	if(array_of_none.length==0){//check for any empty element\
		alert("no one wins ");
		removing();
	}
	else if(turn=='P')//if last turn was of player so now cpu 
		cputurn();
}

function cputurn(){
	var what_to_pass;//var to pass as cpu turn
	if(array_of_player.length==1){//For first move
		var rand=Math.floor(((Math.random() *10)% array_of_none.length) );
		what_to_pass=array_of_none[rand];
	}
	else {
		array_to_check=array_of_cpu;
		var idx=checkWin();//if next move would win ---the cpu--- or no -1=no move will make player win
		if(idx!=-1){//element found that can make cpu win
			what_to_pass=document.getElementById(idx);//element move of cpu 
			
		}
		
		else {//player wont play to win
		    array_to_check=array_of_player;
			idx=checkWin();///if next move would win ---the player--- or no -1=no move will make player win
			if(idx!=-1){//element found that can make cpu win 
				what_to_pass=document.getElementById(idx);//element move of cpu 
			}
			else{
				var rand=Math.floor(((Math.random() *10)% array_of_none.length) );
				what_to_pass=array_of_none[rand];
			}
		}
	}
	Update(what_to_pass,cpu);
}
function checkWin(){
	var temp_id=[];
	for(i=0;i<array_of_none.length;i++){
		temp_id.push(array_of_none[i].id.toString());
	}
    var temp=[];
	for(i=0;i<check.length;i++){
        var diff=0;
		temp=check[i];
		for(y=0;y<array_to_check.length;y++){
		    if(temp.search((array_to_check[y]))!=-1){
				temp=temp.replace(array_to_check[y],"");
			}
		}
		if(temp.length==1 && temp_id.toString().search(temp)!=-1){
			break;
		} 
	}
	if(i==check.length)
	return -1;
	else
	return temp;
}
