class Jet{
    constructor(){
        this.template = new Vehicle(false, false, ['/jet', 1]);
        
        //SIZING
        this.template.body_x_size = 225;
        this.template.body_y_size = 150;
        
        //Central Point
        this.template.x = 50;
        this.template.x_vel = 0;
        this.template.y_vel = 0;
        
        this.template.ground_y_punk = 390;
        this.template.ground_y_industrial = 335;
        
        if(BackGround.name == 'Punk'){
            this.template.y = this.template.ground_y_punk;
        } else if (BackGround.name == 'Industrial'){
            this.template.y = this.template.ground_y_industrial;
        }
        
        //Offset positions
        this.template.body_x_offset = -120;
        this.template.body_y_offset = -70;
        this.template.body_x_offset_s = -120;
        this.template.body_y_offset_s = -70;
        
        this.template.boarding_threshold = 35;
        
        this.template.idle_animation_speed = 5;
        this.template.idle_movement = 2;
        this.template.idle_jerk = 1.2;
        
        this.template.x_speed = 8;
        this.template.y_speed = 8;
    }
    
    display(occupied){
        this.template.display(occupied);
        
/*        //See central point
        fill(255,255,255);
        ellipse(this.template.x, this.template.y, 10, 10);*/
    }
    
    animation(frame, no_hero_idle){
        this.template.animation(frame, no_hero_idle);
    }
    
    update(){
        this.template.update();
    }
    
    run(){
        this.display(false);
        
        if(BackGround.name == 'Punk'){
            if(this.template.y < this.template.ground_y_punk){
                this.animation(frameCount, true);
            }
        } else if (BackGround.name == 'Industrial'){
            if(this.template.y < this.template.ground_y_industrial){
                this.animation(frameCount, true);
            }
        }
    }
    
    run_occupied(frame){
        this.animation(frame, false);
        this.display(true);
        this.update();
    }
}