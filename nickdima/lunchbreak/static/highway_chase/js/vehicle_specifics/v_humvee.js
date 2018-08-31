class Humvee{
    constructor(){
        this.template = new Vehicle(true, false, '/humvee');
        
        //SIZING
        this.template.tire_left_x_size = 45;
        this.template.tire_left_y_size = 45;
        this.template.tire_right_x_size = 45;
        this.template.tire_right_y_size = 45;
        this.template.body_x_size = 225;
        this.template.body_y_size = 150;
        
        //Central Point
        this.template.x = 350;
        this.template.x_vel = 0;
        this.template.y_vel = 0;
        
        this.template.ground_y_punk = 370;
        this.template.ground_y_industrial = 310;
        
        if(BackGround.name == 'Punk'){
            this.template.y = this.template.ground_y_punk;
        } else if (BackGround.name == 'Industrial'){
            this.template.y = this.template.ground_y_industrial;
        }
        
        //Offset positions
        this.template.tire_left_x_offset = -81;
        this.template.tire_left_y_offset = 7;
        this.template.tire_right_x_offset = 50;
        this.template.tire_right_y_offset = 7;
        this.template.body_x_offset = -105;
        this.template.body_y_offset = -90;
        this.template.body_x_offset_s = -105;
        this.template.body_y_offset_s = -90;
        this.template.hero_x_offset = 20;
        this.template.hero_y_offset = -10;
        this.template.wheel_rotation_offset = 23;
        
        this.template.boarding_threshold = 50;
        
        this.template.idle_animation_speed = 5;
        this.template.idle_movement = 2;
        this.template.idle_jerk = 1.2;
        
        this.template.x_speed = 5;
        
    }
    
    display(occupied){
        this.template.display(occupied);
        
/*        //See central point
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