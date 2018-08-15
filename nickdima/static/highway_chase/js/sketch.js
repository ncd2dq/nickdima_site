//let Canvas_Width =  window.innerWidth;
//let Canvas_Height = window.innerHeight;
let Canvas_Width =  800;
let Canvas_Height = 445;
let game_state = true;
//Load Backgrounds
let blackBackground;
let industrialBackground;
let punkBackground;
let BackGround;

//Instantiate hero
let hero;

//All enemies and vehicles should be in "all_units" except for the occupied vehicle
let all_units = [];
let occupied_vehicle = false;

//TESTING--------------
let humvee_object;
let bike1;
let bike2;
let j;
let test_enemy; 

function preload(){
    
}


function setup(){
    createCanvas(Canvas_Width, Canvas_Height);
    //Black backing incase any background layer isn't aligned correctly makes it harder to notice
    blackBackground = color(0, 0, 0);
    
    //Load up backgrounds
    industrialBackground = new IndustrialBackground();
    punkBackground = new PunkBackground();
    
    //Whichever background is asigned to "BackGround" will be the visible background
    BackGround = industrialBackground;
    
    hero = new Hero();
    
    //TESTING--------------
    humvee_object = new Humvee();
    bike1 = new MotoCommuter();
    bike2 = new MotoNaked();
    j = new Jet();
    
    //If units are not in "all_units", they will not move when the background scrolls
    all_units.push(humvee_object, bike1, bike2, j);
}

//GAME LOGIC ------------------------------------------>
function draw(){
    background(blackBackground);
    BackGround.run();
    
    //Vehicle TESTING--------------
    if(occupied_vehicle){
        occupied_vehicle.run_occupied(frameCount);
    }
    for(let i = 0; i < all_units.length; i++){
        all_units[i].run();
    }
    remove_units(all_units);
    
    //Hero Testing
    hero.run(frameCount);
    
    //enemy testing
    if(frameCount % 50 == 0){
        if(random() > 0.35){
            let new_enemy = new Skeleton();
            new_enemy.template.x = Canvas_Width;
            all_units.push(new_enemy);
        }
    }
    
    if(!game_state){
        textSize(15);
        fill(0, 255, 0);
        text("Move with arrow keys or 'WDSA'", 20, 50);
        text("Shoot with spacebar or mouse click or screen tap", 20, 70);
        text("Get in vehicles with 'f' or 'b'", 20, 90);
    }
}
//END GAME LOGIC ------------------------------------------>

function remove_units(unit_list){
    for(let i = unit_list.length - 1; i >= 0; i--){
        if(unit_list[i].template.type == 'enemy'){
            if(!unit_list[i].template.alive){
                unit_list.splice(i, 1); 
            }
        } else if (unit_list[i].template.x <= - 15){
            unit_list.splice(i, 1);
        }
    }
}

//User Input -------------
function keyPressed(){
    if (keyCode === LEFT_ARROW || keyCode == 65){
        if(!hero.occupied_vehicle){
            hero.action('run_left');
        } else {
            occupied_vehicle.template.move('left');
        }
        
    } else if (keyCode === RIGHT_ARROW || keyCode == 68){
        if(!hero.occupied_vehicle){
            hero.action('run_right');
        } else {
            occupied_vehicle.template.move('right');
        }
        
    } else if (keyCode === UP_ARROW || keyCode == 87){
        if(!hero.occupied_vehicle){
            hero.action('jump');
        } else {
            occupied_vehicle.template.move('up');
        }
        
    } else if (keyCode === DOWN_ARROW || keyCode == 83){
        if(hero.occupied_vehicle){
            occupied_vehicle.template.move('down');
        }
    } else if (keyCode == 32){ //the spacebar
        hero.action('attack');
        if(hero.state == 'shoot_right' || hero.state == 'shoot_left'){
            for(let i = 0; i < all_units.length; i ++){
                if(all_units[i].template.type == 'enemy'){
                    all_units[i].template.be_attacked({'x': mouseX, 'y': mouseY});
                }
            }
        }

    } else if (keyCode == 80){ //the 'p' key

    } else if (keyCode == 66 || keyCode == 70){ //the 'b' key or 'f' key
        hero.action('board');
    }
}

function keyReleased(){
    if (keyCode === LEFT_ARROW || keyCode == 65){
        if(!hero.occupied_vehicle){
            hero.action('idle');
        } else {
            occupied_vehicle.template.move('stop');
        }
        
    } else if (keyCode === RIGHT_ARROW || keyCode == 68){
        if(!hero.occupied_vehicle){
            hero.action('idle');
        } else {
            occupied_vehicle.template.move('stop');
        }
        
    } else if (keyCode === UP_ARROW || keyCode == 87){
        if(hero.occupied_vehicle){
            occupied_vehicle.template.move('stop_y');
        }
        
    } else if (keyCode == DOWN_ARROW || keyCode == 83){
        if(hero.occupied_vehicle){
            occupied_vehicle.template.move('stop_y');
        }

    } else if (keyCode == 32){ //the spacebar
        hero.action('aim');

    } else if (keyCode == 80){ //the 'p' key

    } else if (keyCode == 66 || keyCode == 70){ //the 'b' key or 'f' key

    }
}

function mousePressed(){
    hero.action('attack');
    if(hero.state == 'shoot_right' || hero.state == 'shoot_left'){
        for(let i = 0; i < all_units.length; i ++){
            if(all_units[i].template.type == 'enemy'){
                all_units[i].template.be_attacked({'x': mouseX, 'y': mouseY});
            }
        }
    }
}

function mouseReleased(){
    hero.action('aim');
}
//End user input -----

function change_level(){
    if(BackGround == industrialBackground){
        setup();
        BackGround = punkBackground;
        hero = new Hero();
        //TESTING--------------
        all_units = [];
        humvee_object = new Humvee();
        bike1 = new MotoCommuter();
        bike2 = new MotoNaked();
        j = new Jet();

        //If units are not in "all_units", they will not move when the background scrolls
        all_units.push(humvee_object, bike1, bike2, j);
    } else {
        setup();
        BackGround = industrialBackground;
        hero = new Hero();
        //TESTING--------------
        all_units = [];
        occupied_vehicle = false;
        humvee_object = new Humvee();
        bike1 = new MotoCommuter();
        bike2 = new MotoNaked();
        j = new Jet();

        //If units are not in "all_units", they will not move when the background scrolls
        all_units.push(humvee_object, bike1, bike2, j);
    }

}

function pause_game(){
    if(game_state){
        noLoop();
        game_state = false;
    } else {
        loop();
        game_state = true;
    }
}