class BomberBomb{
    constructor(location, velocity, gravity, tower_y){
        this.location = location;
        this.gravity = gravity;
        this.radius = 10;
        this.velocity = velocity;
        this.tower_y = tower_y;
        this.crashed = false;
        this.health = 8;
        this.dmg = 20;
    }
    
    update(){
        this.velocity = this.velocity.add(this.gravity);
        this.location = this.location.add(this.velocity);
    }
    
    display(){
        fill(255, 255, 255);
        ellipse(this.location.x, this.location.y, this.radius, this.radius)
    }
    
    collide(){
        if(this.location.y >= this.tower_y){
            this.crashed = true;
        }
    }
    
    
    run(){
        this.update();
        this.display();
        this.collide();
    }
}