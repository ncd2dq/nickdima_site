class Vector{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
    
    is_in(shape, points){
        // Shape = 'circle', 'triangle', 'square'
        // Points
        // -- circle [center_x, center_y, radius]
        // -- triangle [center_x, center_y, radius, height]
        // -- square [top_left_x, top_left_y, x_len, y_len]
        if(shape == 'circle'){
            condition = in_circle(points);
        } else if(shape == 'triangle'){
            condition = in_triangle(points);
        } else if(shape == 'square'){
            condition = in_square(points);
        } else {
            console.log('Not a valid shape');
        }
    }
    
    in_square(points){
        
    }
    
    in_triangle(points){
        
    }
    
    in_circle(points){
        
    }
}