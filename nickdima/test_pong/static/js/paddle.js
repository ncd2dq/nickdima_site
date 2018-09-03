class YourPaddle{
	constructor(x, y, id){
		this.id = id;
		this.x = x;
		this.y = y;
		this.height = 15;
		this.width = 50;

		this.sock = io.connect('http://' + document.domain + ':' + location.port);
	}

	send_move(direction){
		let data = {'id': this.id};
		if(direction == 'up'){
			data['y_req'] = -10;
			this.sock.emit('move_paddle', data);
		} else if(direction == 'down'){
			data['y_req'] = 10;
			this.sock.emit('move_paddle', data);
		}
	}

	recv_update(x_update, y_update){
		this.x += x_update;
		this.y += y_update;
	}

	show(){
		rect(this.x, this.y, this.width, this.height);
	}
}
