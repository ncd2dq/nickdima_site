let vision_x_max = 800;
let vision_y_max = 800;
let player_pos_x = 400;
let player_pos_y = 400;
let player_actual_x;
let player_actual_y;

let background_img;

function preload(){
	background_img = loadImage("http://www.nickdima.com/stay_alive/static/assets/background.png");
}

function setup(){
	let canvas = createCanvas(vision_x_max, vision_y_max);
	canvas.parent('sketch-holder');
}

function draw(){
	background(0, 0, 0); //This refreshes the sketch
	// Determine players actual position
	if(hero_data){
		for(let i = 0; i < hero_data.length; i++){
			if(hero_data[i]['id'] == my_hero_id){
				player_actual_x = hero_data[i]['location'][0];
				player_actual_y = hero_data[i]['location'][1];
				break;
			}
		}
	}

	//Move the area of the background image we are drawing
	//image(background_img, 
	//subx, suby,  --The position of the subset image ON THE CANVAS
	//subwidth, subheight,  --The dimensions of the subset image
	//canvasx, canvasy,    --The position of the subset image within the parent image
	//canvaswidthsize, canvasheightsize --How large to draw it on the canvas
	// Always draw the subset image start at 0,0 of the canvas
	// The subset image will always have max_x / max_y the length of our canvas (this is all the player can see)
	// The subset image is a fixed square (400x400) around the actual position of the hero
	// Draw the image exactly the same size on the screen
	if(hero_data){
		image(background_img, 
		0, 0, 
		vision_x_max, vision_y_max, 
		player_actual_x - player_pos_x, player_actual_y - player_pos_y, 
		vision_x_max, vision_y_max);
	}


	//Draw your hero in the center and other heros as relative to you
	fill(255, 255, 255);
	if(hero_data){
		for(let i = 0; i < hero_data.length; i++){
			if(hero_data[i]['id'] == my_hero_id){
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

	if(hero_data){
		fill(255, 255, 255);
		rect(10, 10, vision_x_max - 20, 10);
		fill(0, 0, 0);
		rect(10, 10, daylight_data['current'] / daylight_data['maxi'] * (vision_x_max - 20) , 10);

		//Night time cycle: 1/4 1/2 3/4 of the second half of the day
		if(daylight_data['current'] > (daylight_data['maxi'] / 2) + ((daylight_data['maxi'] / 2) * 3 / 4)){
			background(0, 0, 0, 175);
		} else if(daylight_data['current'] > (daylight_data['maxi'] / 2) + ((daylight_data['maxi'] / 2) / 2)){
			background(0, 0, 0, 100);
		} else if(daylight_data['current'] > (daylight_data['maxi'] / 2) + ((daylight_data['maxi'] / 2) / 4)){
			background(0, 0, 0, 50);
		}
	}

	if(hero_data){
		
		for(let i = 0; i < resource_nodes_data.length; i++){

			if(resource_nodes_data[i]['type'] == 'water'){
				fill(0, 0, 255);
			} else if (resource_nodes_data[i]['type'] == 'wood'){
				fill(130, 82, 1);
			} else if (resource_nodes_data[i]['type'] == 'brick'){
				fill(165, 42, 42);
			} else if (resource_nodes_data[i]['type'] == 'steal'){
				fill(70, 70, 70);
			}

			let rel_x = player_actual_x - resource_nodes_data[i]['location'][0];
			let rel_y = player_actual_y - resource_nodes_data[i]['location'][1];

			ellipse(player_pos_x - rel_x, player_pos_y - rel_y,
				resource_nodes_data[i]['hitbox']['x_len'], resource_nodes_data[i]['hitbox']['y_len']);
		}
	}

	//TODO: DRAW WALLS LOOP

	if(hero_data){
		update_inventory();
	}
}

function update_inventory(){
	let cur_hero = false;
	for(let i = 0; i < hero_data.length; i++){
		if(hero_data[i]['id'] == my_hero_id){
			cur_hero = hero_data[i];
		}
	}

	let water_elm = document.getElementById('water');
	water_elm.innerHTML = 'Water: ' + cur_hero['inventory']['water'];
	let wood_elm = document.getElementById('wood');
	wood_elm.innerHTML = 'Wood: ' + cur_hero['inventory']['wood'];
	let brick_elm = document.getElementById('brick');
	brick_elm.innerHTML = 'Brick: ' + cur_hero['inventory']['brick'];
	let iron_elm = document.getElementById('steal');
	iron_elm.innerHTML = 'Steal: ' + cur_hero['inventory']['steal'];

	/*
	let ammo_elm = document.getElementById('ammo');
	ammo_elm.innerHTML = 'Ammo: ' + ;
	let gun_elm = document.getElementById('gun');
	gun_elm.innerHTML = 'Gun: ' + ;
	let tool_elm = document.getElementById('tool');
	tool_elm.innerHTML = 'Tool: ' + ;
	*/
}



function keyPressed(){
    if (keyCode === LEFT_ARROW || keyCode == 65){
        move('pressed', 'left');
    } else if (keyCode === RIGHT_ARROW || keyCode == 68){
        move('pressed', 'right');
        
    } else if (keyCode === DOWN_ARROW || keyCode == 83){
        move('pressed', 'down');
        
    } else if (keyCode === UP_ARROW || keyCode == 87){
        move('pressed', 'up');
    } else if (keyCode == 13){

    } else if (keyCode == 82){
    	//R key "action key"
    	action_key();
    	//TODO: IF YOU PRESS R WHILE A TOOL IS EQUIPPED, THEN CALL THE BUILD FUNCTION FOR 
    	//WHATEVER IS CURRENTLY BEING BUILT
    }
}



function keyReleased(){
    if (keyCode === LEFT_ARROW || keyCode == 65){
        move('released', 'left');
        
    } else if (keyCode === RIGHT_ARROW || keyCode == 68){
        move('released', 'right');
        
    } else if (keyCode === DOWN_ARROW || keyCode == 83){
        move('released', 'down');
        
    } else if (keyCode === UP_ARROW || keyCode == 87){
        move('released', 'up');
    }
}