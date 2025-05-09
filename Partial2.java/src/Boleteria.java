// File: Boleteria.java
import java.io.PrintStream;

public class Boleteria {
    public double valor = 0.0;
    public double valorPromo = 0.0;
    public double totalPromo = 0.0;
    public double totalComun = 0.0;
    public StringBuffer sb = new StringBuffer();

    public Boleteria() {
        open(100.0, 80.0);
    }

    public Boleteria(double valorComun) {
        open(valorComun, valorComun * 0.8);
    }

    public Boleteria(double valorComun, double valorPromo) {
        open(valorComun, valorPromo);
    }

    public void setValor(double v) {
        valor = v;
    }

    public void setValorPromo(double vp) {
        valorPromo = vp;
    }

    public double getValor() {
        return valor;
    }

    public double getValorPromo() {
        return valorPromo;
    }

    public void open(final double valorComun, final double valorPromo) {
        setValor(valorComun);
        setValorPromo(valorPromo);
        inicialize();
    }

    public void inicialize() {
        totalComun = 0.0;
        totalPromo = 0.0;
        sb.delete(0, sb.length());
    }

    public double ticket(String fecha, int n) {
        totalComun += getValor() * n;
        sb.append(fecha + "\t" + "C\t" + n + "\t" + getValor() + "\t" + (getValor() * n) + "\n");
        return getValor() * n;
    }

    public double ticketPromo(String fecha, int n) {
        totalPromo += getValorPromo() * n;
        sb.append(fecha + "\t" + "P\t" + n + "\t" + getValorPromo() + "\t" + (getValorPromo() * n) + "\n");
        return getValorPromo() * n;
    }

    public void resumen() {
        PrintStream p = System.out;
        p.println("\t\t\t the Avengers\n");
        p.println("fecha\t\ttipo\tCantidad.\tvalor\tsubtotal");
        p.println(sb.toString());
        p.println("\t\ttotal tickets comunes : \t" + totalTicket());
        p.println("\t\ttotal tickets promo: \t" + totalTicketsPromo());
        p.println("\t\ttotal general: \t" + total());
    }

    public double total() {
        return totalTicket() + totalTicketsPromo();
    }

    public double totalTicket() {
        return totalComun;
    }

    public double totalTicketsPromo() {
        return totalPromo;
    }
}