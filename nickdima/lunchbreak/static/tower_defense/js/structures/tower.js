//rect(x,y,x_dist,y_dist);
//drawn from top left
//the base of the tower

class Tower{
    constructor(canv_x, canv_y){
        this.radius = 75;
        this.location = new Vector(this.radius / 3, canv_y - this.radius - (this.radius / 3));
        this.weapons = this.create_weapons();
        this.weapon_index_max = 2; //needs to be maually updated if more weapons are built
        this.weapon_index = 0;
        this.current_weapon = this.weapons[this.weapon_index];
        this.health = 100;
        this.max_health = 100;
    }
    
    show(){
        fill(tower_color);
        rect(this.location.x, this.location.y, this.radius, this.radius);
        
    }
    
    create_weapons(){
        let c = new Cannon(this.location, this.radius);
        let ft = new FlameThrower(this.location, this.radius);
        let mg = new MachineGun(this.location, this.radius);
        
        return [mg, c, ft];
    }
    
    fire(mouse_click_vec, bullets){
        this.current_weapon.fire(mouse_click_vec, bullets);
    }
    
    change_weapon(){
        //Change weapon when you hit space bar
        this.weapon_index++;
        if(this.weapon_index <= this.weapon_index_max){
            this.current_weapon = this.weapons[this.weapon_index];
        } else {
            this.weapon_index = 0;
            this.current_weapon = this.weapons[this.weapon_index];
        }
    }
    
    run(mouse_vec){
        this.show();
        this.current_weapon.run(mouse_vec);
        
        this.weapons[1].cool_down();
        this.weapons[2].cool_down();
    }
    
}