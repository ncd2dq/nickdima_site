let Canvas_x = 801;
let Canvas_y = 801;
let Tiles = 20;
let Tile_Dimension = 40;
let cells = new Array(Tiles);
let cell_unrevealed_color = (245, 245, 245);
let cell_revealed_color = (200, 200, 200);
let hard = 0.4;
let medium = 0.25;
let easy = 0.1;
let first_click = true;
let difficulty = window.prompt("Please type the desired difficulty level (Case Sensitive)", "Hard, Medium, Easy");

function setup() {    
    createCanvas(Canvas_x, Canvas_y);
    
    // Create a 2D array with dimensions: Tiles x Tiles
    for (i = 0; i < Tiles; i++){
        cells[i] = new Array(Tiles);
    }
    
    // Iterate through 2D array and fill with cells
    for (i = 0; i < Tiles; i++){
        for (j = 0; j < Tiles; j++){
            cells[i][j] = new Cell(i, j);
        }
    }
    
}


function draw() {
    background(0, 0, 0);
    fill(255,0,0);
    
    // Show all cells in 2D array
    for (i = 0; i < Tiles; i++){
        for (j = 0; j < Tiles; j++){
            cells[i][j].show();
            
            if (cells[i][j].bomb == true && cells[i][j].revealed == true){
                noLoop();
                endsequence();
            }
        }
    }    
    
    /* / Score counter
    textSize(score_size);
    fill(0, 102, 153);
    text(score, Canvas_x / 2 - score_size, score_y_offset);
    */
}


function mousePressed(){
    // Logic that tests if a cell has been clicked on
    if (first_click == true){
        fill_with_bombs(difficulty, mouseX, mouseY);
        //count_all_bombs();
        
        for (i = 0; i < Tiles; i++){
            for (j = 0; j < Tiles; j++){
                if (mouseX >= cells[i][j].x 
                    && mouseX < (cells[i][j].x + Tile_Dimension) 
                    && mouseY >= cells[i][j].y 
                    && mouseY < (cells[i][j].y + Tile_Dimension)){
                    cells[i][j].revealed = true;               
                    cells[i][j].check_neighbors();
                }
            }
        }
        first_click = false;
        
    } else {
        for (i = 0; i < Tiles; i++){
            for (j = 0; j < Tiles; j++){
                if (mouseX >= cells[i][j].x 
                    && mouseX < (cells[i][j].x + Tile_Dimension) 
                    && mouseY >= cells[i][j].y 
                    && mouseY < (cells[i][j].y + Tile_Dimension)){
                    cells[i][j].revealed = true;               
                    cells[i][j].check_neighbors();
                }
            }
        }
    }
}

function fill_with_bombs(difficulty, x, y){
    // Determine what cell they first clicked on
    let cell_x_ref;
    let cell_y_ref;
    // apparently i don't need the else clauses???
    if (x % 1 == 0){
        cell_x_ref = Math.floor(x / Tile_Dimension);
    }
    if (y % 1 == 0){
        cell_y_ref = Math.floor(y / Tile_Dimension);
    }

    // Fill cells with bombs probabilisitically as long as they weren't the first clicked on
    if (difficulty == "Hard"){
        for (i = 0; i < Tiles; i++){
            for (j = 0; j < Tiles; j++){
                if (Math.random() < hard && (j != cell_y_ref || i != cell_x_ref)){
                    cells[i][j].bomb = true;
                }
            }
        }
    } else if (difficulty == "Medium"){
        for (i = 0; i < Tiles; i++){
            for (j = 0; j < Tiles; j++){
                if (Math.random() < medium && (i != cell_x_ref || j != cell_y_ref) ){
                    cells[i][j].bomb = true;
                }
            }
        }
    } else {
        for (i = 0; i < Tiles; i++){
            for (j = 0; j < Tiles; j++){
                if (Math.random() < easy && (i != cell_x_ref || j != cell_y_ref)){
                    cells[i][j].bomb = true;
                }
            }
        }
    }
}

/*
function count_all_bombs(){
    for (i = 0; i < Tiles; i++){
        for (j = 0; j < Tiles; j++){
            
        }
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
*/

function selfdestruct(){
    location.reload();
}

function endsequence(){
    alert("You clicked on a bomb");
    setTimeout(selfdestruct, 1500);
}