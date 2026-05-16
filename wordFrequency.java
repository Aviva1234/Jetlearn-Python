public int findFrequency(String message){
    String[] words = message.split(" ");
    int count = 0;
    for(String word : words){
        if (word.equals(message)){
            count++;
        }
    }
    return count;
}