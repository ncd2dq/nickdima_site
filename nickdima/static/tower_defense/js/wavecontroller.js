//This file provides all the game logic for sending waves at the tower
class WaveController{
    constructor(){
        this.wave = 1;
        this.max_waves = 5;
        this.initial_enemies = 5;
        this.next_wave_count = this.initial_enemies;
        this.difficulty = 1.5;
        this.level_up_difficulty = 2;
        
        this.count = 0;
        this.time_till_next_wave = 5;
        
        this.break_time = 5;
    }
    
    
    spawn_diver(){
        
        
    }
    
    spawn_bomber(){
        
        
    }
    
    spawn_simple(){
        
        
    }
    
    spawn_flock(){
        
        
    }
    
    waves_done(enemy_list, game_data){
        game_data.nextLevel();
        this.wave = 1;
        this.difficulty *= this.level_up_difficulty;
        
    }
    
    display_wave_count(){
        textSize(25);
        fill(0, 0, 0);
        text("Next Wave: " + this.time_till_next_wave, Canvas_Width * 4 / 5 - 50, 25);
        
        text("Wave: " + this.wave + "/" + this.max_waves, Canvas_Width * 4 / 5 + 115, 25);
    }
    
    
    create_wave(enemy_list, game_data){
        if(enemy_list.length == 0){
            this.count ++;
            if(this.count % FPS == 0){
                //Countdown till next wave in seconds
                this.time_till_next_wave--;
            }
            
            if(this.count / FPS == this.break_time){
                
                for(let i = 0; i < this.next_wave_count; i ++){
                    enemy_list.push(new SimpleEnemy(t));
                    //TESTING
                    enemy_list.push(new Bomber(t));
                }
                
                this.count = 0;
                if(this.wave < this.max_waves){
                    this.wave++;
                } else {
                    this.waves_done(enemy_list, game_data);
                    this.wave = 1;
                }
                this.next_wave_count = Math.floor(this.wave * this.difficulty) + this.initial_enemies;
                this.time_till_next_wave = this.break_time;
            }
        }
        
    }
    
    run(enemy_list, game_data){
        this.create_wave(enemy_list, game_data);
        this.display_wave_count();
    }
    
}
