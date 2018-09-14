let your_sock = false;

//On connect give the server your player_id that will be used to keep track of paddle location

your_sock = io.connect('/stay_alive')   //('http://' + document.domain + ':' + location.port + '/');
your_sock.on('connect', function(){
	console.log('Connection event run');
});

your_sock.on('con_test', function(data){
	console.log(data);
});