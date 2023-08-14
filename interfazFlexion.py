import tkinter as tk

def calculoFlexion():

    #ingreso de datos
    b = float(entry1.get())
    h = float(entry2.get())
    recubrimiento = float(entry3.get())
    fc = float(entry4.get())
    fy = float(entry5.get())
    Mu = float(entry6.get())

    #calculo de seccion de acero a flexion
    Mu = Mu/1000
    d = h-recubrimiento
    dp = recubrimiento
    gamma = 0.85
    eu = 0.003
    Es = 200e3

    if fc <= 28:
        beta1 = 0.85
    elif fc >= 55:
        beta1 = 0.65
    else:
        beta1 = 0.85-0.05*(fc-28)/7

    roMax = gamma*beta1*fc/fy*eu/(eu+0.005)
    AsMax = roMax*b*d
    fiMmax = 0.9*AsMax*fy*(d-AsMax*fy/(2*gamma*fc*b))

    AsMin1 = fc**0.5/(4*fy)*b*d
    AsMin2 = 1.4*b*d/fy

    AsMin = max(AsMin1, AsMin2)

    if Mu < fiMmax:
        numerador = 0.9*d-(0.81*d**2-1.8*Mu/(gamma*fc*b))**0.5
        denominador =0.9*fy/(gamma*fc*b)
        As = numerador/denominador

        texto1 = "Acero a traccion = " + str(round(As*1e4,2)) + "[cm2]"
        texto2 = "Acero a compresion = 0 [cm2]"
        texto3 = "Acero minimo a traccion = " + str(round(AsMin*1e4,2)) + "[cm2]"
        texto4 = "La viga no necesita acero a compresion"

    else:
        M2 = (Mu-fiMmax)/0.9
        As2 = M2/(fy*(d-dp))
        As = AsMax+As2
        Asp = As2
        roY = gamma*fc*fy*beta1*eu/(eu-fy/Es)*dp/d+Asp/(b*d)
        ro = As/(b*d)

        if ro > roY:
            texto1 = "Acero a traccion = " + str(round(As*1e4,2)) + "[cm2]"
            texto2 = "Acero a compresion = " + str(round(Asp*1e4,2)) + "[cm2]"
            texto3 = "Acero minimo a traccion = " + str(round(AsMin*1e4,2)) + "[cm2]"
            texto4 = "La viga necesita acero a compresion. As' fluye"

        else:
            a = (As-Asp)*fy/(gamma*fc*b)
            c = a/beta1
            fsp = eu*Es*(c-dp)/c
            AsRev = Asp*fy/fsp

            texto1 = "Acero a traccion = " + str(round(As*1e4,2)) + "[cm2]"
            texto2 = "Acero a compresion = " + str(round(Asp*1e4,2)) + "[cm2]"
            texto3 = "Acero minimo a traccion = " + str(round(AsMin*1e4,2)) + "[cm2]"
            texto4 = "La viga necesita acero a compresion. As' no fluye"

    etiqueta_resultado1.config(text=texto1)
    etiqueta_resultado2.config(text=texto2)
    etiqueta_resultado3.config(text=texto3)
    etiqueta_resultado4.config(text=texto4) 

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Acero por Flexion Simple")

# Etiquetas
etiqueta1 = tk.Label(ventana, text="b[m]:")
etiqueta2 = tk.Label(ventana, text="h[m]:")
etiqueta3 = tk.Label(ventana, text="recub. al eje[m]:")
etiqueta4 = tk.Label(ventana, text="fc' [MPa]:")
etiqueta5 = tk.Label(ventana, text="fy [MPa]:")
etiqueta6 = tk.Label(ventana, text="Mu [KN-m]:")
etiqueta_resultado1 = tk.Label(ventana, text="")
etiqueta_resultado2 = tk.Label(ventana, text="")
etiqueta_resultado3 = tk.Label(ventana, text="")
etiqueta_resultado4 = tk.Label(ventana, text="")

# Campos de entrada
entry1 = tk.Entry(ventana)
entry2 = tk.Entry(ventana)
entry3 = tk.Entry(ventana)
entry4 = tk.Entry(ventana)
entry5 = tk.Entry(ventana)
entry6 = tk.Entry(ventana)

# Botón para calcular la suma
boton_calcular = tk.Button(ventana, text="Calcular Suma", command=calculoFlexion)

# Colocar elementos en la ventana
etiqueta1.pack()
entry1.pack()
etiqueta2.pack()
entry2.pack()
etiqueta3.pack()
entry3.pack()
etiqueta4.pack()
entry4.pack()
etiqueta5.pack()
entry5.pack()
etiqueta6.pack()
entry6.pack()
boton_calcular.pack()
etiqueta_resultado1.pack()
etiqueta_resultado2.pack()
etiqueta_resultado3.pack()
etiqueta_resultado4.pack()

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
