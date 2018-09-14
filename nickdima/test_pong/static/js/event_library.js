let player_id = false;
let your_sock = false;
let player_2_connected = false;
let players = {};
let ball_location = {'x': 200, 'y': 200, 'x_s': 5, 'y_s': 5, 'player_1_score': 0, 'player_2_score': 0};
let paddle_stats = false;

//Assign a the player a random playerID from 1 - 5000
player_id = Math.round(Math.random() * 5000);


//On connect give the server your player_id that will be used to keep track of paddle location
your_sock = io.connect('http://' + document.domain + ':' + location.port + '/pong');
your_sock.on('connect', function(){
	your_sock.emit('player_connect', {'id': player_id});
	console.log('I have connected with ID ' + player_id);
});


//Server tells us if we are player 1 or player 2 and our paddle location is set
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


//When all players have joined, the server will re-ping all players with a final list of location data
//to ensure client and server are synced
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
});

//recieve paddle information from server
your_sock.on('recv_paddle_stats', function(data){
	if(paddle_stats != false){
		paddle_stats = data;
	} else {
		paddle_stats = data;
		player_2_connected = true;
	}
});


//Recieve new paddle locations
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


//Recieve ball locations
your_sock.on('recieve_ball_loc', function(ball){
	ball_location = ball;
});


//Player disconnect
your_sock.on('scram', function(data){
	console.log(data);
	get_out();

});


//Chat Functionality
function add_chat(mes){
	let elm = document.getElementById('chatbox');
	elm.innerHTML = mes['chat'] + '<br>' + elm.innerHTML;
}

your_sock.on('recv_chat', function(data){
	add_chat(data);
});


//Socket testing
your_sock.on('testing', function(data){
	console.log(data);
	console.log('here');
});