class CannonBullets{
    constructor(weapon_tip, weapon_facing_vec){
        this.radius = 15;
        this.location = weapon_tip;
        this.velocity = weapon_facing_vec;
        this.speed = 15;
        this.crashed = false;
        
        this.dmg = 25;
    }
    
    show(){
        fill(black);
        ellipse(this.location.x, this.location.y, this.radius * 2, this.radius * 2); //drawn from center
    }
    
    update(){
        this.location = this.location.add(this.velocity.mult(this.speed));
    }
    
    check_enemy(enemy_list){
        //if the distance between them is less than the distance of both their radius added together, they crashed
        for(let i = enemy_list.length - 1; i >= 0; i--){
            if(this.location.distance(enemy_list[i].location) < this.radius + enemy_list[i].radius){
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