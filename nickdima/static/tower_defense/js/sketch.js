let background_color;
let cannon_color;
let black;
let flame_thrower_color;
let machine_gun_base_color;
let tower_color;
let simple_enemy_color;
let bomber_enemy_color;



function setup() {
    createCanvas(Canvas_Width, Canvas_Height);
    background_color = color(100, 100, 125);
    cannon_color = color(0, 255, 0);
    black = color(0, 0, 0);
    flame_thrower_color = color(100, 0, 0);
    machine_gun_base_color = color(0, 120, 255);
    tower_color = color(255, 0, 0);
    simple_enemy_color = color(100,25,100);
    bomber_enemy_color = color(255, 100, 255);
}

let Canvas_Width = 1200;
let Canvas_Height = 650;
let FPS = 60;

//final variables
let g = new Game(); //Handles level up, score, game data, allow pausing, ect.
let bullets = [];
let t = new Tower(Canvas_Width, Canvas_Height);
let m =  [ {location:new Vector(Canvas_Width / 2, Canvas_Height / 2), radius: 10} ]; //Just incase the mouse ins't on screen yet, weapons will have a default rotation
let Spawn_Radius = Canvas_Height / 2;
let initial_spwn = true;
let wave = new WaveController();
//end final


//Testing variables
let f_enemies = []
let p = new Flock();
let obstacles = [];

function draw() {
    background(background_color);
    if (initial_spwn){
        for(let i = 0; i < 1; i++){
            f_enemies.push(new SimpleEnemy(t));
            f_enemies.push(new Bomber(t));
        }
        initial_spwn = false;
    }
    
    //Have the mouse location always being recorded so all guns can rotate properly
    if(mouseX){
        m = [{location:new Vector(mouseX, mouseY), radius:10}];
    }
    
    //Run the Tower
    t.run(m[0].location);
    
    //Draw the bullets to screen + check if hit enemies
    if(bullets.length != 0){
        for(let i = 0; i < bullets.length; i++){
            bullets[i].run(f_enemies);
        }
    }
    //Remove offscreen or crashed bullets
    bullets_removal(bullets);
    
    //Remove enemies that hit the tower or that have health = 0 
    enemies_crashed_or_killed(f_enemies);
    
    //Show Cooldowns + game score
    g.run(t.weapons);
    
    //Controll enemy spawning
    wave.run(f_enemies, g);
    
    frameRate(FPS);
    //Testing code
    p.run(m, obstacles);
    
    for(let i = 0; i < f_enemies.length; i++){
        f_enemies[i].run(f_enemies);
    }
    
    
    
    //Allow for initial instruction screen / pausing the game
    if(g.paused){
        g.pause();
    }
    
}


// HELPER FUNCTIONS ---
function bullets_removal(bullet_list){
    //Removes if offscreen or if crashed
    for(let i = bullet_list.length - 1; i >= 0; i--){
        if(bullet_list[i].location.x >= Canvas_Width || bullet_list[i].location.x <= 0
          || bullet_list[i].location.y <= 0 || bullet_list[i].location.y >= Canvas_Height || bullet_list[i].crashed){
            bullet_list.splice(i, 1);
        }
    }
}


function enemies_crashed_or_killed(s_enemy_list){
    for(let i = s_enemy_list.length - 1; i >= 0; i--){
        if(s_enemy_list[i].crashed){
            t.health -= s_enemy_list[i].dmg;
            s_enemy_list.splice(i, 1);
        } else {
            if(s_enemy_list[i].health <= 0){
                s_enemy_list.splice(i, 1);
            }
            
        }
    }
}


// USER INPUT FUNCTIONS ---
function keyPressed(){
    if (keyCode === LEFT_ARROW){

    } else if (keyCode === RIGHT_ARROW){

    } else if (keyCode === DOWN_ARROW){

    } else if (keyCode === UP_ARROW){
        
    } else if (keyCode == 32){ //the spacebar
        t.change_weapon();

    } else if (keyCode == 80){ //the 'p' key
        if(g.paused){
            g.paused = false;
        } else {
            g.paused = true;
        }
        g.pause();
    }
}

function keyReleased(){
    if (keyCode === LEFT_ARROW){

    } else if (keyCode === RIGHT_ARROW){

    } else if (keyCode === UP_ARROW || keyCode === DOWN_ARROW){

    } else if (keyCode == 32){

    }
}

function mousePressed(){
    t.fire(new Vector(mouseX, mouseY), bullets);
}

function mouseReleased(){
    t.fire(new Vector(mouseX, mouseY), bullets);
    
}


/*
function mouseDragged(){
    console.log(mouseX, mouseY);
    t.fire(new Vector(mouseX, mouseY), bullets);
}
*/
