Public Class Form1
    Dim numerouno As Double
    Dim numerodos As Double
    Dim total As Double
    Dim operacion As Double
    Dim memoria As Double = 0


    Private Sub button20_Click(sender As Object, e As EventArgs) Handles button20.Click
        Me.textBox1.Text = textBox1.Text & "0"
    End Sub

    Private Sub button15_Click(sender As Object, e As EventArgs) Handles button15.Click
        Me.textBox1.Text = textBox1.Text & "2"
    End Sub

    Private Sub button17_Click(sender As Object, e As EventArgs) Handles button17.Click
        Me.textBox1.Text = textBox1.Text & "7"
    End Sub

    Private Sub button19_Click(sender As Object, e As EventArgs) Handles button19.Click
        Me.textBox1.Text = textBox1.Text & "1"
    End Sub

    Private Sub button11_Click(sender As Object, e As EventArgs) Handles button11.Click
        Me.textBox1.Text = textBox1.Text & "3"
    End Sub

    Private Sub button18_Click(sender As Object, e As EventArgs) Handles button18.Click
        Me.textBox1.Text = textBox1.Text & "4"
    End Sub

    Private Sub button14_Click(sender As Object, e As EventArgs) Handles button14.Click
        Me.textBox1.Text = textBox1.Text & "5"
    End Sub

    Private Sub button10_Click(sender As Object, e As EventArgs) Handles button10.Click
        Me.textBox1.Text = textBox1.Text & "6"
    End Sub

    Private Sub button13_Click(sender As Object, e As EventArgs) Handles button13.Click
        Me.textBox1.Text = textBox1.Text & "8"
    End Sub

    Private Sub button9_Click(sender As Object, e As EventArgs) Handles button9.Click
        Me.textBox1.Text = textBox1.Text & "9"
    End Sub

    Private Sub button16_Click(sender As Object, e As EventArgs) Handles button16.Click
        Me.textBox1.Text = textBox1.Text & "."
        button16.Enabled = False
    End Sub

    Private Sub button8_Click(sender As Object, e As EventArgs) Handles button8.Click
        button16.Enabled = True
        button12.Enabled = True
        textBox2.Text = "+"
        operacion = 2
        numerouno = Val(textBox1.Text)
        textBox1.Clear()

    End Sub

    Private Sub button7_Click(sender As Object, e As EventArgs) Handles button7.Click
        button16.Enabled = True
        button12.Enabled = True
        textBox2.Text = "-"
        operacion = 3
        numerouno = Val(textBox1.Text)
        textBox1.Clear()

    End Sub

    Private Sub button6_Click(sender As Object, e As EventArgs) Handles button6.Click
        button16.Enabled = True
        button12.Enabled = True
        textBox2.Text = "*"
        operacion = 4
        numerouno = Val(textBox1.Text)
        textBox1.Clear()

    End Sub

    Private Sub button5_Click(sender As Object, e As EventArgs) Handles button5.Click
        button16.Enabled = True
        button12.Enabled = True
        textBox2.Text = "/"
        operacion = 5
        numerouno = Val(textBox1.Text)
        textBox1.Clear()

    End Sub

    Private Sub button12_Click(sender As Object, e As EventArgs) Handles button12.Click
        textBox1.Text = "-" & textBox1.Text
        button12.Enabled = False
    End Sub

    Private Sub button4_Click(sender As Object, e As EventArgs) Handles button4.Click
        numerodos = Val(textBox1.Text)
        If operacion = 2 Then
            total = numerouno + numerodos
            textBox1.Text = total
        ElseIf operacion = 3 Then
            total = numerouno - numerodos
            textBox1.Text = total
        ElseIf operacion = 4 Then
            total = numerouno * numerodos
            textBox1.Text = total
        ElseIf operacion = 5 Then
            total = numerouno / numerodos
            textBox1.Text = total
        End If
    End Sub

    Private Sub button2_Click(sender As Object, e As EventArgs) Handles button2.Click
        operacion = 6
        If operacion = 6 Then
            numerouno = Val(textBox1.Text)
            textBox1.Text = System.Math.Sqrt(numerouno)
        End If
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Label1.Visible = False
    End Sub

    Private Sub button3_Click(sender As Object, e As EventArgs) Handles button3.Click
        If operacion = 0 Then
            ' Solo hay un número, calcula su porcentaje directamente
            textBox1.Text = Val(textBox1.Text) / 100
            Exit Sub
        End If

        numerodos = Val(textBox1.Text)

        Select Case operacion
            Case 2 ' Suma
                total = numerouno + (numerouno * numerodos / 100)
            Case 3 ' Resta
                total = numerouno - (numerouno * numerodos / 100)
            Case 4 ' Multiplicación
                total = numerouno * (numerodos / 100)
            Case 5 ' División
                If numerodos <> 0 Then
                    total = numerouno / (numerodos / 100)
                Else
                    textBox1.Text = "Error"
                    Exit Sub
                End If
            Case Else
                textBox1.Text = "Error"
                Exit Sub
        End Select

        textBox1.Text = total
    End Sub

    Private Sub button1_Click(sender As Object, e As EventArgs) Handles button1.Click
        button16.Enabled = True
        button12.Enabled = True
        textBox1.Clear()
    End Sub

    Private Sub button21_Click(sender As Object, e As EventArgs) Handles button21.Click
        memoria = 0
    End Sub

    Private Sub button22_Click(sender As Object, e As EventArgs) Handles button22.Click
        textBox1.Text = memoria.ToString()
    End Sub

    Private Sub button23_Click(sender As Object, e As EventArgs) Handles button23.Click
        memoria = Val(textBox1.Text)
    End Sub

    Private Sub button24_Click(sender As Object, e As EventArgs) Handles button24.Click
        memoria = memoria + Val(textBox1.Text)
    End Sub

    Private Sub button27_Click(sender As Object, e As EventArgs) Handles button27.Click
        Dim num As Double = Val(textBox1.Text)
        If num <> 0 Then
            textBox1.Text = (1 / num).ToString()
        Else
            MsgBox("No se puede dividir entre cero")
        End If
    End Sub

    Private Sub button26_Click(sender As Object, e As EventArgs) Handles button26.Click
        textBox1.Clear()
    End Sub

    Private Sub button25_Click(sender As Object, e As EventArgs) Handles button25.Click
        If textBox1.Text.Length > 0 Then
            textBox1.Text = textBox1.Text.Substring(0, textBox1.Text.Length - 1)
        End If
    End Sub
End Class
