class MachineGunBullets{
    constructor(weapon_tip, weapon_facing_vec){
        this.radius = 3;
        this.location = weapon_tip;
        this.velocity = weapon_facing_vec;
        this.speed = 8;
        this.crashed = false;
        
        this.dmg = 3;

    }
    
    show(){
        fill(black);
        ellipse(this.location.x, this.location.y, this.radius * 2, this.radius * 2); //drawn from 
    }
    
    update(){
        this.location = this.location.add(this.velocity.mult(this.speed));
    }
    
    check_enemy(enemy_list){
        //if the distance between them is less than the distance of both their radius added together, they crashed
        for(let i = enemy_list.length - 1; i >= 0; i--){
            if(this.location.distance(enemy_list[i].location) < this.radius + enemy_list[i].radius){
                this.crashed = true;
                enemy_list[i].health -= this.dmg;
            }
        }
    }
    
    run(enemy_list){
        this.update();
        this.show();
        this.check_enemy(enemy_list);
    }
    
}