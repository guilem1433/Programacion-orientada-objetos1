Algoritmo CalculateDaysFixed
	years <- 0
	months <- 0
	weeks <- 0
	days <- 0
	total_days <- 0
	Escribir 'Enter the number of days: '
	Leer total_days
	days <- total_days
	Repetir
		Si days>=365 Entonces
			years <- years+1
			days <- days-365
		FinSi
	Hasta Que days<365
	Repetir
		Si days>=30 Entonces
			months <- months+1
			days <- days-30
		FinSi
	Hasta Que days<30
	Repetir
		Si days>=7 Entonces
			weeks <- weeks+1
			days <- days-7
		FinSi
	Hasta Que days<7
	Escribir 'In ', total_days, ' days there are:'
	Escribir years, ' years, ', months, ' months, ', weeks, ' weeks and ', days, ' days.'
FinAlgoritmo
