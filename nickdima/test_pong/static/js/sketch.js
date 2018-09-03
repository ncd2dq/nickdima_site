let player_id = false;
let your_sock = false;
let player_2_connected = false;

let move_up = false;
let move_down = false;

let players = {};

function setup(){
	createCanvas(400, 400);

	player_id = Math.round(Math.random() * 5000);
	your_sock = io.connect('http://' + document.domain + ':' + location.port);
	your_sock.on('connect', function(){
		your_sock.emit('player_connect', {'id': player_id});
		console.log('I have connected with ID ' + player_id);
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
		console.log(keys_vals);
		for(let i = 0; i < keys_vals.length; i++){
			if(keys_vals[i] != 'count'){
				let cur_player_id = keys_vals[i];
				players[cur_player_id]['num'] = data_base[cur_player_id]['player_number'];
				players[cur_player_id]['x'] = data_base[cur_player_id]['x'];
				players[cur_player_id]['y'] = data_base[cur_player_id]['y'];
			}
		}
	});
}
function draw(){
	console.log('in drawloop');
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
