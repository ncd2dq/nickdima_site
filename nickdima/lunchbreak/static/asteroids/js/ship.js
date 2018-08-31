//Describes the spaceship class
function SpaceShip(){
    this.tip_x = 300;
    this.tip_y = 300;
    this.ship_momentum = new Vector(0, 0);
    this.ship_acceleration = new Vector(0,0);
    this.crashed = false;
    this.boosting = false;
    this.forward = true;
    this.gravity_loss = 0.03;
    
    this.shooting = false;
    this.fire_rate_frame = 0;
    
    this.teleport_offset = Ship_Height;
    this.destination_offset = Ship_Height / 3;
    
    this.ready_gun_1 = true;
    
    this.create_vertices = function(tip_x, tip_y){
        //Returns Trangle Vertices: Tip, BL, BR as tuples in an array
        let BL_x = tip_x - Ship_Radius;
        let BL_y = tip_y + Ship_Height;
        let BR_x = tip_x + Ship_Radius;
        let BR_y = tip_y + Ship_Height;
        let Back_Ref_x = tip_x;
        let Back_Ref_y = tip_y + Ship_Height;
        let center_x = tip_x;
        let center_y = tip_y + Ship_Height / 2;
        let final_points = [[tip_x, tip_y],
                           [BL_x, BL_y], 
                           [BR_x, BR_y],
                            [Back_Ref_x, Back_Ref_y],
                           [center_x, center_y]];
        
        return final_points;
    }
    
    //All of the ships other point are stored in this list
    this.ship_vertices = this.create_vertices(this.tip_x, this.tip_y);
    
    this.show = function(){
        //Draw body of ship
        triangle(this.ship_vertices[0][0], this.ship_vertices[0][1],
                this.ship_vertices[1][0], this.ship_vertices[1][1],
                this.ship_vertices[2][0], this.ship_vertices[2][1]);
        
        //Draw ship guns
        let tip = new Vector(this.ship_vertices[0][0], this.ship_vertices[0][1]);
        let BL = new Vector(this.ship_vertices[1][0], this.ship_vertices[1][1]);
        let BR = new Vector(this.ship_vertices[2][0], this.ship_vertices[2][1]);
        
        let gun_1_base = tip.mid_point(BL);
        let gun_2_base = tip.mid_point(BR);
        
        //The base is the half way point on the triangle, and their length is dependent
        //on the way the ship is facing so that the   y rotate correctly
        let ship_facing = this.find_ship_facing_direction();
        
        if(this.ready_gun_1 == true){
            var gun_1_tip = gun_1_base.add(ship_facing.mult(13));
            var gun_2_tip = gun_2_base.add(ship_facing.mult(8));     
        } else {
            var gun_1_tip = gun_1_base.add(ship_facing.mult(8));
            var gun_2_tip = gun_2_base.add(ship_facing.mult(13));  
        }

        
        strokeWeight(2);
        line(gun_1_base.x, gun_1_base.y, gun_1_tip.x, gun_1_tip.y);
        line(gun_2_base.x, gun_2_base.y, gun_2_tip.x, gun_2_tip.y);
        
        this.gun_1_tip = gun_1_tip;
        this.gun_2_tip = gun_2_tip;
        
    }
    
    this.rotate = function(theta){
        //Remove center of triangle, do rotation, add center back in
        let convFactor = Math.PI / 180;
        let new_vertices = [];
        for(let i = 0; i < this.ship_vertices.length; i++){
            cur_x = this.ship_vertices[i][0];
            cur_y = this.ship_vertices[i][1];
            //Remove Center
            cur_x -= this.tip_x;
            cur_y -= this.tip_y + (Ship_Height / 2);
            new_x = cur_x * Math.cos(theta * convFactor) - cur_y * Math.sin(theta * convFactor);
            new_y = cur_x * Math.sin(theta * convFactor) + cur_y * Math.cos(theta * convFactor);
            //Add Center Back In
            new_x += this.tip_x;
            new_y += this.tip_y - (Ship_Height / 2);
            new_vertices.push([new_x, new_y]);
        }
        this.ship_vertices = new_vertices;
        //this.tip_x = new_vertices[0][0];
        //this.tip_y = new_vertices[0][1];
    }
    
    this.find_ship_facing_direction = function(){
        //Modify the BL point to be directly behind the tip then find
        //The vector between them
        //Then get that vectors unit direction
        let tip_x = this.ship_vertices[0][0];
        let tip_y = this.ship_vertices[0][1];
        let Back_Ref_x = this.ship_vertices[3][0];
        let Back_Ref_y = this.ship_vertices[3][1];
        
        back_vector = new Vector(Back_Ref_x, Back_Ref_y);
        tip_vector = new Vector(tip_x, tip_y);
        let direction = tip_vector.sub(back_vector);
        direction = direction.unit_direction();
        
        return direction;
    }
    
    this.shoot = function(bullet_list){
        if (this.shooting){
            if(this.fire_rate_frame % 6 == 0){
                
                if(this.ready_gun_1 == true){
                    direction = this.find_ship_facing_direction();
                    new_bullet = new Bullet(this.gun_1_tip.x, this.gun_1_tip.y, direction);
                    this.ready_gun_1 = false;
                } else {
                    direction = this.find_ship_facing_direction();
                    new_bullet = new Bullet(this.gun_2_tip.x, this.gun_2_tip.y, direction);
                    this.ready_gun_1 = true;
                }
                bullet_list.push(new_bullet);
            }
        this.fire_rate_frame++;
        }
    }
    
    this.loop_position = function(){
        center_x = this.tip_x;
        center_y = this.tip_y + (Ship_Height / 2);
        let loop = false;
        if(center_x >= Canvas_Width + this.teleport_offset){
            loop = true;
            this.tip_x = 0 - this.destination_offset;
        } else if(center_x <= 0 - this.teleport_offset){
            loop = true; 
            this.tip_x = Canvas_Width + this.destination_offset;
        } else if(center_y >= Canvas_Height + this.teleport_offset + (Ship_Height / 2)){
            loop = true; 
            this.tip_y = 0 - this.destination_offset - Ship_Height;
            //PROBLEM IS HERE
        } else if(center_y <= 0 - this.teleport_offset){
            loop = true; 
            this.tip_y = Canvas_Height + this.destination_offset;
        }
        if (loop == true){
            
            this.ship_vertices = this.create_vertices(this.tip_x, this.tip_y);
        }
                  
        
    }
    
    this.collide = function(asteroid_list, buffer=Ship_Height){
        
        //ellipse(this.ship_vertices[4][0], this.ship_vertices[4][1], buffer * 1.5, buffer * 1.5); // For debugging - shows range that it calculates vertices collide
        
        for(let i = 0; i < asteroid_list.length; i++){
            if( sqrt(Math.pow((asteroid_list[i].x - this.ship_vertices[4][0]), 2) + 
                     Math.pow((asteroid_list[i].y - this.ship_vertices[4][1]), 2)) < buffer * 1.5 ){ // Only check collision with all vertices if asteroid is within certain radius
               
                let right_side = Math.pow(asteroid_list[i].radius, 2) / 3;
                for(let j = 0; j < this.ship_vertices.length; j++){
                    try{
                        let left_side = Math.pow((this.ship_vertices[j][0] - asteroid_list[i].x), 2) + Math.pow((this.ship_vertices[j][1] - asteroid_list[i].y), 2);
                        if(left_side < right_side){
                            this.crashed = true;  
                        }
                    }
                    catch(err){
                        //for some reason it says cannot read property x of undefined on line 155 sometimes
                        console.log(err);
                    }
                }
            }
        }
    }
    
    this.update = function(){
        this.ship_momentum = this.ship_momentum.mult((1 - this.gravity_loss));
        this.ship_momentum = this.ship_momentum.add(this.ship_acceleration);
        this.tip_x += this.ship_momentum.x;
        this.tip_y += this.ship_momentum.y;
        this.ship_acceleration = new Vector(0, 0);
    }
    
    this.boost = function(acceleration_vector){
        acceleration_vector = acceleration_vector.mult(0.25)
        if(this.forward){
            acceleration_vector = acceleration_vector.mult(-1);
        }
        if (this.boosting){
            this.ship_acceleration = acceleration_vector;              
        }
    }
    
    this.run = function(theta, asteroid_list, bullet_list){
        this.boost(acceleration_vector);
        this.shoot(bullet_list);
        this.ship_vertices = this.create_vertices(this.tip_x, this.tip_y);
        this.rotate(theta);
        this.collide(asteroid_list);
        this.update();
        this.loop_position();
        this.show();
    }
}
