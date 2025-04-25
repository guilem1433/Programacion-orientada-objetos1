Algoritmo main13
    
    workers <- 50
    nomina <- 0
    worked_hours<- 0
	
    
    Escribir "nomina calculation"
	
    
    Mientras workers > 0 Hacer
        
        Escribir "enter worked hours", (51 - Numero_Obreros), ":"
        Leer worked_hours
		
        
        salary <- worked_hours * 30000
		
        
        Total_Nomina <- Total_Nomina + salary
		
        
        Escribir "worker ", ": worked hours = ", worked_hours, ", Salario = ", salary
		
    FinMientras
	
    Escribir "Total Nómina: ", Total_Nomina, " bolívares"
FinAlgoritmo