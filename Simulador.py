import tkinter as tk
#import robot
from luz import luz
from tkinter import colorchooser
from tkinter import PhotoImage


#rehacer el codigo pero usando las clases para almacenar sus valores y no un diccionario 


#añadir borrar
#los puntos se diferencian al momento de borrar
#creo que me tocara hacer un arreglo para almacernar cada nuevo objeto que se cree
#para poder llamarlo dps 
#ubicaicones de los puntos de fin
puntos_fin = {}
luces = []


#recuerda agregar las validaciones de los datos ingresados
#puedo agregar mas informacion a este punto
#Obtension de informacion de todos los componentes

def obtener_informacion_luz():  
    luz_importada = luz(0, 250, 250, 0)  # Crear una nueva instancia de la clase luz con valores iniciales
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Ingresar Información")
    ventana_emergente.geometry("300x300")
    ventana_emergente.resizable(False, False)

    tk.Label(ventana_emergente, text="Ingrese la intensidad de la luz:").pack(pady=10)
    entrada_intensidad = tk.Entry(ventana_emergente)
    entrada_intensidad.pack(pady=5)

    tk.Label(ventana_emergente, text="Distancia maxima de la luz:").pack(pady=10)
    entrada_distancia = tk.Entry(ventana_emergente)
    entrada_distancia.pack(pady=5)

    def guardar_datos():
        intensidad = entrada_intensidad.get()
        distancia_maxima = entrada_distancia.get()
        luz_importada.setIntensidad(intensidad)
        luz_importada.setAlcanze(distancia_maxima)
        luces.append(luz_importada)
        ventana_emergente.destroy()

    tk.Button(ventana_emergente, text="Guardar", command=guardar_datos).pack(pady=20)

    def detalles():
        ventana_detalles = tk.Toplevel()
        ventana_detalles.geometry("410x200")
        ventana_detalles.resizable(False, False)
        ventana_detalles.title("Detalles")
        tk.Label(ventana_detalles, text="Intensidad de la luz:").pack(pady=10)
        tk.Label(ventana_detalles, text="Este valor representa que tanto brilla esta luz trabaja con valores entre 0 y 100").pack(pady=10)
        tk.Label(ventana_detalles, text="Distancia maxima de la luz:").pack(pady=10)
        tk.Label(ventana_detalles, text="La distancia de la luz se mide en Cm con valores entre 0 y 100").pack(pady=10)


    tk.Button(ventana_emergente, text="Informacion", command=detalles).pack(pady=10)
    añadir_punto_luz()
    return luz_importada


def obtener_informacion_calor():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Ingresar Información")

    tk.Label(ventana_emergente, text="Ingrese la información:").pack(pady=10)
    entrada = tk.Entry(ventana_emergente)
    entrada.pack(pady=5)

    def confirmar():
        informacion = entrada.get()
        ventana_emergente.destroy()
        añadir_punto_calor(informacion)

    tk.Button(ventana_emergente, text="Confirmar", command=confirmar).pack(pady=10)    

def Cambiar_a_simulacion():
    Menu_frame.destroy()
    Canvas.destroy()
    canvas_simulacion = tk.Canvas(Ventana_principal, highlightthickness=0, bg="white")
    canvas_simulacion.pack(expand=True, fill="both")
    print("Cambiando a simulación")


    #Recuperar la informacion de los puntos finales

#def obtener_informacion_color():
#   ventana_emergente = tk.Toplevel()
#   ventana_emergente.title("Ingresar Información")
#
#   tk.Label(ventana_emergente, text="Ingrese la información:").pack(pady=10)
#   entrada = tk.Entry(ventana_emergente)
#   entrada.pack(pady=5)
#
#   def confirmar():
#       informacion = entrada.get()
#       ventana_emergente.destroy()
#       añadir_punto_color(informacion)
#
#   tk.Button(ventana_emergente, text="Confirmar", command=confirmar).pack(pady=10)    

