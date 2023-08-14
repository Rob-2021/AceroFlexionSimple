def calculoFlexion():

    #ingreso de datos
    b = 0.2
    h = 0.4
    recubrimiento = 0.05
    fc = 20
    fy = 500
    Mu = 120

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

    print(texto1)
    print(texto2)
    print(texto3)
    print(texto4)
