#"Condicionales concatenados"

#edad=int(input("Introdizca su edad: "))

#if 0<edad<100:
    #print ("La edad es valida")
#else:
 #   print("Edad invalida")


#"Salario concatenado"

salario_presidente=int(input("Introdice el salario de presidente: "))
print ("Salario de presidente: " + str(salario_presidente))

salario_director=int(input("Introdice el salario del director: "))
print ("Salario del director: " + str(salario_director))

salario_jefe_area=int(input("Introdice el salario del jefe de area: "))
print ("Salario del jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("INtroduzca el salario del administrativo: "))
print ("Salario del administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo esta en orden")
else:
    print("Algo ha fallado en la empresa")
