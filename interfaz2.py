import tkinter as tk

def calculoFlexion():

    #ingreso de datos
    b = float(entry_b.get())
    h = float(entry_h.get())
    recubrimiento = float(entry_recubrimiento.get())
    fc = float(entry_fc.get())
    fy = float(entry_fy.get())
    Mu = float(entry_Mu.get())

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


    # Configurando el texto en las etiquetas de resultado
    etiqueta_resultado1.config(text=texto1)
    etiqueta_resultado2.config(text=texto2)
    etiqueta_resultado3.config(text=texto3)
    etiqueta_resultado4.config(text=texto4)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Flexión")

# Etiquetas y campos de entrada
etiqueta_b = tk.Label(ventana, text="Ancho (b) [m]:")
etiqueta_h = tk.Label(ventana, text="Altura (h) [m]:")
etiqueta_recubrimiento = tk.Label(ventana, text="Recubrimiento al eje [m]:")
etiqueta_fc = tk.Label(ventana, text="Resistencia del concreto (fc) [MPa]:")
etiqueta_fy = tk.Label(ventana, text="Resistencia del acero (fy) [MPa]:")
etiqueta_Mu = tk.Label(ventana, text="Momento flector (Mu) [KN-m]:")

entry_b = tk.Entry(ventana)
entry_h = tk.Entry(ventana)
entry_recubrimiento = tk.Entry(ventana)
entry_fc = tk.Entry(ventana)
entry_fy = tk.Entry(ventana)
entry_Mu = tk.Entry(ventana)

boton_calcular = tk.Button(ventana, text="Calcular", command=calculoFlexion)

# Etiquetas de resultado
etiqueta_resultado1 = tk.Label(ventana, text="")
etiqueta_resultado2 = tk.Label(ventana, text="")
etiqueta_resultado3 = tk.Label(ventana, text="")
etiqueta_resultado4 = tk.Label(ventana, text="")

# Colocar elementos en la ventana
etiqueta_b.grid(row=0, column=0)
entry_b.grid(row=0, column=1)
etiqueta_h.grid(row=1, column=0)
entry_h.grid(row=1, column=1)
etiqueta_recubrimiento.grid(row=2, column=0)
entry_recubrimiento.grid(row=2, column=1)
etiqueta_fc.grid(row=3, column=0)
entry_fc.grid(row=3, column=1)
etiqueta_fy.grid(row=4, column=0)
entry_fy.grid(row=4, column=1)
etiqueta_Mu.grid(row=5, column=0)
entry_Mu.grid(row=5, column=1)
boton_calcular.grid(row=6, columnspan=2)
etiqueta_resultado1.grid(row=7, columnspan=2)
etiqueta_resultado2.grid(row=8, columnspan=2)
etiqueta_resultado3.grid(row=9, columnspan=2)
etiqueta_resultado4.grid(row=10, columnspan=2)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
