class MachineGun{
    constructor(t_loc, t_radi){
        this.location_center = new Vector(t_loc.x + t_radi / 2, t_loc.y + t_radi / 2);
        this.base_radi = t_radi / 2;
        
        this.gun_1_ready = true;
        this.gun_angle = 20;
        this.gun_angle_offset = 30;
        this.facing = new Vector(1, -1);
        this.gun_1_location = new Vector(this.location_center.x, this.location_center.y - this.base_radi / 2);
        this.gun_2_location = new Vector(this.location_center.x + this.base_radi / 2, this.location_center.y);
        this.tip_1 = this.gun_1_location.add(this.facing.mult(this.barrel_length));
        this.tip_2 = this.gun_2_location.add(this.facing.mult(this.barrel_length));
        this.barrel_length = 35;
        this.tip_offset = 9 / 10;
        this.cool_down_time = 0;
        
    }
    
    cool_down(){
        
        
    }
    
    fire(mouse_click_vec, bullets){
        if(this.gun_1_ready){
            this.gun_1_ready = false;
            let bullet = new MachineGunBullets(this.tip_1, this.facing);
            bullets.push(bullet);
        } else {
            this.gun_1_ready = true;
            let bullet = new MachineGunBullets(this.tip_2, this.facing);   
            bullets.push(bullet);
        }
        
        
    }
    
    machine_gun_rotate(mouse_vec){
        
        let ref_vec = new Vector(this.location_center.x, this.location_center.y);
        ref_vec.x += this.base_radi / 2;
        ref_vec = ref_vec.sub(this.location_center);

        let mouse_ref = mouse_vec.sub(this.location_center);
        
        let dot = mouse_ref.dot(ref_vec);
        
        dot = dot / (mouse_ref.mag() * ref_vec.mag());
        
        this.gun_angle = Math.acos(dot) * (1 / convFactor);
        
        let face = mouse_vec.sub(this.location_center).normalize();
        this.facing = face;
        
        let r = this.base_radi / 2;
        this.gun_1_location.x =  r * Math.cos(this.gun_angle * convFactor * - 1 - this.gun_angle_offset * convFactor) + this.location_center.x;
        this.gun_1_location.y =  r * Math.sin(this.gun_angle * convFactor * - 1 - this.gun_angle_offset * convFactor) + this.location_center.y;
        
        this.gun_2_location.x = r * Math.cos(this.gun_angle * convFactor * - 1 + this.gun_angle_offset * convFactor) + this.location_center.x;
        this.gun_2_location.y = r * Math.sin(this.gun_angle * convFactor * - 1 + this.gun_angle_offset * convFactor) + this.location_center.y;
        
        
    }
    
    show(){
        //Base
        fill(machine_gun_base_color);
        ellipse(this.location_center.x, this.location_center.y, this.base_radi, this.base_radi);
        
        strokeWeight(3);
        //Barrel 1
        if(this.gun_1_ready){
            //Long barrel
            let tip = this.gun_1_location.add(this.facing.mult(this.barrel_length));
            this.tip_1 = tip;
            line(this.gun_1_location.x, this.gun_1_location.y, tip.x, tip.y);
        } else {
            let tip = this.gun_1_location.add(this.facing.mult(this.barrel_length * this.tip_offset));
            this.tip_1 = tip;
            line(this.gun_1_location.x, this.gun_1_location.y, tip.x, tip.y);
            
        }
        
        //Barrel 2
        if(!this.gun_1_ready){
            //Short barrel
            let tip_2 = this.gun_2_location.add(this.facing.mult(this.barrel_length));
            this.tip_2 = tip_2;
            line(this.gun_2_location.x, this.gun_2_location.y, tip_2.x, tip_2.y); 
        } else {
            let tip_2 = this.gun_2_location.add(this.facing.mult(this.barrel_length * this.tip_offset));
            this.tip_2 = tip_2;
            line(this.gun_2_location.x, this.gun_2_location.y, tip_2.x, tip_2.y);
        }
        strokeWeight(1);
    }
    
    run(mouse_vec, bullets){
        this.show();
        this.machine_gun_rotate(mouse_vec);
        
    }
    
}