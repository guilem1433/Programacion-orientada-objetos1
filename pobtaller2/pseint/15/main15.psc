Algoritmo main15
	years <- 0
	months <- 0
	weeks <- 0
	days <- 0
	total_days <- 0
	Escribir 'Enter the number of days: '
	Leer total_days
	days <- total_days
	Mientras days>=365 Hacer
		years <- years+1
		days <- days-365
	FinMientras
	Mientras days>=30 Hacer
		months <- months+1
		days <- days-30
	FinMientras
	Mientras days>=7 Hacer
		weeks <- weeks+1
		days <- days-7
	FinMientras
	Escribir 'In ', total_days, ' days there are:'
	Escribir years, ' years, ', months, ' months, ', weeks, ' weeks and ', days, ' days.'
FinAlgoritmo
