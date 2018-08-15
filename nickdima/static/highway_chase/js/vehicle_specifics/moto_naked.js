class MotoNaked{
    constructor(){
        this.template = new Vehicle(true, true, '/motorbikes/naked');
        
        //SIZING
        this.template.tire_left_x_size = 30;
        this.template.tire_left_y_size = 30;
        this.template.tire_right_x_size = 30;
        this.template.tire_right_y_size = 30;
        this.template.body_x_size = 130;
        this.template.body_y_size = 50;
        
        //Central Point
        this.template.x = 550;
        this.template.x_vel= 0;
        this.template.y_vel = 0;
    
        
        this.template.ground_y_punk = 382;
        this.template.ground_y_industrial = 324;
        
        
        if(BackGround.name == 'Punk'){
            this.template.y = this.template.ground_y_punk;
        } else if (BackGround.name == 'Industrial'){
            this.template.y = this.template.ground_y_industrial;
        }
        
        //Offset positions
        this.template.tire_left_x_offset = -65;
        this.template.tire_left_y_offset = 7;
        this.template.tire_right_x_offset = 30;
        this.template.tire_right_y_offset = 7;
        this.template.body_x_offset = -70;
        this.template.body_y_offset = -22; 
        this.template.body_x_offset_s = -70;
        this.template.body_y_offset_s = -22;
        this.template.hero_x_offset = 0;
        this.template.hero_y_offset = -20;
        this.template.wheel_rotation_offset = 15;
        
        this.template.boarding_threshold = 30;
        
        this.template.idle_animation_speed = 5;
        this.template.idle_movement = 1;
        this.template.idle_jerk = 1.1;
        
        this.template.x_speed = 10;
        
    }
    
    display(occupied){
        this.template.display(occupied);
        
  /*      //See central point
        fill(255,255,255);
        ellipse(this.template.x, this.template.y, 10, 10);*/
    }
    
    animation(frame){
        this.template.animation(frame);
    }
    
    update(){
        this.template.update();
    }
    
    run(){
        this.display();
    }
    
    run_occupied(frame){
        this.animation(frame);
        this.display(true);
        this.update();
    }
}
    