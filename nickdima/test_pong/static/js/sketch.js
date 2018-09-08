let player_id = false;
let your_sock = false;
let player_2_connected = false;


let move_up = false;
let move_down = false;

let players = {};

let ball_location = {'x': 200, 'y': 200, 'x_s': 5, 'y_s': 5, 'player_1_score': 0, 'player_2_score': 0};


function setup(){
	let canvas = createCanvas(400, 400);
	canvas.parent('sketch-holder');

	player_id = Math.round(Math.random() * 5000);
	your_sock = io.connect('http://' + document.domain + ':' + location.port + '/');  //io.connect('');  //io.connect('http://' + document.domain + ':' + location.port);
	your_sock.on('connect', function(){
		your_sock.emit('player_connect', {'id': player_id});
		console.log('I have connected with ID ' + player_id);
	});

	your_sock.on('testing', function(data){
		console.log(data);
		console.log('here');
	});

	your_sock.on('scram', function(data){
		console.log(data);
		get_out();

	});

	function add_chat(mes){
		let elm = document.getElementById('chatbox');
		elm.innerHTML = mes['chat'] + '<br>' + elm.innerHTML;
	}

	your_sock.on('recv_chat', function(data){
		add_chat(data);
	});

	your_sock.on('what_player', function(data){
		console.log('recieved player number ' + data['player_number']);
		if(data['id'] == player_id){
			players[player_id] = {};
			if(data['player_number'] == 1){
				players[player_id]['num'] = data['player_number'];
				players[player_id]['x'] = 10;
				players[player_id]['y'] = 50;
			} else {
				players[player_id]['num'] = data['player_number'];
				players[player_id]['x'] = 375;
				players[player_id]['y'] = 50;
			}
		}
	});

	your_sock.on('all_players', function(data_base){
		let keys_vals = Object.keys(data_base);
		for(let i = 0; i < keys_vals.length; i++){
			if(keys_vals[i] != 'count'){
				let cur_player_id = keys_vals[i];
				console.log('all players function');
				console.log(players);
				console.log(cur_player_id);
				players[cur_player_id] = {};
				players[cur_player_id]['num'] = data_base[cur_player_id]['player_number'];
				players[cur_player_id]['x'] = data_base[cur_player_id]['x'];
				players[cur_player_id]['y'] = data_base[cur_player_id]['y'];
			}
		}
		player_2_connected = true;
	});


	your_sock.on('all_info', function(data_base){
		let keys_vals = Object.keys(data_base);
		for(let i = 0; i < keys_vals.length; i++){
			if(keys_vals[i] != 'count'){
				let cur_player_id = keys_vals[i];
				players[cur_player_id]['num'] = data_base[cur_player_id]['player_number'];
				players[cur_player_id]['x'] = data_base[cur_player_id]['x'];
				players[cur_player_id]['y'] = data_base[cur_player_id]['y'];
			}
		}

	});

	your_sock.on('recieve_ball_loc', function(ball){
		ball_location = ball;
	});

	
}
function draw(){
	background(0, 0, 0);
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
		let keys_vals = Object.keys(players);
		for(let i = 0; i < keys_vals.length; i++){
			if(keys_vals[i] != 'count'){
				let cur_player_id = keys_vals[i];
				fill(255, 255, 255);
				rect(players[cur_player_id]['x'], players[cur_player_id]['y'], 15, 50);
			}
		}

		fill(255, 255, 255);
		ellipse(ball_location['x'], ball_location['y'], 8, 8);

		try{
			text(ball_location['player_1_score'], 10, 10);
			text(ball_location['player_2_score'], 370, 10);
		}
		catch(e){
			console.log(e)
		}

		if(move_up){
			your_sock.emit('move_request', {'id': player_id, 'y': -5});
		} else if(move_down){
			your_sock.emit('move_request', {'id': player_id, 'y': 5});
		}

		//the magic but currently a client is acting as the server
		//if(players[player_id]['num'] == 1){
		//	move_ball(ball_location);
		//}

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


/*
function move_ball(ball_loc){

	ball_loc['x'] += ball_loc['x_s'];
	ball_loc['y'] += ball_loc['y_s'];

	//paddle is 15 long 50 tall

	if(ball_loc['y'] > 400){
		ball_loc['y_s'] *= -1;
	} else if (ball_loc['y'] < 0){
		ball_loc['y_s'] *= -1;
	} else if (ball_loc['x'] > 400 || ball_loc['x'] < 0){
		ball_loc = {'x': 200, 'y': 200, 'x_s': 6, 'y_s': 6};
	}

	let keys_vals = Object.keys(players);
	for(let i = 0; i < keys_vals.length; i++){
		if(keys_vals[i] != 'count'){
			let cur_player_id = keys_vals[i];

			let x = players[cur_player_id]['x'];
			let y = players[cur_player_id]['y'];

			if(ball_loc['x'] > players[cur_player_id]['x'] && ball_loc['x'] < players[cur_player_id]['x'] + 15){
				if(ball_loc['y'] > players[cur_player_id]['y'] && ball_loc['y'] < players[cur_player_id]['y'] + 50){
					ball_loc['x_s'] *= -1;
				}
			}
		}
	}

	your_sock.emit('send_ball_loc', ball_loc);

}
*/