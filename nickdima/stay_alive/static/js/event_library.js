let your_sock = false;

//On connect give the server your player_id that will be used to keep track of paddle location

your_sock = io.connect('http://' + document.domain + ':' + location.port + '/');
your_sock.on('connect', function(){
	console.log('Connection event run');
	your_sock.emit('test_con', {'hello':'hi'})
});