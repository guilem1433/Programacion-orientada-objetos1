import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

    abstract class Jugador {
        protected String eleccion;

        public String getEleccion() {
            return eleccion;
        }

        public abstract void jugar(String eleccion); //public
    }
    class JugadorHumano extends Jugador {

        @Override // change to Override
        public void jugar(String eleccion) {
            this.eleccion = eleccion.toLowerCase();
        }
    }
    //javaCopiarEditarimport java.utilł.Random; "not used line"
    class JugadorComputadora extends Jugador {

        @Override //turned to override
        public void jugar(String noUsado) {
            String[] opciones = {"piedra", "papel", "tijera"};
            Random rand = new Random();
            this.eleccion = opciones[rand.nextInt(opciones.length)];
        }
    }
    class Juego {
        private Jugador jugador1;
        private Jugador jugador2;

        public Juego(Jugador j1, Jugador j2) {
            this.jugador1 = j1;
            this.jugador2 = j2;
        }

        public String jugarRonda(String eleccionJugador) {
            jugador1.jugar(eleccionJugador);
            jugador2.jugar(null);

            String e1 = jugador1.getEleccion();
            String e2 = jugador2.getEleccion();

            String resultado;
            if (e1.equals(e2)) {
                resultado = "¡Empate!";
            } else if (
                    (e1.equals("piedra") && e2.equals("tijera")) ||
                            (e1.equals("papel") && e2.equals("piedra")) ||
                            (e1.equals("tijera") && e2.equals("papel"))
            ) {
                resultado = "¡Ganaste!";
            } else {
                resultado = "¡Perdiste!";
            }

            return "Tú elegiste: " + e1 + "\nComputadora eligió: " + e2 + "\n" + resultado;
        }
    }
    //javaCopiarEditarimport javax.swing.;import java.awt.;import java.awt.event.ActionEvent;import "not used
    java.awt.event.ActionListener;

    public class JuegoGUI extends JFrame { //public
        private JTextArea resultadoArea;
        private Juego juego;

        public JuegoGUI() {
            setTitle("Piedra, Papel o Tijera - POO");
            setSize(400, 300);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            setLayout(new BorderLayout());

            //Inicializar jugadores //bad commented,  in wrong line
            JugadorHumano jugadorHumano = new JugadorHumano(); //was commented
            JugadorComputadora jugadorComputadora = new JugadorComputadora();
            juego = new Juego(jugadorHumano, jugadorComputadora);

            // Área de resultado        resultadoArea = new JTextArea();
            resultadoArea.setEditable(false);
            resultadoArea.setFont(new Font("Arial", Font.PLAIN, 16));
            add(new JScrollPane(resultadoArea), BorderLayout.CENTER);

            JPanel panelBotones = new JPanel(); //was commented Jpanel, // paneljbottons
            String[] opciones = {"Piedra", "Papel", "Tijera"};
            for (String opcion : opciones) {
                JButton boton = new JButton(opcion);
                boton.addActionListener(new ActionListener() {
                    @Override //change to override
                    public void actionPerformed(ActionEvent e) { //public
                        String resultado = juego.jugarRonda(opcion);
                        resultadoArea.setText(resultado);
                    }
                });
                panelBotones.add(boton);
            }

            add(panelBotones, BorderLayout.SOUTH);
        }

        public static void main(String[] args) { //public
            SwingUtilities.invokeLater(() -> {
                JuegoGUI gui = new JuegoGUI();
                gui.setVisible(true);
            });
        }
    }

    void main() {
    }
