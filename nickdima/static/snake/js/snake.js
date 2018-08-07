// All Snake Parts
function SnakeHead(){
    this.x_offset = snake_offset;
    this.y_offset = snake_offset;
    this.x = this.x_offset * Tile_Dimension;
    this.y = this.y_offset * Tile_Dimension;
    this.prev_x = 0;
    this.prev_y = 0;
    this.tail = []
    
    this.show = function(){
        // Draws the head of the snake
        color(0, 255, 0);
        rect(this.x, this.y, Tile_Dimension, Tile_Dimension);
        
        // Draws the body pieces of the snake
        if (this.tail.length != 0){
            for (i = 0; i < this.tail.length; i++){
                this.tail[i].show()
            }
        }
    }
    
    this.move = function(direction){
        // First, store current location as previous, so that can be used to
        // move snake body pieces, then update current position
        this.prev_x = this.x;
        this.prev_y = this.y;
        this.x += direction[0] * Tile_Dimension;
        this.y += direction[1] * Tile_Dimension;
        
        // This checks if head collided with any of tail pieces
        for (i = 0; i< this.tail.length; i++){
            if (this.x == this.tail[i].x && this.y == this.tail[i].y){
                this.tail = [];
                alert("Your final score was " + score)
                score = 0
            }
        }
        
        // This ensures that the snake wraps around the edges of the screen
        if (this.x >= Canvas_x){
            this.x = 0;
        } else if (this.x < 0){
            this.x = Canvas_x - Tile_Dimension;
        } else if (this.y >= Canvas_y){
            this.y = 0;
        } else if (this.y < 0){
            this.y = Canvas_y - Tile_Dimension;
        }
        
        // This handles the trailing affect of the snake tail
        if (this.tail.length != 0){
            for (i = 0; i < this.tail.length; i++){
                // For the first tail piece, take the prev_location from the SnakeHead
                if (i == 0){
                    this.tail[i].prev_x = this.tail[i].x;
                    this.tail[i].prev_y = this.tail[i].y;
                    this.tail[i].x = this.prev_x;
                    this.tail[i].y = this.prev_y;
                } else {
                    // For the other tail pieces, take the prev_location from tail pieces
                    // that appear earlier in the tail array
                    this.tail[i].prev_x = this.tail[i].x;
                    this.tail[i].prev_y = this.tail[i].y;
                    this.tail[i].x = this.tail[i - 1].prev_x;
                    this.tail[i].y = this.tail[i - 1].prev_y;   
                }
            }
        }
        
    }
    
    // Checks if the snake head is overlapping food and replaces with new food
    // as well as increments score
    this.eat = function(food_list){
        if (food_list.length > 0){
            for (i = 0; i < food_list.length; i++){
                if (this.x == food_list[i].x && this.y == food_list[i].y){
                    this.tail.push(new SnakeBody(this.prev_x, this.prev_y));
                    food_list[i] = new Food();
                    score += 1;
                    
                }
            }
        }
        
    }
    
}

// Snake body class that just keeps track of locations and can be drawn
function SnakeBody(x, y){
    this.x = x;
    this.y = y;
    this.prev_x = 0;
    this.prev_y = 0;
    
    this.show = function(){
        rect(this.x, this.y, Tile_Dimension, Tile_Dimension)
    }
}