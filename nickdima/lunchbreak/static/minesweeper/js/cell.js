function Cell(x, y){
    this.x_ref = x;
    this.y_ref = y;
    this.x = x * Tile_Dimension;
    this.y = y * Tile_Dimension;
    this.bomb = false;
    this.revealed = false;
    this.neighbor_bombs = 0;
    
    
    this.show = function(){
        // All of them are blank rects until revealed
        if (this.revealed == false){
            fill(cell_unrevealed_color);
            rect(this.x, this.y, Tile_Dimension, Tile_Dimension);
        }
        
        if (this.revealed == true && this.bomb == false){
            fill(cell_revealed_color);
            rect(this.x, this.y, Tile_Dimension, Tile_Dimension);
            
            // Renders the bomb count text within the cell
            textSize(Tile_Dimension);
            fill(0, 102, 153);
            text(this.neighbor_bombs, this.x + Tile_Dimension / 3, this.y + Tile_Dimension * 6 / 7);
    
        }
        
        if (this.revealed == true && this.bomb == true){
            fill(cell_revealed_color);
            rect(this.x, this.y, Tile_Dimension, Tile_Dimension);
            
            // Renders the bomb count text within the cell
            textSize(Tile_Dimension);
            fill(255, 0, 0);
            text('X', this.x + Tile_Dimension / 3, this.y + Tile_Dimension * 6 / 7);
        }
    }
    
    this.check_neighbors = function(){
        let count = 0;

        for (i = this.x_ref - 1; i < this.x_ref + 2; i++){
            for (j = this.y_ref - 1; j < this.y_ref + 2; j++){
                if (i >= 0 && j >= 0 && i < Tiles && j < Tiles){
                    if (cells[i][j].bomb == true){
                        count += 1;
                    }
                }
            }
        }
        this.neighbor_bombs = count;
            
    }
}


