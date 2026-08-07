"""Programa principal del proyecto modular BCCR."""

from lectura_datos import cargar_tabla_bccr, mostrar_top_10
from limpieza_datos import limpiar_datos, resumir_por_tipo_entidad 

def ejecutar():
    """Cargar los datos y presenta el menu del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos = limpiar_datos(datos_crudos)
    
    while True:
        print("\n PROYECTO DE ANALISIS BCCR")
        print("1, Mostrar primeras 10 entidades limpias.")
        print("2. Promedio por tipo de entidad.")
        print("3. Mostrar entidades finacieras con diferencial mayot al promedio.")
        print("4. Mostrar lista entidades y exportar CSV.")
        print("5. Graficar")
        print("6. Salir")
        
        opcion = input("Seleccione un opcion: ").strip()
        
        if opcion == "1":
            print(mostrar_top_10(datos))
        elif opcion == "2":
            promedios = resumir_por_tipo_entidad(datos)
            print(f"Promedio general del diferencial: {promedios[0]:.2f}") 
            print("Promedio por tipo de entidad:")
            print(promedios[1].to_string(index=False))
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("Analisis Finalizado")
            input("Presione enter para salir")
            break
        else:
            print("Opcion invalida. Escriba un numero del 1 al 6.")
        input("\n Presione enter para continuar.... \n")

if __name__ == "__main__":
    ejecutar()