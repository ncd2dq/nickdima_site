//Describes the asteroid class
let large = 55;
let medium = 43;
let smallish = 23;
let small = 13;

function Asteroid(width, height, size=4){
    this.crashed = false;
    let possible_x = [];
    let possible_y = [];
    for(let i = 0; i < width / 3; i++){
        possible_x.push(i);
    }
    for(let i = 0; i < height / 3; i++){
        possible_y.push(i);
    }
    for(let i = width * 2 / 3; i < width; i++){
        possible_x.push(i);
    }
    for(let i = height * 2 / 3; i < height; i++){
        possible_y.push(i);
    }
    this.width = width;
    this.height = height;
    this.x = random(possible_x);
    this.y = random(possible_y);
    
    this.size = size;
    if(this.size == 4){
        this.radius = large;
    } else if (this.size == 3){
        this.radius = medium;
    } else if(this.size == 2){
        this.radius = smallish;
    } else if(this.size ==1){
        this.radius = small;
    }
    let x_dir = random(-1, 1);
    let y_dir = random(-1, 1);
    this.velocity = new Vector(x_dir, y_dir);
    this.velocity = this.velocity.unit_direction();
    
    this.loop = function(){
        if(this.x >= this.width + this.radius + 1){
            this.x = 0 - this.radius;
        } else if (this.x <= 0 - this.radius - 1){
            this.x = this.width + this.radius;
        } else if (this.y >= this.height + this.radius + 1){
            this.y = 0 - this.radius;
        } else if (this.y <= 0 - this.radius - 1){
            this.y = this.height + this.radius;
        }
    }
    
    this.bullet_hit = function(bullet_list){
        
        for(let i =0; i < bullet_list.length; i++){
            //(x - h)**2 + (y - k)**2 <= r**2
            let left_side = Math.pow((this.x - bullet_list[i].location.x), 2) + Math.pow((this.y - bullet_list[i].location.y), 2);
            let right_side = Math.pow(this.radius, 2) / 2;
            if(left_side < right_side){
                this.crashed = true;
                bullet_list[i].crashed = true;
            }
        }
    }
    
    this.make_babies = function(asteroid_list){
        //this.velocity .mult(scalar)
        let new_size = this.size - 1;
        let baby1 = new Asteroid(this.width, this.height, new_size);
        let baby2 = new Asteroid(this.width, this.height, new_size);
        
        baby1.x = this.x;
        baby2.x = this.x;
        baby1.y = this.y;
        baby2.y = this.y;
        
        cur_x = this.velocity.x;
        cur_y = this.velocity.y;
        let convFactor = Math.PI / 180;
        new_x_v = cur_x * Math.cos(25 * convFactor) - cur_y * Math.sin(25 * convFactor);
        new_y_v = cur_x * Math.sin(25 * convFactor) + cur_y * Math.cos(25 * convFactor);
        let velocity1 = new Vector(new_x_v, new_y_v);
        
        
        new_x_v = cur_x * Math.cos(335 * convFactor) - cur_y * Math.sin(335 * convFactor);
        new_y_v = cur_x * Math.sin(335 * convFactor) + cur_y * Math.cos(335 * convFactor);        
        let velocity2 = new Vector(new_x_v, new_y_v);
        
        baby1.velocity = velocity1.unit_direction();
        baby2.velocity = velocity2.unit_direction();
        
        if(this.size == 4){
            baby1.velocity = baby1.velocity.mult(1.5);
            baby2.velocity = baby2.velocity.mult(1.5);
        } else if (this.size == 3){
            baby1.velocity = baby1.velocity.mult(1.75);
            baby2.velocity = baby2.velocity.mult(1.75);
        } else if (this.size == 2){
            baby1.velocity = baby1.velocity.mult(2.1);
            baby2.velocity = baby2.velocity.mult(2.1);       
        }
        
        asteroid_list.push(baby1);
        asteroid_list.push(baby2);
    }
    
    this.show = function(){
        if(this.size >= 1){
        fill(asteroid_color);
        ellipse(this.x, this.y, this.radius, this.radius);
        }
    }
    
    this.update = function(){
        this.x += this.velocity.x;
        this.y += this.velocity.y;
    }
    
    this.run = function(bullet_list){
        this.bullet_hit(bullet_list);
        this.update();
        this.show();
        this.loop();
    }
}