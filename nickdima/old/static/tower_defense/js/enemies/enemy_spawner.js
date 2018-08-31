function random_spawn(canvas_w, canvas_h, spwn_radius, tower_class){
    //(x - h)**2 + (y - k)**2 = r**2
    //Need to determine the maximum and the minimum y position
    //Max = circle y, minimum = canvas_h
    // y = +/- sqrt(r**2 - (x - h)**2) + k
    let spwn_x = random(canvas_w, canvas_w + spwn_radius);
    let min_y = -sqrt(Math.pow(spwn_radius, 2) - Math.pow(spwn_x - canvas_w, 2)) + canvas_h / 2;
    let spwn_y = random(min_y, canvas_h);
    
    let spwn_dir = determine_spwn_direction(spwn_x, spwn_y, tower_class);
    
    return [new Vector(spwn_x, spwn_y), spwn_dir];
}

function determine_spwn_direction(spwn_x, spwn_y, tower_class){
    let new_x = random(tower_class.location.x - spwn_x, tower_class.location.x + tower_class.radius - spwn_x);
    let new_y = random(tower_class.location.y - spwn_y, tower_class.location.y + tower_class.radius - spwn_y);
    let dir_new = new Vector(new_x, new_y);
    dir_new = dir_new.normalize();
    
    return dir_new;
}

function bomber_spawn(canvas_w, canvas_h){
    //Goal of this function is to return the initial Vector(x, y) of the bomber vechile
    let spawn_x = random(canvas_w, canvas_w * 1.5);
    let spawn_y = random(0, canvas_h * (1 / 4));
    
    let gravity = new Vector(0, random(0.0055, 0.1));
    console.log(gravity.y)
    return [new Vector(spawn_x, spawn_y), new Vector(-1, 0), gravity];
}