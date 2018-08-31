class Vehicle{
    constructor(land_vehicle, moto, file_path){
        //State variables
        this.type = 'vehicle';
        this.land_vehicle = land_vehicle;
        this.moto = moto;
        this.occupied = false;
        this.direction = 'right';
        this.moving = false;
        
        //Offset positions (compared to the central point) so that you only need to update the central point location
        this.tire_left_x_offset = 0;  
        this.tire_left_y_offset = 0;
        this.tire_right_x_offset = 0;
        this.tire_right_y_offset = 0;
        this.body_x_offset = 0;
        this.body_y_offset = 0;
        this.body_x_offset_s = 0; //currently being unused -- but could be used for a tank when it shoots, the body recoils backwards and needs to reset
        this.body_y_offset_s = 0;
        this.hero_x_offset = 0;
        this.hero_y_offset = 0;
        this.wheel_rotation_offset = 0; //Translate the center coordinate point to the middle of the tire (compared to the top left point)
        
        //Central Point
        this.x = 0;
        this.y = 0;
        this.x_vel = 0;
        this.y_vel = 0;
        this.x_speed = 0;
        this.y_speed = 0;
        
        //Image Sizes
        this.tire_left_x_size = 0;
        this.tire_left_y_size = 0;
        this.tire_right_x_size = 0;
        this.tire_right_y_size = 0;
        this.body_x_size = 0;
        this.body_y_size = 0;
        
        //Hold sprite pictures + animation speed
        this.animation_dict = this.load_animation_dictionary(file_path);
        this.animation_index = 0;
        this.animation_index_max = 4;
        this.idle_animation_speed = 5;
        this.idle_movement = 5;
        this.idle_jerk = 1.2;
        this.wheel_rotation_speed = 0.005;
        
        this.ground_y_punk = 0;
        this.ground_y_industrial = 0;
        this.boarding_threshold = 0; //How close to the objects center does the hero need to board the vehicle
        this.side_scroll_begins = Canvas_Width * 3 / 4;
    }
    
    load_animation_dictionary(file_path){
        let prefix = 'http://www.nickdima.com/static/highway_chase/assets/vehicles';
        let animation_dict = {'body': [], 'tire': []};
        
        if(this.land_vehicle == true){
            animation_dict['body'].push(loadImage(prefix + file_path + '/body.png'));
            animation_dict['tire'].push(loadImage(prefix + file_path + '/tire.png'));
        } else {
            //file_path = [image location path, number of images]
            for(let i = 0; i < file_path[1]; i++){
                animation_dict['body'].push(loadImage(prefix + file_path[0] + '/body' + i + '.png'));
            }
        }
        return animation_dict;
    }
    
    _apply_y_vel(){
        //Determine if going up or down will bring you offscreen or underground
        if(BackGround.name == 'Punk'){
            if(this.y_vel > 0 && this.y + this.y_vel < this.ground_y_punk || (this.y_vel < 0 && this.y - this.y_vel > 15)){
                let hero_center = hero.find_center();
                this.y += this.y_vel;
                hero.y = this.y - hero_center[3] + this.hero_y_offset;

            } else if (this.y_vel > 0 && this.y + this.y_vel >= this.ground_y_punk){
                this.y = this.ground_y_punk;
            }
        } else if(BackGround.name == 'Industrial'){
            if(this.y_vel > 0 && this.y + this.y_vel < this.ground_y_industrial || (this.y_vel < 0 && this.y - this.y_vel > 15)){
                let hero_center = hero.find_center();
                this.y += this.y_vel;
                hero.y = this.y - hero_center[3] + this.hero_y_offset;

            } else if (this.y_vel > 0 && this.y + this.y_vel >= this.ground_y_industrial){
                this.y = this.ground_y_industrial;
            }
        }
        
    }
    
    move(direction){
        if(direction == 'left'){
            this.x_vel = -occupied_vehicle.template.x_speed;
            this.direction = 'left';
            this.moving = true;
        } else if (direction == 'right'){
            this.x_vel = occupied_vehicle.template.x_speed;
            this.direction= 'right';
            this.moving = true;
        } else if (direction == 'up' || direction == 'down'){
            this.fly(direction);
        } else if (direction == 'stop'){
            this.x_vel = 0;
            this.moving = false;
        } else if (direction == 'stop_y'){ //stop up and down are split out so that you can keep flying in the x/y direction while stopping in the other
            this.y_vel = 0;
        }
    }
    
    update(){
        if(this.x + this.x_vel >= this.side_scroll_begins){
            BackGround.side_scroll();
            this._apply_y_vel();
            
        } else {
            let hero_center = hero.find_center();
            this.x += this.x_vel;
            hero.x = this.x - hero_center[2] + this.hero_x_offset;
            this._apply_y_vel();
        }
    }
    
    _change_background_speed(){
            if(BackGround.name == 'Punk'){
                BackGround.speed = this.x_speed * 2 / 3;
                BackGround.speed1 = this.x_speed * 2 / 3 * 1.2;
                BackGround.speed2 = this.x_speed * 2 / 3 * 1.2 * 1.2;
            } else if(BackGround.name == 'Industrial'){
                BackGround.speed = this.x_speed * 2 / 3;
            }
    }
    
    be_boarded(hero_center){
        //Check x + y with boarding threshold to see if hero center is within boarding threshold square
        if(hero_center[0] >= this.x - this.boarding_threshold && hero_center[0] <= this.x + this.boarding_threshold){
            if(hero_center[1] >= this.y - this.boarding_threshold && hero_center[1] <= this.y + this.boarding_threshold){
                //First reposition the hero at the vehicles center points
                hero.x = this.x - hero_center[2] + this.hero_x_offset;
                hero.y = this.y - hero_center[3] + this.hero_y_offset;
                this.occupied = true;
                this._change_background_speed();
                return true;
            }
        }
        return false;
    }
    
    fly(direction, speed){
        if(!this.land_vehicle){
            if(direction == 'up'){
                this.y_vel = -this.y_speed;
            } else if(direction == 'down') {
                this.y_vel = this.y_speed;
            }
        }
    }
    
    exit(){
        this.occupied = false;
        this.body_x_offset = this.body_x_offset_s;
        this.body_y_offset = this.body_y_offset_s;
        this.moving = false;
        this.x_vel = 0;
        this.y_vel = 0;
        BackGround.reset_speed();
    }
    
    animation(frame, no_hero_idle){
        //No hero idle means the vehicle is idling without a hero in it (so don't alter any of the heros positions)
        if(no_hero_idle){
            if(frame % this.idle_animation_speed == 0){
                if(this.animation_index == 0){
                    this.body_y_offset += this.idle_movement;
                } else if (this.animation_index == 1){
                    this.body_y_offset += this.idle_movement * this.idle_jerk;

                } else if (this.animation_index == 2){
                    this.body_y_offset -= this.idle_movement;

                } else if (this.animation_index == 3){
                    this.body_y_offset -= this.idle_movement * this.idle_jerk;
                }
            }
        } else {
            if(frame % this.idle_animation_speed == 0){
                if(this.animation_index == 0){
                    this.body_y_offset += this.idle_movement;
                    hero.y += this.idle_movement;
                    
                } else if (this.animation_index == 1){
                    this.body_y_offset += this.idle_movement * this.idle_jerk;
                    hero.y += this.idle_movement * this.idle_jerk;
                    
                } else if (this.animation_index == 2){
                    this.body_y_offset -= this.idle_movement;
                    hero.y -= this.idle_movement;
                    
                } else if (this.animation_index == 3){
                    this.body_y_offset -= this.idle_movement * this.idle_jerk;
                    hero.y -= this.idle_movement * this.idle_jerk;
                }
            }
        }
        
        //Advance the animation frame
        if(this.animation_index < this.animation_index_max - 1){
            this.animation_index++;
        } else {
            this.animation_index = 0;
        }
        
    }
    
    wheel_rotation(){
        if(this.direction == 'right'){
            push();
            translate(this.x + this.tire_left_x_offset + this.wheel_rotation_offset, this.y + this.tire_left_y_offset + this.wheel_rotation_offset);
            rotate(degrees(frameCount * this.wheel_rotation_speed));
            image(this.animation_dict['tire'][0], -this.wheel_rotation_offset, -this.wheel_rotation_offset, this.tire_left_x_size, this.tire_left_y_size);
            pop();
        
            push();
            translate(this.x + this.tire_right_x_offset + this.wheel_rotation_offset, this.y + this.tire_right_y_offset + this.wheel_rotation_offset);
            rotate(degrees(frameCount * this.wheel_rotation_speed));
            image(this.animation_dict['tire'][0], -this.wheel_rotation_offset, -this.wheel_rotation_offset, this.tire_right_x_size, this.tire_right_y_size);
            pop();
        } else {
            push();
            translate(this.x + this.tire_left_x_offset + this.wheel_rotation_offset, this.y + this.tire_left_y_offset + this.wheel_rotation_offset);
            rotate(degrees(-frameCount * this.wheel_rotation_speed));
            image(this.animation_dict['tire'][0], -this.wheel_rotation_offset, -this.wheel_rotation_offset, this.tire_left_x_size, this.tire_left_y_size);
            pop();
        
            push();
            translate(this.x + this.tire_right_x_offset + this.wheel_rotation_offset, this.y + this.tire_right_y_offset + this.wheel_rotation_offset);
            rotate(degrees(-frameCount * this.wheel_rotation_speed));
            image(this.animation_dict['tire'][0], -this.wheel_rotation_offset, -this.wheel_rotation_offset, this.tire_right_x_size, this.tire_right_y_size);
            pop();
        }
    }
    
    display_wheels(){
        if(this.moving){
            this.wheel_rotation();
        } else { 
            image(this.animation_dict['tire'][0], this.x + this.tire_left_x_offset, this.y + this.tire_left_y_offset, this.tire_left_x_size, this.tire_left_y_size);
            image(this.animation_dict['tire'][0], this.x + this.tire_right_x_offset, this.y + this.tire_right_y_offset, this.tire_right_x_size, this.tire_right_y_size);
        } 
    }
    
    display(occupied){
        if(occupied){
            if(this.land_vehicle){
                hero.display();
            }
        }
        if(this.land_vehicle == true){
            if(this.moto == true){ //Motorcycle wheels are behind the body
                this.display_wheels();
                image(this.animation_dict['body'][0], this.x + this.body_x_offset, this.y + this.body_y_offset, this.body_x_size, this.body_y_size);
                
            } else { //Non-motorcycle wheels are in front of the body
                image(this.animation_dict['body'][0], this.x + this.body_x_offset, this.y + this.body_y_offset, this.body_x_size, this.body_y_size);
                this.display_wheels();
            }
        } else { //Air vehicles do not have wheels
            image(this.animation_dict['body'][0], this.x + this.body_x_offset, this.y + this.body_y_offset, this.body_x_size, this.body_y_size);
        }
    } 
}