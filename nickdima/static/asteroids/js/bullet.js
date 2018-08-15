//Describes the bullet class

function Bullet(x, y, direction){
    this.location = new Vector(x, y);
    this.direction = direction;
    this.radius = 5;
    this.crashed = false;
    this.fuel = Canvas_Height * 2 / 3;
    this.teleport_offset = 10
    
    this.show = function(){
        ellipse(this.location.x, this.location.y, this.radius, this.radius);
    }
    
    this.update = function(){
        move = this.direction.mult(5)
        this.location = this.location.add(move);
        this.fuel -= move.mag();
    }
    
    this.loop = function(){
        if(this.location.x >= Canvas_Width + this.teleport_offset){
            this.location.x = 0;
        } else if (this.location.x <= 0 - this.teleport_offset){
            this.location.x = Canvas_Width;
        } else if (this.location.y >= Canvas_Height + this.teleport_offset){
            this.location.y = 0;
        } else if (this.location.y <= 0 - this.teleport_offset){
            this.location.y = Canvas_Height;
        }
    }
    
    this.run = function(){
        this.update();
        this.loop();
        this.show();
    }
}