class Cannon{
    constructor(t_loc, t_radi){
        this.radius = t_radi * 4 / 5;
        this.location = new Vector(t_loc.x + t_radi / 2, t_loc.y + t_radi / 2);
        this.cannon_length = 50;
        this.facing = new Vector(this.location.x + this.cannon_length * 2 / 3, this.location.y - this.cannon_length * 2 / 3);
        
        this.frame_count = 0;
        this.cool_down_standard = 3;
        this.cool_down_time = 0;
        this.on_cool_down = false;
    }
    
    cannon_rotate(mouse_vec){
        //vec = Vector(mouseX, mouseY)
        if(!this.on_cool_down){
            let pointer = mouse_vec.sub(this.location);
            pointer = pointer.normalize().mult(this.cannon_length);
            pointer = pointer.add(this.location);
            this.facing = pointer;
        } else {
            let pointer = mouse_vec.sub(this.location);
            pointer = pointer.normalize().mult(this.cannon_length * 2 / 3);
            pointer = pointer.add(this.location);
            this.facing = pointer;
        }
    }
    
    fire(mouse_click_vec, bullets){
        if(!this.on_cool_down){
            this.on_cool_down = true;
            this.cool_down_time = this.cool_down_standard;
            let dir = this.facing.sub(this.location).normalize();
            let new_bullet = new CannonBullets(this.facing, dir);
            bullets.push(new_bullet);
        }
    }
    
    
    show(){
        fill(cannon_color);
        
        //draws from the center point
        //base unit of cannon
        ellipse(this.location.x, this.location.y, this.radius, this.radius);
        
        //tube part of cannon
        strokeWeight(5);
        line(this.location.x, this.location.y, this.facing.x, this.facing.y);
        strokeWeight(1);
        
    }
    
    cool_down(){
        this.frame_count++;
        if(this.cool_down_time != 0){
            if(this.frame_count % FPS == 0){
                this.cool_down_time--;
            }
        } else {
            this.on_cool_down = false;
            this.frame_count = 0;
        }
        
    }
    
    run(mouse_vec, bullets){
        this.show();
        this.cannon_rotate(mouse_vec);
    }
    
    
}
