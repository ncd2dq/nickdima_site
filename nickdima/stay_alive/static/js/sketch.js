let vision_x_max = 400;
let vision_y_max = 400;
let player_pos_x = 200;
let player_pos_y = 200;
let player_actual_x;
let player_actual_y;

function setup(){
	let canvas = createCanvas(vision_x_max, vision_y_max);
	canvas.parent('sketch-holder');
}

function draw(){
	background(0, 0, 0);

	//Draw your hero in the center and other heros as relative to you
	fill(255, 255, 255);
	if(hero_data){
		for(let i = 0; i < hero_data.length; i++){
			if(hero_data[i]['id'] == my_hero_id){
				player_actual_x = hero_data[i]['location'][0];
				player_actual_y = hero_data[i]['location'][1];
				rect(player_pos_x, player_pos_y, hero_data[i]['hitbox']['x_len'], hero_data[i]['hitbox']['y_len']);
			} else {
				//Determine the relative distance between your hero's actual and the other heros
				let rel_x = player_actual_x - hero_data[i]['location'][0];
				let rel_y = player_actual_y - hero_data[i]['location'][1];

				//Apply the relative x/y translation to where your hero is fixed
				rect(player_pos_x - rel_x, player_pos_y - rel_y, hero_data[i]['hitbox']['x_len'], hero_data[i]['hitbox']['y_len']);
			} 
		}
	}
}



function keyPressed(){
    if (keyCode === LEFT_ARROW){
        move('pressed', 'left');
    } else if (keyCode === RIGHT_ARROW){
        move('pressed', 'right');
        
    } else if (keyCode === DOWN_ARROW){
        move('pressed', 'down');
        
    } else if (keyCode === UP_ARROW){
        move('pressed', 'up');
    } else if (keyCode == 13){

    }
}



function keyReleased(){
    if (keyCode === LEFT_ARROW){
        move('released', 'left');
        
    } else if (keyCode === RIGHT_ARROW){
        move('released', 'right');
        
    } else if (keyCode === DOWN_ARROW){
        move('released', 'down');
        
    } else if (keyCode === UP_ARROW){
        move('released', 'up');
    }
}