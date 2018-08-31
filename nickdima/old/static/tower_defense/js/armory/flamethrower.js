class FlameThrower{
    constructor(t_loc, t_radi){
        this.height = t_radi * 4 / 5;
        this.width = t_radi / 2;
        this.location = new Vector(t_loc.x + t_radi / 2, t_loc.y);
        this.ready = true;
        this.facing = new Vector(0.5, -0.5);
        this.flame_thrower_length = 50;
        this.bullet_batch = 4; //4
        
        this.frame_count = 0;
        this.fired_max = 5; //5
        this.fired = 0;
        this.cool_down_standard = 2;
        this.cool_down_time = 0;
        this.on_cool_down = false;
    }
    
    cool_down(){
        this.frame_count++;
        if(this.cool_down_time > 1){
            if(this.frame_count % FPS == 0){
                this.cool_down_time--;
            }
        } else if(this.cool_down_time == 1 && this.frame_count % FPS == 0){
            this.cool_down_time = 0;
            this.fired = 0;
        } else if(this.cool_down_time == 0) {
            this.on_cool_down = false;
            this.frame_count = 0;
        }
    }
    
    flame_thrower_rotate(mouse_vec){
        //vec = Vector(mouseX, mouseY)
        let new_loc = this.location.add(new Vector(0, this.height / 2))
        let pointer = mouse_vec.sub(new_loc);
        pointer = pointer.normalize().mult(this.flame_thrower_length);
        pointer = pointer.add(new_loc);
        this.facing = pointer;
    }
    
    fire(mouse_click_vec, bullets){
        if(!this.on_cool_down){
            this.fired++;
            let new_loc = this.location.add(new Vector(0, this.height / 2))
            let dir = this.facing.sub(new_loc).normalize();
            for(let i = 0; i < this.bullet_batch; i++){
                let new_bullet = new FlameThrowerBullets(this.facing, dir);
                bullets.push(new_bullet);
            }
        }
    }
    
    count_fire(){
        if(this.fired == this.fired_max && !this.on_cool_down){
            this.on_cool_down = true;
            this.cool_down_time = this.cool_down_standard;
        }       
    }
    
    
    show(){
        fill(flame_thrower_color);
        
        //draws from the center point
        //base unit of flame_thrower
        triangle(this.location.x, this.location.y, 
                 this.location.x - this.width, this.location.y + this.height,
                this.location.x + this.width, this.location.y + this.height);
        
        //tube part of cannon
        strokeWeight(5);
        line(this.location.x, this.location.y + this.height / 2, this.facing.x, this.facing.y);
        strokeWeight(1);
        
        //tip of flamethrower
        strokeWeight(0);
        fill(flame_thrower_color);
        ellipse(this.facing.x, this.facing.y, 10, 10)
        strokeWeight(1);
    }
    
    run(mouse_vec, bullets){
        this.show();
        this.flame_thrower_rotate(mouse_vec);
        this.count_fire();
    }
    
}