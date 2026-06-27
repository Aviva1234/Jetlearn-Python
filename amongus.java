//import java.util.ArrayList;

class Player{
    private String color;
    
    public Player(String color){
        this.color = color;
    }
}

class Crewmate extends Player{
    private int tasks;

    public Crewmate(String color){
        this.color = color;
        this.tasks = 5;
    }

    public void completeTask(){
        tasks--;
    }
}

class Impostor extends Player{
    public void kill(Crewmate mate){
        mate.delete();
    }
}

String[] colors = new {"blue", "green", "yellow", "orange", "red", "pink", "cyan", "purple"};

class Game{
    

    public createGame(int players){
        //crewmates array and impostors array
        ArrayList<Player> players = new ArrayList<Player>();
        for(int i=0; i<players; i++){
            players.add(new Player(colors[i]));
        }
    }
}