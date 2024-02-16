public class Games {
    private String name;
    private double price;
    private double playTime;
    private int playerCount;
    private double rating;

    public Games(String name, double price, double playTime, int playerCount, double rating) {
        this.name = name;
        this.price = price;
        this.playTime = playTime;
        this.playerCount = playerCount;
        this.rating = rating;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }

    public double getPlayTime() {
        return this.playTime;
    }

    public int getPlayerCount() {
        return this.playerCount;
    }

    public double getRating() {
        return this.rating;
    }

    public void setPrice(double price) {
        if (price < 0) {
            throw new IllegalArgumentException("Error: Price cannot be below $0.00");
        }
        else {
            this.price = price;
        }
    }
}