#recuerda hacer validaciones a la velocidad 
def obtener_informacion_robot():
    venta_emergente = tk.Toplevel()
    venta_emergente.title("Ingresar Información del robot")
    
    # Usar grid para todos los widgets
    tk.Label(venta_emergente, text="Cantidad de sensores:").grid(row=0, column=0, columnspan=3, pady=10)
    
    # Radio buttons for selecting the number of sensors
    sensores_var = tk.IntVar()
    tk.Radiobutton(venta_emergente, text="1", variable=sensores_var, value=1).grid(row=0, column=3, padx=10)
    tk.Radiobutton(venta_emergente, text="2", variable=sensores_var, value=2).grid(row=0, column=4, padx=10)
    tk.Radiobutton(venta_emergente, text="3", variable=sensores_var, value=3).grid(row=0, column=5, padx=10)
    
    tk.Label(venta_emergente, text="luz:").grid(row=2, column=0, columnspan=3, pady=10)
    luz_var = tk.BooleanVar()
    tk.Checkbutton(venta_emergente, variable=luz_var).grid(row=2, column=4, pady=10)
    
    tk.Label(venta_emergente, text="calor:").grid(row=4, column=0, columnspan=3, pady=10)
    calor_var = tk.BooleanVar()
    tk.Checkbutton(venta_emergente, variable=calor_var).grid(row=4, column=4, pady=10)
    
    tk.Label(venta_emergente, text="color:").grid(row=6, column=0, columnspan=3, pady=10)
    color_var = tk.BooleanVar()
    tk.Checkbutton(venta_emergente, variable=color_var).grid(row=6, column=4, pady=10)
    
    tk.Label(venta_emergente, text="velocidad:").grid(row=8, column=0, columnspan=3, pady=10)
    velocidad_var = tk.DoubleVar()
    tk.Entry(venta_emergente, textvariable=velocidad_var).grid(row=8, column=4, pady=10)
    
    def confirmar():
        informacion = {
            "sensores": sensores_var.get(),
            "luz": luz_var.get(),
            "calor": calor_var.get(),
            "color": color_var.get(),
            "velocidad": velocidad_var.get()
        }
        print("Información recopilada:", informacion)  # Imprimir para depuración
        añadir_robot()  # Llamar a añadir_robot con la información recopilada
        venta_emergente.destroy()
    
    tk.Button(venta_emergente, text="Confirmar", command=confirmar).grid(row=10, column=0, columnspan=3, pady=10)

#funciones para arrastrar las ventanas
#si no se se reucuperan las ultimas ubicaciones aca esta el problema

def arrastrar(event):
    event.widget.startX = event.x
    event.widget.startY = event.y

def on_drag(event):
    x = event.widget.winfo_x() - event.widget.startX + event.x
    y = event.widget.winfo_y() - event.widget.startY + event.y
    if x < 250:
        x = 250
    if y < 0:
        y = 0
    event.widget.place(x=x, y=y)
  
def on_drag_fin(event):
    x = event.widget.winfo_x()
    y = event.widget.winfo_y()
    # Actualizar la ubicación final en el diccionario
    puntos_fin[event.widget] = (x, y,puntos_fin[event.widget][2])

def añadir_robot():
    draggable_label = tk.Label(Canvas, text="Robot", bg="light blue", width=10, height=5)
    draggable_label.place(x=250, y=250)
    draggable_label.bind("<ButtonPress-1>", arrastrar)
    draggable_label.bind("<B1-Motion>", on_drag)
    draggable_label.bind("<ButtonRelease-1>", on_drag_fin)
    # Guardar la ubicación inicial
    puntos_fin[draggable_label] = (250, 250,"Robot")

def añadir_punto_fin():
    draggable_label = tk.Label(Canvas, text="Fin", bg="light green", width=10, height=5)
    draggable_label.place(x=250, y=250)
    draggable_label.bind("<ButtonPress-1>", arrastrar)
    draggable_label.bind("<B1-Motion>", on_drag)
    draggable_label.bind("<ButtonRelease-1>", on_drag_fin)
    # Guardar la ubicación inicial
    puntos_fin[draggable_label] = (250, 250,"fin")


