function gameStats(width, height){
    this.score = 0;
    this.level = 1;
    this.width = width;
    this.height = height;
    this.over = "You Crashed!";
    this.new_level = "Next Level!";
    this.asteroid_count = 0;
    this.count_per_asteroid = 15;
    
    this.instruction1 = "Press or hold the spacebar to fire";
    this.instruction2 = "Press or hold the arrow keys to move";
    this.instruction3 = "Press 'P' to play or pause at anytime";
    
    this.paused = true;
    
    this.nextLevel = function(){
        this.level ++;
        textSize(25);
        fill(0, 255, 0);
        text(this.new_level, this.width / 2 - 75, this.height / 2);
    }
    
    this.calculate_asteroid_count = function(initial_asteroids, asteroid_increment, level){
        if(level == 1){
            this.asteroid_count = this.count_per_asteroid * initial_asteroids;
        } else if(level > 1) {
            this.asteroid_count = ((this.count_per_asteroid * initial_asteroids) + (this.level - 1) * asteroid_increment * this.count_per_asteroid);
        }
    }
        
    this.score_keep = function(){
        textSize(25);
        fill(all_other_color);
        text("Score: " + this.score, this.width - 160, 30);
        text("Level: " + this.level, 25, 30);
        text("Asteroids: " + this.asteroid_count, 25, 55);
    }
    
    this.crashed = function(){
        textSize(25);
        fill(255, 0, 0);
        text(this.over, this.width / 2 - 75, this.height / 2);
        text("Final Score Was: " + this.score, this.width / 2 - 75, this.height / 2 + 35);
    }
    
    this.pause = function(){
        background(0, 0, 0, 175);
        textSize(25);
        fill(255, 0, 0);
        text(this.instruction1, this.width / 3 - 75, this.height / 2);
        text(this.instruction2, this.width / 3 - 75, this.height / 2 + 35);
        text(this.instruction3, this.width / 3 - 75, this.height / 2 + 70);
        noLoop();
    }
    
}

//let difficulty = window.prompt("Please type the desired difficulty level (Case Sensitive)", "Hard, Medium, Easy");