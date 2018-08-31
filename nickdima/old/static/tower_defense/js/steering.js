const convFactor = Math.PI / 180;

function rotate_this(vect, theta){
    //x' = x*Math.cos(theta) - y*Math.sin(theta)
    //y' = y*Math.cos(theta) + x*Math.sin(theta)
    let new_x = vect.x * Math.cos(theta * convFactor) - vect.y * Math.sin(theta * convFactor);
    let new_y = vect.y * Math.cos(theta * convFactor) + vect.x * Math.sin(theta * convFactor);
    
    return new Vector(new_x, new_y);
}

function steeringForce(unit_class, target_vector){
    let steering = new Vector(target_vector.x - unit_class.location.x,
                               target_vector.y - unit_class.location.y);
    steering = steering.normalize();
    
    return steering
}

function avoidForce(unit_class, avoid_this_class, angle=30, avoidForce=1000){
    //Higher avoidForce = more important the objects are
    //angle is the angle by which it's going to try and avoid the force by
    //x' = x*Math.cos(theta) - y*Math.sin(theta)
    //y' = y*Math.cos(theta) + x*Math.sin(theta)
    let avoid_x = avoid_this_class.location.x;
    let avoid_y = avoid_this_class.location.y;
    
    let class_x = unit_class.location.x;
    let class_y = unit_class.location.y;
    
    let pointer = new Vector(avoid_x - class_x, avoid_y - class_y);
    let dist2 = Math.pow(pointer.mag(), 2);
    pointer = pointer.normalize();
    
    avoid = rotate_this(pointer, angle);
    avoid = avoid.mult(1 / dist2).mult(avoidForce);
    
    return avoid;
}