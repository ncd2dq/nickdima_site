function Vector(x, y){
    this.x = x;
    this.y = y;
    
    this.add = function(other){
        //Adds two vectors NOT IN PLACE
        let new_x = this.x + other.x;
        let new_y = this.y + other.y;
        
        return new Vector(new_x, new_y);
    }
    
    this.sub = function(other){
        //Subtracts two vectors NOT IN PLACE
        let new_x = this.x - other.x;
        let new_y = this.y - other.y;
        
        return new Vector(new_x, new_y);
    }
    
    this.mult = function(scalar){
        //Multiplies a vector by a scalar
        let new_x = this.x * scalar;
        let new_y = this.y * scalar;
        
        return new Vector(new_x, new_y);
    }
    
    this.mag = function(){
        //Returns the magnitude of a vector
        let operand = Math.pow(this.x, 2) + Math.pow(this.y, 2);
        let magnitude = sqrt(operand);
        
        return magnitude;
    }
    
    this.unit_direction = function(){
        //Returns the unit direction of a vector
        let mag = this.mag();
        let new_x = this.x / mag;
        let new_y = this.y / mag;
        
        return new Vector(new_x, new_y);
    }
    
    this.mid_point = function(other){
        let difference = this.sub(other);
        difference = difference.mult(0.5);
        difference = difference.add(other);
        
        return difference;
    }
}