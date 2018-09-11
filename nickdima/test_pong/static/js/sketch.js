let move_up = false;
let move_down = false;

function setup(){
	let canvas = createCanvas(400, 400);
	canvas.parent('sketch-holder');
}

function draw(){
	background(0, 0, 0);
	//If no player 2, just draw the first paddle
	if(!player_2_connected){

		let keys_vals = Object.keys(players);
		for(let i = 0; i < keys_vals.length; i++){
			if(keys_vals[i] != 'count'){
				let cur_player_id = keys_vals[i];
				fill(255, 255, 255);
				rect(players[cur_player_id]['x'], players[cur_player_id]['y'], 15, 50);
			}
		}
	} else {
		//Draw paddles
		let keys_vals = Object.keys(players);
		for(let i = 0; i < keys_vals.length; i++){
			if(keys_vals[i] != 'count'){
				let cur_player_id = keys_vals[i];
				let cur_player_num = players[cur_player_id]['num'];
				fill(255, 255, 255);
				if(cur_player_num == 1){
					rect(players[cur_player_id]['x'], players[cur_player_id]['y'], paddle_stats['p1']['xsize'], paddle_stats['p1']['ysize']);
				} else {
					rect(players[cur_player_id]['x'], players[cur_player_id]['y'], paddle_stats['p2']['xsize'], paddle_stats['p2']['ysize']);
				}
			}
		}

		//Draw ball
		fill(255, 255, 255);
		ellipse(ball_location['x'], ball_location['y'], 8, 8);

		//Display score
		try{
			text(ball_location['player_1_score'], 10, 10);
			text(ball_location['player_2_score'], 370, 10);
		}
		catch(e){
			console.log(e)
		}

		//Request paddle movements
		if(move_up){
			your_sock.emit('move_request', {'id': player_id, 'y': -5});
		} else if(move_down){
			your_sock.emit('move_request', {'id': player_id, 'y': 5});
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
    	document.getElementById('chat_button').click();
    }
}

function mousePressed(){
	if(mouseY < 200){
		move_up = true;
	} else if (mouseY > 200){
		move_down = true;
	}

}

function mouseReleased(){
	move_up = false;
	move_down = false;

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