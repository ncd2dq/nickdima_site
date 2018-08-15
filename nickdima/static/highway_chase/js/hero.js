class Hero{
    constructor(){
        this.state = 'idle_right'; //Used to determine what sprite images to display
        this.facing = 'right'; //Used to determine what orientation of sprite images to display
        this.animation_dict = this.create_animation_dictionary(); //Load all sprite images
        this.animation_index = 0; //Keep track of what sprite image is being displayed in its respective animation loop
        this.animation_speed = 5; //Lower numbers mean the sprite will animate faster
        this.occupied_vehicle = false; //Determine if sprite is in a vehicle or not
        this.jump1 = false;
        this.jump2 = false;
        this.x = 20;
        this.y = BackGround.hero_floor;
        this.y_vel = 0;
        this.gravity = 1;
        this.y_standard = BackGround.hero_floor;
        this.run_speed = 3;
        this.side_scroll_beings = Canvas_Width * 2 / 3;
        this.max_health = 15;
        this.health = this.max_health;
    }
    
    create_animation_dictionary(){
        //Load all hero sprite images and create a dictionary containing lists of the images in chronological order for animation
        let animation_dict = {};
        let prefix_right = 'assets/hero/ellie frames/right/Ellie frame_';
        let prefix_left = 'assets/hero/ellie frames/left/Ellie frame_';
        let suffix = '.png';
        
        animation_dict['aim_right'] =   [];
        animation_dict['death_right'] = [];
        animation_dict['idle_right'] =  [];
        animation_dict['run_right'] =   [];
        animation_dict['shoot_right'] = [];
        animation_dict['aim_left'] =    [];
        animation_dict['death_left'] =  [];
        animation_dict['idle_left'] =   [];
        animation_dict['run_left'] =    [];
        animation_dict['shoot_left'] =  [];
        
        //RIGHT FACING
        //Load Aim Images
        for(let i = 0; i < 8; i++){
            animation_dict['aim_right'].push(loadImage(prefix_right + 'aim_' + i + suffix));
        }
        //Load Death Images
        for(let i = 0; i < 8; i++){
            animation_dict['death_right'].push(loadImage(prefix_right + 'death_' + i + suffix));
        }
        //Load Idle Images
        for(let i = 0; i < 4; i++){
            animation_dict['idle_right'].push(loadImage(prefix_right + 'idle_' + i + suffix));
        }
        //Load Run Images
        for(let i = 0; i < 14; i++){
            if( i < 10){
                animation_dict['run_right'].push(loadImage(prefix_right + 'run_0' + i + suffix));
            } else {
                animation_dict['run_right'].push(loadImage(prefix_right + 'run_' + i + suffix));
            }
        }
        //Load Shoot Images
        for(let i = 0; i < 4; i++){
            animation_dict['shoot_right'].push(loadImage(prefix_right + 'shoot_' + i + suffix));
        }
        
        //LEFT FACING
        //Load Aim Images
        for(let i = 0; i < 8; i++){
            animation_dict['aim_left'].push(loadImage(prefix_left + 'aim_' + i + suffix));
        }
        //Load Death Images
        for(let i = 0; i < 8; i++){
            animation_dict['death_left'].push(loadImage(prefix_left + 'death_' + i + suffix));
        }
        //Load Idle Images
        for(let i = 0; i < 4; i++){
            animation_dict['idle_left'].push(loadImage(prefix_left + 'idle_' + i + suffix));
        }
        //Load Run Images
        for(let i = 0; i < 14; i++){
            if( i < 10){
                animation_dict['run_left'].push(loadImage(prefix_left + 'run_0' + i + suffix));
            } else {
                animation_dict['run_left'].push(loadImage(prefix_left + 'run_' + i + suffix));
            }
        }
        //Load Shoot Images
        for(let i = 0; i < 4; i++){
            animation_dict['shoot_left'].push(loadImage(prefix_left + 'shoot_' + i + suffix));
        }
        
        return animation_dict;
    }
    
    set_animation_speed(){
        //Set correct animation speed based on sprite state
        if(this.state == 'idle_left' || this.state == 'idle_right'){
            this.animation_speed = 8;
        } else {
            this.ainmation_speed = 5;
        }
    }
    
    health_bar(){
        fill(0, 0, 0);
        rect(this.x + 18, this.y, 30, 5);
        fill(0, 255, 0);
        rect(this.x + 18, this.y, (30 / this.max_health) * this.health, 5);
        
        if(this.health == 0){
            noLoop();
            setTimeout(function(){location.reload();}, 3000);
        }
    }
    
    loop_current_animation(frame){
        //Increment animation index in order to animate sprite
        
        //Set correct animation speed based on sprite state
        this.set_animation_speed();
        
        //Iterate through sprite images to animate hero
        //If sprite is aiming, only loop through animation once, ending on last part of animation so she holds her aiming stance
        let max_animation = this.animation_dict[this.state].length;
        if(this.state == 'aim_left' || this.state == 'aim_right'){
            if(frame % this.animation_speed == 0){
                if(this.animation_index < max_animation - 1){
                    this.animation_index++;
                }
            }
        } else {
            if(frame % this.animation_speed == 0){
                if(this.animation_index < max_animation - 1){
                    this.animation_index++;
                } else {
                    this.animation_index = 0;
                }
            }
        }
    }
    
    update(){
        //Only allow for right scrolling + handle hero physics
        if(this.state == 'run_right'){
            if(this.x >= this.side_scroll_beings){
                BackGround.side_scroll();
            } else {
                this.x += this.run_speed;
            }
        } else if(this.state == 'run_left'){
            if(this.x >= - 20)
            this.x -= this.run_speed;
        }
        
        this.y += this.y_vel;
        //If hero is above ground level, let physics apply
        if(this.y < this.y_standard){
            this.y_vel += this.gravity
        } else {
            //Do not allow the hero to go beneath the ground level and reset jump2 ability when hero hits the ground
            this.y = this.y_standard
            this.y_vel = 0;
            this.jump2 = false;
            this.jump1 = false;
        }
    }
    
    //Hero Action Methods -------------------------------
    _aim(){
        if(this.state == 'shoot_right' || this.state == 'shoot_left'){ //if coming from shooting, display final aim frame
            this.animation_index = this.animation_dict[this.state].length - 1;
        } //if not coming from shooting, play full aim animation

        if(this.facing == 'right'){
            this.state = 'aim_right';
        } else {
            this.state = 'aim_left';
        }
    }
    
    _jump(){
        if(!this.occupied_vehicle){
            if(!this.jump2 && !this.jump1){
                this.y -= 10;
                this.y_vel = -9;
                this.jump1 = true;
            } else if(this.y_vel != 0 && !this.jump2){ //allows the double jump
                this.y -= 10;
                this.y_vel = -9;
                this.jump2 = true;
            } 
        }
    }
    
    _run(behavior){
        if (behavior == 'run_left'){
            this.state = 'run_left';
            this.facing = 'left'
            
        } else if(behavior == 'run_right'){
            this.state = 'run_right';
            this.facing = 'right';
        }
    }
    
    _attack(){
        if(this.state == 'aim_right' || this.state == 'aim_left'){ //first check if already aiming, if not, aim
            if(this.facing == 'right'){
                this.state = 'shoot_right';
            } else {
                this.state = 'shoot_left';
            }
        } else { //If hero isn't already aiming, the first space bar press will make the hero aim
            if(this.facing == 'right'){
                this.state = 'aim_right';
            } else {
                this.state = 'aim_left';
            }
        }
    }
    
    _board(){
        if(!this.occupied_vehicle){ //If not already in a vehicle, attempt to board all vehicles
            let hero_center = this.find_center();
            for(let i = 0; i < all_units.length; i++){
                if(all_units[i].template.type == 'vehicle'){
                    if(all_units[i].template.be_boarded(hero_center)){
                        occupied_vehicle = all_units[i];
                        all_units.splice(i, 1);
                        this.occupied_vehicle = true;
                        this.facing = 'right';
                        this.state = 'idle_right';
                        break;
                    }
                }
            }
        } else {
            occupied_vehicle.template.exit();
            all_units.push(occupied_vehicle);
            occupied_vehicle = false;
            this.occupied_vehicle = false;
            this.facing = 'right';
            this.state = 'idle_right';
        }
    }
    
    _idle(){
        if(this.facing == 'right'){
            this.state = 'idle_right';
        } else {
            this.state = 'idle_left';
        }
    }
    //End Hero Action Methods ---------------------------
    
    action(behavior){
        //Allow hero to perform actions based on user inputs
        if(behavior == 'aim'){
            this._aim();
            return false; //do not check other actions to avoid resetting animation index
            
        } else if(behavior == 'jump'){
            this._jump();
            return false; //do not check other actions to avoid resetting animation index
        }
        
        this.animation_index = 0;
            
        if (behavior == 'run_left' || behavior == 'run_right'){
            this._run(behavior);
            
        } else if(behavior == 'attack'){
            this._attack();
            
        } else if(behavior == 'board'){
            this._board();
            
        } else if(behavior == 'idle'){
            this._idle();
        }
    }
    
    find_center(){
        //Find the position of the central hitpoint of hero
        return [this.x + 35, this.y + 30, 35, 30];
    }
    
    display(){
        //Display the current animated frame
        image(this.animation_dict[this.state][this.animation_index], this.x, this.y, 75, 75);
        
        //Determine central hitpoint of the hero
/*        fill(255,255,255);
        ellipse(this.x + 35, this.y + 30, 5, 5);   */
    }
    
    run(frame){
        this.loop_current_animation(frame);
        if(!this.occupied_vehicle){
            this.display();
            this.update();
        }
        this.health_bar();
    }
}