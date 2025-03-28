import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calculator extends JFrame {
    private JPanel panel;
    private JTextField txtNum1;
    private JTextField txtNum2;
    private JButton btnBorrar;
    private JTextField txtTotal;
    private JButton btnSumar;
    private JButton btnRestar;
    private JButton btnMultiplicar;
    private JButton btnDividir;
    private Operacion objOperacion;

    public Calculator() {
        setTitle("Calculadora");
        setSize(400, 330);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        panel = new JPanel();
        setContentPane(panel);
        panel.setLayout(null);

        JLabel lblNum1 = new JLabel("Número 1:");
        lblNum1.setBounds(30, 30, 80, 25);
        panel.add(lblNum1);

        txtNum1 = new JTextField();
        txtNum1.setBounds(120, 30, 150, 25);
        panel.add(txtNum1);

        JLabel lblNum2 = new JLabel("Número 2:");
        lblNum2.setBounds(30, 70, 80, 25);
        panel.add(lblNum2);

        txtNum2 = new JTextField();
        txtNum2.setBounds(120, 70, 150, 25);
        panel.add(txtNum2);

        btnSumar = new JButton("Sumar");
        btnSumar.setBounds(30, 110, 100, 25);
        panel.add(btnSumar);

        btnRestar = new JButton("Restar");
        btnRestar.setBounds(150, 110, 100, 25);
        panel.add(btnRestar);

        btnMultiplicar = new JButton("Multiplicar");
        btnMultiplicar.setBounds(30, 150, 100, 25);
        panel.add(btnMultiplicar);

        btnDividir = new JButton("Dividir");
        btnDividir.setBounds(150, 150, 100, 25);
        panel.add(btnDividir);

        btnBorrar = new JButton("Borrar");
        btnBorrar.setBounds(90, 190, 100, 25);
        panel.add(btnBorrar);

        JLabel lblTotal = new JLabel("Total:");
        lblTotal.setBounds(30, 230, 80, 25);
        panel.add(lblTotal);

        txtTotal = new JTextField();
        txtTotal.setBounds(120, 230, 150, 25);
        txtTotal.setEditable(false);
        panel.add(txtTotal);

        objOperacion = new Operacion();

        btnSumar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1 = Integer.parseInt(txtNum1.getText());
                int num2 = Integer.parseInt(txtNum2.getText());
                int resultado = objOperacion.sumar(num1, num2);
                txtTotal.setText(String.valueOf(resultado));
            }
        });

        btnRestar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1 = Integer.parseInt(txtNum1.getText());
                int num2 = Integer.parseInt(txtNum2.getText());
                int resultado = objOperacion.restar(num1, num2);
                txtTotal.setText(String.valueOf(resultado));
            }
        });

        btnMultiplicar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1 = Integer.parseInt(txtNum1.getText());
                int num2 = Integer.parseInt(txtNum2.getText());
                int resultado = objOperacion.multiplicar(num1, num2);
                txtTotal.setText(String.valueOf(resultado));
            }
        });

        btnDividir.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1 = Integer.parseInt(txtNum1.getText());
                int num2 = Integer.parseInt(txtNum2.getText());
                try {
                    double resultado = objOperacion.dividir(num1, num2);
                    txtTotal.setText(String.valueOf(resultado));
                } catch (ArithmeticException ex) {
                    txtTotal.setText("Error");
                }
            }
        });

        btnBorrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                txtNum1.setText("");
                txtNum2.setText("");
                txtTotal.setText("");
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Calculator().setVisible(true));
    }
}