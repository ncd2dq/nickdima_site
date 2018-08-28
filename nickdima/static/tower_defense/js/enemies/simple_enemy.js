class SimpleEnemy{
    constructor(tower_class){
        this.spwn = random_spawn(Canvas_Width, Canvas_Height, Spawn_Radius, tower_class);
        this.tower_max_x = tower_class.location.x + tower_class.radius;
        this.location = this.spwn[0];
        this.speed = 5;
        this.velocity = this.spwn[1];
        this.radius = 10;
        this.crashed = false;
        this.health = 10;
        this.dmg = 5;
    }
    
    collide(){
        if(this.location.x <= this.tower_max_x){
            this.crashed = true;
        }
        
        
    }
    
    update(){
        this.velocity = this.velocity.normalize().mult(this.speed);
        this.location = this.location.add(this.velocity);
    }
    
    show(){
        fill(simple_enemy_color);
        ellipse(this.location.x, this.location.y, this.radius, this.radius);
    }
    
    run(){
        this.update();
        this.show();
        this.collide();
        
        //This will show their trajectory
        //line(this.location.x + this.velocity.mult(250).x, this.location.y + this.velocity.mult(250).y, this.location.x, this.location.y);
    }
    
    
}

// function random_spawn(canvas_w, canvas_h, spwn_radius, tower_class)