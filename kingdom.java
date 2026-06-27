class Villager{
    private String name;
    private int coins;

    public Villager(String name, int coins){
        this.name = name;
        this.coins = coins;
    }

    public void loseCoins(int amt){
        coins -= amt;
    }

    public void receiveCoins(int amt){
        coins+=amt;
    }
}

class Goblin{
    private String name;
    private int stolenCoins;

    public Goblin(String name){
        this.name = name;
        this.stolenCoins = 0;
    }

    public stealCoins(Villager vill, int amt){
        stolenCoints+=amt;
        vill.loseCoins(amt);
    }

    public dropCoins(int amt){
        stolenCoins-=amt;
    }

}

class Knight{
    private String name;

    public Knight(String name){
        this.name = name;
    }

    private void returnCoins(int amt, Villager vill){
        vill.receiveCoins(amt);
    }

    public void attackGoblin(Villager vill, Goblin gob, int amt){
        vill.returnCoins(amt);
    }

}
