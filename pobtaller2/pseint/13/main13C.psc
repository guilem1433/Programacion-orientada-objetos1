Algoritmo main13C
	workers <- 50
	Total_Nomina <- 0
	worked_hours <- 0
	Escribir 'Nomina Calculation'
	contador <- 1
	Repetir
		Escribir 'Enter worked hours for worker ', contador, ':'
		Leer worked_hours
		salary <- worked_hours*30000
		Total_Nomina <- Total_Nomina+salary
		Escribir 'Worker ', contador, ': Worked hours = ', worked_hours, ', Salary = ', salary
		contador <- contador+1
	Hasta Que contador>workers
	Escribir 'Total Nomina: ', Total_Nomina, ' bolívares'
FinAlgoritmo
