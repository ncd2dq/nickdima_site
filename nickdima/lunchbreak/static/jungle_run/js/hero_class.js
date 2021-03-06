class Hero{
    constructor(){
        this.animation_index = 0;
        this.animation_max = 11;
        this.running_frame_change_every = 3;
        this.jumping_frame_change_every = 8;
        //power up 
        this.power_up_change_frame_every = 1;
        this.dank_glass = loadImage('http://www.nickdima.com/lunchbreak/static/jungle_run/assets/hero/dankglass.png');
        //end power up
        this.change_frame_every = this.running_frame_change_every;
        this.animation_list = this.create_running_array();
        
        
/*        this.x = 35;
        this.y = Canvas_Height - 190;*/
        
        this.x = 100;
        this.y = Canvas_Height / 4;
        
        
        this.y_standard = Canvas_Height - 190;
        
        this.y_vel = 0;
        this.gravity = 0.5;
        this.max_downward = -12;
        this.jump_vel = 8;
        this.jump_budge = 16;
        
        this.jump_count = 0;
        this.max_jumps = 2;
        
        this.resized_x = 175;
        this.resized_y = 175;
        
        this.possible_surfaces = [];
        
        this.above_zone = false;
        this.fixed_y = Canvas_Height / 3 - (this.resized_y / 4);
        this.fix_y_for_obstacles = 58;
        
        this.was_high_enough = false;
        this.max_speed_reached = false;
        
        //new position when in above zone
        //this.fixed_y and this.fixed_y + (this.resized_y * 5/ 6) - this.fix_y_for_obstacles
        //everything else is the same
    }
    
    create_running_array(){
        let prefix = 'http://www.nickdima.com/lunchbreak/static/jungle_run/assets/hero/run-cycle-inked2_xcf-Frame_';
        let suffix = '__100ms___replace_.png';
        let images = [];
        
        for(let i = 1; i < this.animation_max + 2; i++){
            if(i < 10){
                images.push( loadImage(prefix + '0' + i + suffix) );
            } else {
                images.push( loadImage(prefix + i + suffix)  );
            }
        }
        
        return images;
    }
    
    stand_on(objs){
        this.possible_surfaces = [];
        for(let i = 0; i < objs.length; i++){
            if(this.x + this.resized_x / 3 >= objs[i].x + objs[i].image_blank_space &&
               this.x + this.resized_x / 3 <= objs[i].x - objs[i].image_blank_space + objs[i].resized_x &&
              this.y + this.resized_y * 5 / 6 <= objs[i].y + objs[i].image_blank_space){
                this.possible_surfaces.push(objs[i].y_standard);

            } else if(this.x + this.resized_x * 1.75 / 3 >= objs[i].x + objs[i].image_blank_space &&
               this.x + this.resized_x * 1.75 / 3 <= objs[i].x - objs[i].image_blank_space + objs[i].resized_x &&
                this.y + this.resized_y * 5 / 6 <= objs[i].y + objs[i].image_blank_space){
                this.possible_surfaces.push(objs[i].y_standard);
            }

            
        }
        if(this.possible_surfaces.length == 0){ // if he is above no other objects, change the floor back to the ground level
                this.y_standard = backgroundObject.y_standard;
            } else { //if he is above other objects, change the floor to the highest of the objects he is above
                let highest = Canvas_Height;
                for(let j = 0; j < this.possible_surfaces.length; j++){
                    if(this.possible_surfaces[j] < highest){
                        highest = this.possible_surfaces[j];
                    }
                }
                this.y_standard = highest;
            }
    }
    
    display_dank(){
        if(!this.above_zone){
            let current_image = this.animation_list[this.animation_index];
            image(this.dank_glass, 
                  this.x + (this.resized_x * 1 / 3 + 5), this.y + (this.resized_y * 1 / 4 + 2),
                 35, 15); //resizes the image
        } else {
            let current_image = this.animation_list[this.animation_index];
            image(this.dank_glass, 
                  this.x + (this.resized_x * 1 / 3 + 5), this.fixed_y - this.fix_y_for_obstacles + (this.resized_y * 1 / 4 + 2),
                 35, 15); //resizes the image
        }
    }
    
    update(){
        //THIS IS WHERE THE MAGIC OF UNLIMITED UPWARD MOVEMENT COMES FROM
        
        //If your y position would go higher than a set limit on the screen, create a global_y_offset of how much higher you are relative to that fixed
        //y point. Now, instead of moving the character, move all other objects downward by that much to show relative motion
        
        let top_left_actual = this.y + this.resized_y * 1 / 3; // find real y position of hero
        if(top_left_actual <= this.fixed_y){ //compare it to the fixed position on screen
            global_y_offset = this.fixed_y - (top_left_actual); //find the difference to apply to all objects when drawn
            this.above_zone = true;
        } else {   
            global_y_offset = 0;
            this.above_zone = false;
        }
            
        if(this.y - this.y_vel < this.y_standard){ //when above the current floor, allow him to keep falling
            this.y -= this.y_vel;
            if(this.y_vel > this.max_downward){
                this.y_vel -= this.gravity;
            }
            this.change_frame_every = this.jumping_frame_change_every;
            if(running_sound.isPlaying() == true){
                running_sound.stop();
            }
            
        } else if (this.y - this.y_vel > this.y_standard){
            this.y = this.y_standard;
            this.y_vel = 0;
            this.jump_count = 0;
            if(normal){ //if powerup is running go into frantic mode
                this.change_frame_every = this.running_frame_change_every;
            } else if (!normal){
                this.change_frame_every = this.power_up_change_frame_every;
            }
            if(running_sound.isPlaying() == false){
                running_sound.play();
            }
        } else if (this.y >= this.y_standard){
            this.y = this.y_standard;
            this.y_vel = 0;
            this.jump_count = 0;
            if(normal){ //if powerup is running go into frantic mode
                this.change_frame_every = this.running_frame_change_every;
            } else if (!normal){
                this.change_frame_every = this.power_up_change_frame_every;
            }
            if(running_sound.isPlaying() == false){
                running_sound.play();
            }
            
        } else {
            if(running_sound.isPlaying() == false){
                running_sound.play();
            }
        }
        
    }
    
    jump(){
        if(this.jump_count < this.max_jumps && this.jump_count == 0){
            this.jump_count++;
            this.y -= this.jump_budge;
            this.y_vel += this.jump_vel;
        } else if(this.jump_count == 1){
            this.y_vel = 0;
            this.y -= this.jump_budge * 1.5;
            this.y_vel += this.jump_vel * 1.3;
            this.jump_count++;
        }
        
    }
    
    choose_animation_index(frame){
        //there are 0 - 11 frames (12 total)
        if(frame % this.change_frame_every == 0){
            if(this.animation_index <= this.animation_max - 1){
                this.animation_index++;
            } else {
                this.animation_index = 0;
            }
        }
    }
    
    display(){
        //display an image based on what animation frame
        if(!this.above_zone){
            let current_image = this.animation_list[this.animation_index];
            image(current_image, 
                  this.x, this.y,
                 this.resized_x, this.resized_y); //resizes the image
        } else {
            let current_image = this.animation_list[this.animation_index];
            image(current_image, 
                  this.x, this.fixed_y - this.fix_y_for_obstacles,
                 this.resized_x, this.resized_y); //resizes the image
        }
        
/*        ellipse(this.x + 175/3, this.fixed_y, 5,5);*/
        
        //find hit box
/*        fill(255,255,0);
        if(this.above_zone){
            ellipse(this.x + 175/3, this.fixed_y + (this.resized_y * 5/ 6) - this.fix_y_for_obstacles, 5, 5); // bottom left
            ellipse(this.x + 175 * 1.75 / 3, this.fixed_y + (this.resized_y * 5/ 6) - this.fix_y_for_obstacles, 5, 5); //bottom right
            ellipse(this.x + 175 / 3, this.fixed_y, 5, 5); // top left
            ellipse(this.x + 175 * 1.75 / 3, this.fixed_y, 5, 5); //top right
        } else if(!this.above_zone){
            fill(255, 0, 0);
            ellipse(this.x + 175 / 3, this.y + this.resized_y * 5 / 6, 5, 5); // bottom left
            ellipse(this.x + 175 * 1.75 / 3, this.y + this.resized_y * 5 / 6, 5, 5); //bottom right
            ellipse(this.x + 175 / 3, this.y + this.resized_y * 1 / 3, 5, 5); // top left
            ellipse(this.x + 175 * 1.75 / 3, this.y + this.resized_y * 1 / 3, 5, 5); //top right
        }*/
    }
    
    collect_coins(coins_list){
        for(let i = 0; i < coins_list.length; i++){
            
            //Establish coin vertices
            let c_tr, c_br, c_bl, c_tl;
            c_tr = [coins_list[i].x + coins_list[i].resized_x * 2 / 3, coins_list[i].y + coins_list[i].resized_y * 1 / 5 + global_y_offset];
            c_br = [coins_list[i].x + coins_list[i].resized_x * 2 / 3, coins_list[i].y + coins_list[i].resized_y * 4 / 5 + global_y_offset];
            c_bl = [coins_list[i].x + coins_list[i].resized_x / 3, coins_list[i].y + coins_list[i].resized_y * 4 / 5 + global_y_offset];
            c_tl = [coins_list[i].x + coins_list[i].resized_x / 3, coins_list[i].y + coins_list[i].resized_y * 1 / 5 + global_y_offset];
            
            let c_verts = [c_tr, c_br, c_bl, c_tl];
            //Establish hero vertices
            let h_tr, h_br, h_bl, h_tl;
            if(this.above_zone){
                h_tr = [this.x + 175 * 1.75 / 3, this.fixed_y];
                h_br = [this.x + 175 * 1.75 / 3, this.fixed_y + (this.resized_y * 5/ 6) - this.fix_y_for_obstacles];
                h_bl = [this.x + 175/3, this.fixed_y + (this.resized_y * 5/ 6) - this.fix_y_for_obstacles];
                h_tl = [this.x + 175 / 3, this.fixed_y];
            } else {
                h_tr = [this.x + 175 * 1.75 / 3, this.y + this.resized_y * 1 / 3];
                h_br = [this.x + 175 * 1.75 / 3, this.y + this.resized_y * 5 / 6];
                h_bl = [this.x + 175 / 3, this.y + this.resized_y * 5 / 6];
                h_tl = [this.x + 175 / 3, this.y + this.resized_y * 1 / 3];   
            }
            
            //check if inside
            for(let j = 0; j < c_verts.length; j++){
                if(c_verts[j][0] <= h_br[0] && c_verts[j][0] >= h_bl[0] &&
                  c_verts[j][1] <= h_bl[1] && c_verts[j][1] >= h_tl[1]){
                    coins_list[i].collected = true;
                    break
                }
            }
        }

    }
    
    high_enough_to_die(){
/*        if(this.above_zone && global_y_offset >= 86){
            this.ready_to_die = true;
            console.log(global_y_offset, this.y_vel);
        }*/

        //y_vel is at terminal velocity
        //he went from was high enough
        //the next time he got to y_vel = 0 he was on ground floor
        
        //groundfloor = level 0
        //if you were on level 2 or higher, if the next time your y_vel = 0, you are on the ground floor, it means you fell from that level and are dead
        //when you this.y_vel == 0 it resets the falling_fast_enough and 
        if(this.above_zone && global_y_offset >= 210){
            this.was_high_enough = true;
        }
        
        if(this.y_vel <= this.max_downward){
            this.max_speed_reached = true;
        }
        
        
        if(this.y_vel == 0){
            if(this.y == 242 && this.max_speed_reached && this.was_high_enough){ //ground level
                hero_health = 0;
                gState.game_over = true;
                gState.fell = true;
                console.log('You fell to your death');
            } else {
                this.was_high_enough = false;
                this.max_speed_reached = false;
            }
        }
    }
    
    run(frame, objs, coins_list){
        this.update();
        this.choose_animation_index(frame);
        this.display();
        if(!normal){
            this.display_dank();
        }
        this.stand_on(objs);
        this.collect_coins(coins_list);
        this.high_enough_to_die();
    }
    
}