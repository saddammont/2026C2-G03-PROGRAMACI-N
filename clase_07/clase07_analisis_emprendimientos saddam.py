"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

#La red EmprendeCR tiene varias sedes en Costa Rica. Cada sede registra ventas de lunes a viernes y una meta semanal.
#Al terminar, el programa debe construir un reporte que indique:
#
#Promedio diario de ventas.
#Porcentaje de cumplimiento de la meta.
#Clasificacion con condicionales.
#Provincias analizadas sin repetir.
#Ranking base con nombre de sede y total.
#Sede o sedes con la venta mas alta, incluyendo empates.
#La clase no busca solo imprimir datos. Busca practicar como un algoritmo convierte una lista de registros en informacion util para decidir.
#Total semanal vendido por sede.

from sedes import sedes
top_sucursal = ""
def calcular_total(lista_ventas):
    """recibo una lista y la sumo"""
    return sum(lista_ventas)

def calcular_promedio (lista_ventas):
    """recibo una lista de ventas y calculo su promedio"""
    return sum(lista_ventas)/len(lista_ventas)

def calcular_porcentaje_meta(ventas, meta):
    """calcula el porcentaje con respecto a la meta"""
    return ventas / meta * 100

def calcular_clasificacion(porcentaje):
    """"Clasifica el emprendimiento según porcentaje de cumplimiento de meta de ventas."""
    if porcentaje >=100:
        clasificacion = "Meta alcanzada, emprendimiento rentable"
    elif porcentaje > 80:
        clasificacion = "Observación, no se logró la meta."
    
        clasificacion = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCIÓN."
    return clasificacion

def imprimir_reporte(reporte):
    """Imprime el reporte final de ventas por emprendimiento"""
    print("\nREPORTE FINAL")
    print("-" * 60)
    for fila in reporte:
        print(f"Emprendimiento: {fila["nombre"].upper()}")
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total semanal: ₡{fila["total"]:,.2f}")
        print(f"Promedio diario: ₡{fila["promedio"]:,.2f}")
        print(f"Pordentaje cumplimiento: {fila["porcentaje"]:,.0f}%")
        print(f"Estado: {fila["estado"]}")
        print("-" * 60)
    print(f"cantidad de emprendimientos: {len(reporte)}")
    
def imprimir_top(ranking):
    for top in ranking:
        
        prueba = top[1]
        
        
    return prueba.replace(top,0)

# variables
provincias = set()
reporte = []
ranking = []
prueba = []






for emprendimiento in sedes:
    #emprendimiento = sedes[0]
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]
    sucursal = emprendimiento["nombre"]
    
    #procesamiento de variables
    total_emprendimiento = calcular_total(ventas)
    promedio_emprendimiento = calcular_promedio(ventas)
    porcentaje_meta = calcular_porcentaje_meta(total_emprendimiento, meta)
    clasificacion = calcular_clasificacion(porcentaje_meta)
    
    provincias.add(emprendimiento["provincia"])
    
    ranking.append((emprendimiento["nombre"],total_emprendimiento))
    
    
    
    reporte.append(
        {
            "nombre" : emprendimiento["nombre"],
            "provincia" : emprendimiento["provincia"],
            "tipo"  : emprendimiento["tipo"],
            "total" : total_emprendimiento,
            "promedio" : promedio_emprendimiento,
            "porcentaje" : porcentaje_meta,
            "estado" : clasificacion
        }
    )

#imprimir_reporte(reporte)
imprimir_top(ranking)


