#"Programa evaluador: Becas (and/or)"

#print("-->Programa de becas<--")
#distancia=int(input("Ingrese la distancia (en kilometros) de su hogar a la escuela: "))
#hermanos=int(input("Ingrese la cantidad de hermanos que tiene: "))
#salario=int(input("Ingrese el salario anual que recibe su tutor: $"))

#print ("Distancia: "+ str (distancia)+  "." )
#print("Hermanos: "+ str(hermanos)+ ".")
#print("Salario: $"+ str(salario)+ ".")

#if distancia>40 and hermanos>2 or salario<=20000:
#   print("Usted es acredor de la beca.")
#else:
#    print ("No, ustes no es acredor a la beca.")




#" : Asignatura Optativa (in)"

print("-->Asignaturas Optativas<--")
print("Informática gráfica  --  Pruebas de software  --  Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura que desees cursar: ")
asignatura=opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print ("Asignatura elegida: "+ asignatura)
else:
    print("La asignatura escogida no esta contempada.")
