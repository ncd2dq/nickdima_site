let your_sock = false;
let hero_data = false;
let my_hero_id = false;
let daylight_data = false;
let resource_nodes_data = false;

//On connect give the server your player_id that will be used to keep track of paddle location

your_sock = io.connect('http://' + document.domain + ':' + location.port + '/stay_alive');
your_sock.on('connect', function(){
	console.log('Connection event run');
});

your_sock.on('con_test', function(data){
	console.log(data);
});

//Recieve data about heros
your_sock.on('hero_data', function(data){
	hero_data = data['hero_data'];
});

your_sock.on('daylight_data', function(data){
	daylight_data = data['daylight_data'];
});

your_sock.on('resource_nodes_data', function(data){
	resource_nodes_data = data['resource_nodes_data'];
});

//Server sends us a unique id so we know which hero we can change
your_sock.on('your_hero_id', function(data){
	if(my_hero_id == false){
		my_hero_id = data['your_hero_id'];
		console.log(data);
		console.log('above is from hero id');
	} else {
		console.log('new player joined');
	}
});

function move(type, dir){
	let packet = {'id': my_hero_id, 'dir': false};
	if(type == 'pressed'){
		if(dir == 'up'){
			packet['dir'] = 'up';
		} else if(dir == 'down'){
			packet['dir'] = 'down';
		} else if(dir == 'right'){
			packet['dir'] = 'right';
		} else if(dir == 'left'){
			packet['dir'] = 'left';
		}
		packet['type'] = true;
		your_sock.emit('move_req', packet)
	} else if(type == 'released'){
		if(dir == 'up'){
			packet['dir'] = 'up';
		} else if(dir == 'down'){
			packet['dir'] = 'down';
		} else if(dir == 'right'){
			packet['dir'] = 'right';
		} else if(dir == 'left'){
			packet['dir'] = 'left';
		}
		packet['type'] = false;
		your_sock.emit('move_req', packet)
	}
}