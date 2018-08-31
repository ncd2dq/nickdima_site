class IndustrialBackground{
    constructor(){
        this.name = 'Industrial';
        this.position1 = 0;
        this.position2 = 697.5 ;
        this.position3 = 697.5 * 2;
        
        this.b0 = loadImage('http://www.nickdima.com/static/highway_chase/assets/environments/industrial/layer0.png');
        this.b0x = this.position1;
        this.b0x2 = this.position2;
        this.b0x3 = this.position3;
        
        this.b1 = loadImage('http://www.nickdima.com/static/highway_chase/assets/environments/industrial/layer1.png');
        this.b1x = this.b0x;
        this.b1x2 = this.b0x2;
        this.b1x3 = this.b0x3
        
        this.b2 = loadImage('http://www.nickdima.com/static/highway_chase/assets/environments/industrial/layer2.png');
        this.b2x = this.b0x;
        this.b2x2 = this.b0x2;
        this.b2b3 = this.b0x3;
        
        this.b3 = loadImage('http://www.nickdima.com/static/highway_chase/assets/environments/industrial/layer3.png');
        this.b3x = this.b0x;
        this.b3x2 = this.b0x2;
        this.b3x3 = this.b0x3;
        this.image_resizing = 1.98;
        
        this.speed_s = 2 * 1.2 * 1.2;
        this.speed = 2 * 1.2 * 1.2;
        
        this.floor_y = 360;
        this.hero_floor = 295;
    }

    reset_speed(){
        //Used when hero exits a vehicle to return background to neutral walking speed
        this.speed = this.speed_s;
    }
    
    
    move_objects(){
        //When side scrolling, all units aside from the hero and their occupied vehicle should be pushed to the left
        for(let i = 0; i < all_units.length; i++){
            all_units[i].template.x -= this.speed;
        }
    }
    
    realign(){
        //stops the gap from occuring between parralax layers
        //Stage 1 --> Find the farthest left most of each set
/*        let left_most = [this.b0x, this.b0x2, this.b0x3];
        
        left_most.sort(function(a,b){return a-b});
        
        //Stage 2 --> Redraw all others based on farthest left
        //Realign b_x
        left_most[1] = left_most[0] + 697;
        left_most[2] = left_most[0] + (697 * 2);
        this.b0x = left_most[0];
        this.b0x2 = left_most[1];
        this.b0x3 = left_most[2];
        
        //Realign b1x
        this.b1x = left_most[0];
        this.b1x2 = left_most[1];
        this.b1x3 = left_most[2];
        
        //Realign b2x
        this.b2x = left_most[0];
        this.b2x2 = left_most[1];
        this.b2x3 = left_most[2];*/
        
        this.b0x = 0;
        this.b0x2 = 695;
        this.b0x3 = 695 * 2;
        
        //Realign b1x
        this.b1x = 0;
        this.b1x2 = 695;
        this.b1x3 = 695 * 2;
        
        //Realign b2x
        this.b2x = 0;
        this.b2x2 = 695;
        this.b2x3 = 695 * 2;
        
    }
    
    update(){
        this.b0x = this.position1;
        this.b1x = this.position1;
        this.b2x = this.position1;
        this.b3x = this.position1;
        
        this.b0x2 = this.position2;
        this.b1x2 = this.position2;
        this.b2x2 = this.position2;
        this.b3x2 = this.position2;
        
        this.b0x3 = this.position3;
        this.b1x3 = this.position3;
        this.b2x3 = this.position3;
        this.b3x3 = this.position3;
        
        this.position1 -= this.speed;
        this.position2 -= this.speed;
        this.position3 -= this.speed;

        
    }
    
    infinite_loop(){
        //When any of the images reaches fully off the left side of screen, reset it by sending it to the far right off screen
        if (this.position1 <= -697.5){
            this.position1 = 697.5 * 2;
            this.realign();
        }
        if (this.position2 <= -697.5){
            this.position2 = 697.5 * 2;
            this.realign();
        }
        if (this.position3 <= -697.5){
            this.position3 = 697.5 * 2;
            this.realign();
        }
    }
    
    display(){
        //Display images: For the industrial level, there is no parallax.
        //Syntax image(image, x_pos, y_pos, x_resize, y_resize)
        
        //Background iteration 1
        image(this.b0, this.b0x, 0, this.b0.width * this.image_resizing, this.b0.height * this.image_resizing);
        image(this.b1, this.b1x, 0, this.b1.width * this.image_resizing, this.b1.height * this.image_resizing);
        image(this.b2, this.b2x, 0, this.b2.width * this.image_resizing, this.b2.height * this.image_resizing);
        image(this.b3, this.b3x, 0, this.b3.width * this.image_resizing, this.b3.height * this.image_resizing);
        
        //Background iteration 2
        image(this.b0, this.b0x2, 0, this.b0.width * this.image_resizing, this.b0.height * this.image_resizing);
        image(this.b1, this.b1x2, 0, this.b1.width * this.image_resizing, this.b1.height * this.image_resizing);
        image(this.b2, this.b2x2, 0, this.b2.width * this.image_resizing, this.b2.height * this.image_resizing);
        image(this.b3, this.b3x2, 0, this.b3.width * this.image_resizing, this.b3.height * this.image_resizing);
        
        //Background iteration 3
        image(this.b0, this.b0x3, 0, this.b0.width * this.image_resizing, this.b0.height * this.image_resizing);
        image(this.b1, this.b1x3, 0, this.b1.width * this.image_resizing, this.b1.height * this.image_resizing);
        image(this.b2, this.b2x3, 0, this.b2.width * this.image_resizing, this.b2.height * this.image_resizing);
        image(this.b3, this.b3x3, 0, this.b3.width * this.image_resizing, this.b3.height * this.image_resizing);
        
/*        //Use this to see the proper "ground level" drawn with a red line"
        stroke(255, 0, 0);
        strokeWeight(1);
        line(0, 360, 400, 360);*/
    }
    
    run(){
        this.infinite_loop();
        this.display();
    }
    
    side_scroll(){
        this.update();
        this.move_objects();
    }
    
}
