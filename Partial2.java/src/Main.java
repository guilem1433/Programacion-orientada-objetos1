// File: Main.java
public class Main {
    public static void main(String[] args) {
        Boleteria boleteria = new Boleteria(120.0, 100.0);
        boleteria.ticket("2025-06-09", 5);
        boleteria.ticketPromo("2025-06-09", 3);
        boleteria.resumen();
    }
}