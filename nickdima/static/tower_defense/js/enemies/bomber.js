//These enermies will fly on a horizontal line (fixed y coordinate) and eventually drop a bomb
//that hits the tower

//Choose a random time that they drop a bomb so that sometimes the bomb misses
//The bombs themselves can use the projecticle equations to take the ships velocity and have gravity
//affect it

//When you destroy their bombs, a wave of fire eminates from them, so destroy them or 
//destroy their bombs quickly!!

class Bomber{
    constructor(tower_class){
        this.spwn = bomber_spawn(Canvas_Width, Canvas_Height);
        this.tower_max_x = tower_class.location.x + tower_class.radius;
        this.tower_y = tower_class.location.y;
        this.location = this.spwn[0];
        this.velocity = this.spwn[1];
        this.gravity = this.spwn[2];
        this.speed = 2.5;
        this.radius = 10;
        this.crashed = false;
        this.health = 15;
        this.dmg = 5;
        this.deploy_x = this.calculate_deploy_time(); //fix
        this.deployed = false;
    }
    
    collide(){
        if(this.location.x <= - this.radius){
            this.health = 0;
        }
        
    }
    
    calculate_deploy_time(){
        //At what x position do i need to launch this bomb?
        //x = x0 + v0x*t + 1/2 ax * t**2
        //y = y0 + v0y*t + 1/2 ay * t**2
        
        //t = sqrt((y_target - y_initial)*2 / (gravity))
        //x = x_target - speed*t
        
        let time = Math.sqrt(((this.tower_y - this.location.y) * 2) / this.gravity.y);
        let deploy_x = this.tower_max_x - (-this.speed) * time;
        return deploy_x;
    }
    
    deploy_bomb(enemy_list){
        if(this.location.x <= this.deploy_x && !this.deployed){
            enemy_list.push(new BomberBomb(this.location, this.velocity.normalize().mult(this.speed), this.gravity, this.tower_y));
            this.deployed = true;
        }
    }
    
    update(){
        this.velocity = this.velocity.normalize().mult(this.speed);
        this.location = this.location.add(this.velocity);
    }
    
    show(){
        fill(bomber_enemy_color);
        rect(this.location.x, this.location.y, this.radius, this.radius);
    }
    
    run(enemy_list){
        this.update();
        this.show();
        this.collide();
        this.deploy_bomb(enemy_list);
        
        //This will show their trajectory
        //line(this.location.x + this.velocity.mult(250).x, this.location.y + this.velocity.mult(250).y, this.location.x, this.location.y);
    }
    
}