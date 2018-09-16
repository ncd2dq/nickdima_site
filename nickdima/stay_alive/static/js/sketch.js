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