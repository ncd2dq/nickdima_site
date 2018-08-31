let Ship_Height = 45;
let Ship_Radius = 18;
let Ship_Gun_Length = 5;

let background_color;
let asteroid_color;
let all_other_color;

let Canvas_Width = 600;
let Canvas_Height = 600;

let ship = new SpaceShip();

let bullets = [];
let asteroids = [];
let initial_asteroid_count = 1;
let asteroid_count = initial_asteroid_count;
let asteroid_increment = 2;

let theta = 0;
let theta_change = 0;

let game = new gameStats(Canvas_Width, Canvas_Height);
game.calculate_asteroid_count(initial_asteroid_count, asteroid_increment, game.level);

let acceleration_vector = new Vector(0, 0);

let developer_mode = false;

function setup() {
    createCanvas(Canvas_Width, Canvas_Height);
    background_color = color(125, 100, 125);
    asteroid_color = color(0, 255, 255);
    all_other_color = color(0, 102, 153);
    //Add asteroids
    for(let i = 0; i < asteroid_count; i++){
        asteroids.push(new Asteroid(Canvas_Width, Canvas_Height));
    }
}


function draw() {
    background(background_color);

    //Display bullets
    if(bullets.length != 0){
        for(let i = 0; i < bullets.length; i++){
            bullets[i].run();
        }
    }
    //No longer display bullets if they run out of fuel or hit an asteroid
    if(bullets.length != 0){
        for(let i = bullets.length - 1; i >= 0; i--){
            if(bullets[i].fuel <= 0){
                bullets.splice(i, 1);
            } else if(bullets[i].crashed == true){
                bullets.splice(i, 1);
            }
        }
    }
    
    //Display asteroids and make babies
    if(asteroids.length != 0){
        for(let i = asteroids.length - 1; i >= 0; i--){
            asteroids[i].run(bullets);
            if(asteroids[i].crashed == true){
                asteroids[i].make_babies(asteroids);
            } 
        }
    }

    if(asteroids.length != 0){
        for(let i = asteroids.length - 1; i >=0; i--){
            if(asteroids[i].crashed == true){
                asteroids.splice(i, 1);
                game.score++;
                game.asteroid_count--;
            } else if(asteroids[i].size <= 0){
                asteroids.splice(i, 1);
            }
        }
    }
    
    //Handle score / level projection
    game.score_keep();
    //Handle ship interactions
    ship.run(theta, asteroids, bullets);
    acceleration_vector = ship.find_ship_facing_direction();
    //Handle ship rotations
    theta += theta_change;
    
    if(game.paused){
        game.pause();
    }
    
    if(asteroids.length == 0){
        game.nextLevel();
        noLoop();
        ship = new SpaceShip();
        bullets = [];
        asteroid_count += asteroid_increment;
        asteroids = [];
        game.calculate_asteroid_count(initial_asteroid_count, asteroid_increment, game.level);
        for(let i = 0; i < asteroid_count; i++){
            asteroids.push(new Asteroid(Canvas_Width, Canvas_Height));
        }
        setTimeout(loop, 3000);
        
    }
    
    if(ship.crashed == true){
        game.crashed();
        noLoop();
        setTimeout(window.location.reload.bind(window.location), 3000)
    }
}


// User input
function keyPressed(){
    if(developer_mode){
        console.log(keyCode);
    }
    if (keyCode === LEFT_ARROW){
        //direction = [-1, 0];
        theta_change = -5;
        
    } else if (keyCode === RIGHT_ARROW){
        //direction = [1, 0];
        theta_change = 5;
        
    } else if (keyCode === DOWN_ARROW){
        ship.boosting = true;
        ship.forward = true;
        
    } else if (keyCode === UP_ARROW){
        ship.boosting = true;
        ship.forward = false;
        
    } else if (keyCode == 32){ //the spacebar
        ship.shooting = true;
    } else if (keyCode == 80){ //the 'p' key
        if (game.paused){
            game.paused = false;
            loop();
        } else {
            game.paused = true;
        }
    }
}

function keyReleased(){
    if(developer_mode){
        console.log(keyCode);
    }
    
    if (keyCode === LEFT_ARROW){
        //direction = [-1, 0];
        theta_change = 0;
        
    } else if (keyCode === RIGHT_ARROW){
        //direction = [1, 0];
        theta_change = 0;
    } else if (keyCode === UP_ARROW || keyCode === DOWN_ARROW){
        ship.boosting = false;
        acceleration_vector = new Vector(0, 0);
    } else if (keyCode == 32){
        ship.shooting = false;
        ship.fire_rate_frame = 0;
    }
}
