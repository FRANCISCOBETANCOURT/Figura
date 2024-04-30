
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


# Función para cargar la primera fila de un archivo Excel
def cargar_primera_fila(nombre_archivo):
    wb = openpyxl.load_workbook(nombre_archivo)
    sheet = wb.active
    primera_fila = []
    for cell in sheet[1]:
        primera_fila.append(cell.value)
    return primera_fila

# Cargar solo la primera fila de cada archivo Excel en variables
t = cargar_primera_fila('datost.xlsx')
x1 = cargar_primera_fila('datosx1.xlsx')
x2 = cargar_primera_fila('datosx2.xlsx')
f = cargar_primera_fila('datos.xlsx')

# Crear subplot
plt.figure(figsize=(10, 10))

plt.subplot(1, 3, 1)  # Subplot 1
plt.plot(t, x1, 'k-', label='x1')  # 'k-' para curva negra
plt.xlabel('t')
plt.ylabel('x1')
plt.grid(True)  # Agregar grid
plt.legend()

plt.subplot(1, 3, 2)  # Subplot 2
plt.plot(t, x2, 'k-', label='x2')  # 'k-' para curva negra
plt.xlabel('t')
plt.ylabel('x2')
plt.grid(True)  # Agregar grid
plt.legend()

plt.subplot(1, 3, 3)  # Subplot 3
plt.plot(t, f, 'k-', label='f')  # 'k-' para curva negra
plt.xlabel('t')
plt.ylabel('f')
plt.grid(True)  # Agregar grid
plt.legend()

plt.tight_layout()  # Ajustar el diseño para evitar superposiciones
plt.show()