def añadir_punto_luz():
    draggable_label = tk.Label(Canvas, text="Luz", bg="yellow", width=10, height=5)

    draggable_label.place(x=250, y=250)
    draggable_label.bind("<ButtonPress-1>", arrastrar)
    draggable_label.bind("<B1-Motion>", on_drag)
    draggable_label.bind("<ButtonRelease-1>", on_drag_fin)
    # Guardar la ubicación inicial junto con la información
    puntos_fin[draggable_label] = (250, 250, "luz")


def añadir_punto_calor():

    draggable_label = tk.Label(Canvas,text="Calor", bg="red", width=10, height=5)
    
    draggable_label.place(x=250, y=250)
    draggable_label.bind("<ButtonPress-1>", arrastrar)
    draggable_label.bind("<B1-Motion>", on_drag)
    draggable_label.bind("<ButtonRelease-1>", on_drag_fin)
    # Guardar la ubicación inicial
    puntos_fin[draggable_label] = (250, 250,"calor")


def añadir_punto_color():
    color = colorchooser.askcolor()[1]
    if color:
        # Crear un punto de color en el canvas
        punto = tk.Label(Canvas, bg=color, width=10, height=5)
        punto.place(x=250, y=250)
        punto.bind("<ButtonPress-1>", arrastrar)
        punto.bind("<B1-Motion>", on_drag)
        punto.bind("<ButtonRelease-1>", on_drag_fin)
        # Guardar la ubicación inicial
        puntos_fin[punto] = (250, 250,color)

def imprimir_puntos_luz():
    for widget, (x, y, text) in puntos_fin.items():
        if text == "luz":
            print(f"Texto: {text}, Ubicación: ({x}, {y})")

Ventana_principal = tk.Tk()
Ventana_principal.title("Simulador de robots de Braitenberg")
Ventana_principal.geometry("800x600")

# Crear un Canvas area de trabajo
# recordar el canvas tiene superpuesto un menu de opciones y pierde los primeros 250 pixeles en x y todos esos pixles en y
Canvas = tk.Canvas(Ventana_principal, highlightthickness=0,bg="white")
Canvas.pack(expand=True, fill="both")


# Crear un Frame para el menú de opciones 
Menu_frame = tk.Frame(Canvas, bg="lightgrey", width=250)
Menu_frame.pack(side="left", fill="y")

# Botones para agregar funciones al simulador
Boton_robot = tk.Button(Menu_frame, text="Robot", command=añadir_robot)
Boton_robot = tk.Button(Menu_frame, text="Robot", command=obtener_informacion_robot)
Boton_robot.place(x=10, y=10)

Boton_fin = tk.Button(Menu_frame, text="Fin", command=añadir_punto_fin)
Boton_fin.place(x=10, y=50)

Boton_luz = tk.Button(Menu_frame, text="Luz", command=añadir_punto_luz)
Boton_luz = tk.Button(Menu_frame, text="Luz", command=obtener_informacion_luz)
Boton_luz.place(x=10, y=90)

Boton_calor = tk.Button(Menu_frame, text="Calor", command=añadir_punto_calor)
Boton_calor = tk.Button(Menu_frame, text="Calor", command=obtener_informacion_calor)
Boton_calor.place(x=10, y=130)

Boton_color = tk.Button(Menu_frame, text="Color", command=añadir_punto_color)
#Boton_color = tk.Button(menu_frame, text="Color", command=obtener_informacion_color)
Boton_color.place(x=10, y=170)

boton_pasar_simluacion = tk.Button(Menu_frame, text="Pasar a simulacion", command=Cambiar_a_simulacion)
boton_pasar_simluacion.place(x=10, y=250)

#para confirmar que se este guardando su ubicacion
#Botón para imprimir las ubicaciones finales
Boton_imprimir = tk.Button(Menu_frame, text="Imprimir Ubicaciones", command=imprimir_puntos_luz)
Boton_imprimir.place(x=10, y=210)


Ventana_principal.mainloop()
#cambiar el boton incicio a robot
#agregar la funcionalidad de añadir un robot y sus caractaristicas
#en la funciones tienen tiene que estar en psuedocodigo inventarse 
 