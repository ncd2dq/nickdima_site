//To avoid bullets, you need to use the avoidForce method and give it avoidForce(unit that's avoiding something, the thing that it will avoid)

class Flock{
    constructor(){
        this.location = new Vector(100, 100);
        this.height = 25;
        this.width = 12;
        this.hit_box_circle_distance = 2;
        this.points_list = this.create_vertices(this.location);
        this.true_center = [];
        this.velocity = new Vector(0, 0);
        this.max_force = 5;
        this.crashed = false;
        
    }
        
    create_vertices(location){
        //tip, BL, BR, center
        let tip = [location.x, location.y];
        let BL = [tip[0] - (this.width / 2), tip[1] + this.height];
        let BR = [BL[0] + this.width, BL[1]];
        let center = [tip[0], tip[1] + (this.height / 2)];
        
        return [tip, BL, BR, center];
    }
    
    update(){
        for(let i = 0; i < this.points_list.length; i++){
            this.points_list[i][0] += this.velocity.x;
            this.points_list[i][1] += this.velocity.y;
        }
        
        this.location.x += this.velocity.x;
        this.location.y += this.velocity.y;
    }
    
    applyForce(force){
        this.velocity = this.velocity.add(force);
        this.velocity = this.velocity.limit(this.max_force);
    }
    
    avoid(targets){
        for(let i = targets.length - 1; i >= 0; i--){
            let avoid = avoidForce(this, targets[i]);
            this.applyForce(avoid);
        }
        
    }
    
    chase(target){
        if(target.length != 0){
            for(let i = 0; i < target.length; i++){
                let steering = steeringForce(this, target[i].location); //needs unit_class, target_vector
                this.applyForce(steering);
            }
        }
    }
    
    hit_objects(target_attack, target_avoid){
        //WHEN YOU DRAW ELLIPSES IT TAKES (X,Y,X_DISTANCE,Y_DISTANCE) NOT RADIUS
        // (x - h)**2 + (y - k)**2 <= r mean's the point (h,k) is inside the circle
        //can either calculate the distance between two circles and if that distances is less than d1+d2, they collided
        //or you can check all three vertices *a lot slower*
        let obj_list = [];
        if (target_avoid.length != 0){
            obj_list = obj_list.concat(target_avoid);
        }
        if(target_attack.length != 0){
            obj_list = obj_list.concat(target_attack);
        }
        
        if(obj_list.length !=0){
            for(let i = 0; i < obj_list.length; i++){
                let obj_x = obj_list[i].location.x;
                let obj_y = obj_list[i].location.y;

                let dist = new Vector(obj_x, obj_y).distance(this.true_center);

                if (dist < (this.width * this.hit_box_circle_distance / 2) + obj_list[i].radius){
                    this.crashed = true;
                }   
            }
        }
  
    }
    
    rotation(){
        let center_v = new Vector(this.points_list[3][0], this.points_list[3][1]);
        let tip = this.velocity.normalize().mult(this.height).add(center_v);
        
        let n_center_v = this.velocity.normalize().mult(this.height / 2).add(center_v);
        

        //once you know the velocity, just rotate it 90 degrees to get a triangle
        let BL = rotate_this(this.velocity.normalize().mult(this.width / 2), 90);
        BL = BL.add(center_v);
        let BR = rotate_this(this.velocity.normalize().mult(this.width / 2), -90);
        BR = BR.add(center_v);
        
        this.true_center = new Vector(n_center_v.x, n_center_v.y);
        
        //ellipse is the hit box for debugging
        fill(255,0,0);
        ellipse(n_center_v.x, n_center_v.y, this.width*this.hit_box_circle_distance, this.width*this.hit_box_circle_distance);
        
        fill(0,0,0);
        triangle(tip.x, tip.y, BL.x, BL.y, BR.x, BR.y);
        
    }
    
    run(target_attack, target_avoid){
        this.chase(target_attack);
        this.avoid(target_avoid);
        if(this.velocity.x){
            this.rotation();
        }
        this.update();
        this.hit_objects(target_attack, target_avoid);
    }
    
}