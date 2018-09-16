let your_sock = false;
let hero_data = false;
let my_hero_id = false;

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

//Server sends us a unique id so we know which hero we can change
your_sock.on('your_hero_id', function(data){
	my_hero_id = data['you_hero_id']
})