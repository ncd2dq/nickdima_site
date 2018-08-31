// All food parts
function Food(){
    this.x_offset = floor(random(Tiles));
    this.y_offset = floor(random(Tiles));
    this.x = this.x_offset * Tile_Dimension;
    this.y = this.y_offset * Tile_Dimension;
    
    this.show = function(){
        rect(this.x, this.y, Tile_Dimension, Tile_Dimension);
        
    }
    
}