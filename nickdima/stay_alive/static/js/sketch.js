function setup(){
	let canvas = createCanvas(400, 400);
	canvas.parent('sketch-holder');
}

function draw(){
	background(0, 0, 0);

	fill(255, 255, 255);
	if(hero_data){
		for(let i = 0; i < hero_data.length; i++){
			rect(hero_data[i]['location'][0], hero_data[i]['location'][1], hero_data[i]['hitbox']['x_len'], hero_data[i]['hitbox']['y_len']);
		}
	}
}



function keyPressed(){
    if (keyCode === LEFT_ARROW){
        
    } else if (keyCode === RIGHT_ARROW){

        
    } else if (keyCode === DOWN_ARROW){
        move_down = true;
        
    } else if (keyCode === UP_ARROW){
        move_up = true;
    } else if (keyCode == 13){

    }
}



function keyReleased(){
    if (keyCode === LEFT_ARROW){

        
    } else if (keyCode === RIGHT_ARROW){

        
    } else if (keyCode === DOWN_ARROW){
        move_down = false;
        
    } else if (keyCode === UP_ARROW){
        move_up = false;
    }
}