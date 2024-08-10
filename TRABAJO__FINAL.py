# Listas para libros
cod_lib_list = ["L001", "L002", "L003"]
libro_list = ["LA ILIADA", "CIEN AÑOS", "JUAN GAVIOTA"]
autor_list = ["HOMERO", "GABRIEL GARCIA", "RICHARD BACH"]
tomo_list = ["300", "967", "970"]
opin_lib_list = ["BUENA", "BUENA", "MALA"]

# Listas para usuarios
dni_usu_list = ["12122323", "23233434", "65653423", "76879809", "12327687"]
nom_usu_list = ["JEISON", "NICOLAS", "ANDRES", "LUISA", "DIANA"]
apl_usu_list = ["RUIZ", "FARFAN", "GUIDO", "POLO", "ROMERO"]
tel_usu_list = ["901901901", "987987987", "945945945", "943932932", "965786654"]

# Listas para documentos
num_doc_list = ["S001", "S002", "S003"]
gen_solic = ["FANTASIA", "AUTOSUPERACIÓN", "AUTOBIOGRAFÍA"]
libro_solic = ["EL PRINCIPITO", "HÁGASE RICO", "MALCOM X"]
autor_solic = ["ANTOINE DE SAINT", "NAPOLEON HILL", "MALCOM X"]

# inicio
# libros
# usuarios
# documentos
# buscar_libros
# retirar_libros
# devolver_libros
# lista_libros
# buscar_x_cod
# buscar_x_nombre
# buscar_x_autor
# reg_usuario
# validar_dni
# list_usuarios
# baja_usuario
# doc_solicit
# lista_solicitudes
# cancel_solic


# =======//===================//================//================//============//
def inicio():
    print("-------------------------------------------------")
    print("------------ SISTEMA DE BIBLIOTECA --------------")
    print("------------  1. LIBROS          ----------------")
    print("------------  2. USUARIOS        ----------------")
    print("------------  3. DOCUMENTOS      ----------------")
    print("------------  4. SALIR           ----------------")
    print("-------------------------------------------------")
    op = int(input("Elija un Módulo de su interés: "))
    if op == 1:
        print("\nUsted ha elegido el Módulo LIBROS")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
        libros()
    else:
        if op == 2:
            print("\nUsted ha elegido el Módulo USUARIOS")
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            usuarios()
        else:
            if op == 3:
                print("\nUsted ha elegido el Módulo DOCUMENTOS")
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                documentos()
            else:
                if op >= 4:
                    print("\nUsted ha terminado el proceso.")
                    print("Gracias")
                    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                    exit


# =======//===================//================//================//============//
def libros():
    print("-------------------------------------------------")
    print("------------ MÓDULO DE LIBRO   ------------------")
    print("------------  1. BUSCAR        ------------------")
    print("------------  2. RETIRAR       ------------------")
    print("------------  3. DEVOLVER      ------------------")
    print("------------  4. BIBLIOTECA    ------------------")
    print("------------  5. SALIR         ------------------")
    print("-------------------------------------------------")
    oa = int(input("\nSeñale que acción quiere realizar: "))
    if oa == 1:
        print("\nUsted ha elegido BUSCAR un libro")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
        buscar_libros()
    else:
        if oa == 2:
            print("\nUsted ha elegido RETIRAR un libro")
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            retirar_libro()
        else:
            if oa == 3:
                print("\nUsted ha elegido DEVOLVER un libro")
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                devolver_libro()
            else:
                if oa == 4:
                    print("\nUsted ha elegido MOSTRAR BIBLIOTECA")
                    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
                    lista_libros()
                else:
                    if oa == 5:
                        inicio()
                    else:
                        print("¡Error!\nOpción Inválida")
                        oa = int(input("Señale que acción quiere realizar: "))


# =======//===================//================//================//============//
def buscar_libros():
    print("---------------------------")
    print("---- BUSCAR LIBRO POR----- ")
    print("-----  1. CÓDIGO     ------")
    print("-----  2. NOMBRE     ------")
    print("-----  3. AUTOR      ------")
    print("-----  4. SALIR      ------")
    print("---------------------------")
    ot = int(input("Ingrese por cual parámetro desea BUSCAR un libro: "))
    if ot == 1:
        print("\nUsted ha elegido buscar por CÓDIGO")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
        buscar_x_cod()
    else:
        if ot == 2:
            print("\nUsted ha elegido buscar por NOMBRE DE LIBRO")
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            buscar_x_nombre()
        else:
            if ot == 3:
                print("\nUsted ha elegido buscar por AUTOR")
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
                buscar_x_autor()
            else:
                if ot == 4:
                    libros()
                else:
                    print("¡Error!\nOpción Inválida\n")
                    buscar_libros()


# =======//===================//================//================//============//
def buscar_x_cod():
    x = input("Ingrese el CÓDIGO del libro: ").upper()
    cod_disp = False
    for i in range(len(cod_lib_list)):
        if x == cod_lib_list[i]:
            cod_disp = True
            print("\n=*=*=*= EL LIBRO ESTÁ DISPONIBLE =*=*=*=*=\n")
            print("CÓDIGO: ", cod_lib_list[i])
            print("NOMBRE DEL LIBRO: ", libro_list[i])
            print("AUTOR: ", autor_list[i])
            print("TOMO: ", tomo_list[i])
            print("OPINIÓN: ", opin_lib_list[i])
            oq = input("\n¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
            if oq == "SI" or oq == "SÍ":
                buscar_libros()
            else:
                libros()
    if not cod_disp:
        print("\n=*=*=*= EL LIBRO |NO| ESTÁ DISPONIBLE =*=*=*=*=\n")
        oq = input("¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
        if oq == "SI" or oq == "SÍ":
            buscar_libros()
        else:
            libros()


# =======//===================//================//================//============//
def buscar_x_nombre():
    x = input("Ingrese el NOMBRE del libro: ").upper()
    nom_disp = False
    for i in range(len(libro_list)):
        if x == libro_list[i]:
            nom_disp = True
            print("\n=*=*=*= EL LIBRO ESTÁ DISPONIBLE =*=*=*=*=\n")
            print("NOMBRE DEL LIBRO: ", libro_list[i])
            print("CÓDIGO: ", cod_lib_list[i])
            print("AUTOR: ", autor_list[i])
            print("TOMO: ", tomo_list[i])
            print("OPINIÓN: ", opin_lib_list[i])
            oq = input("\n¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
            if oq == "SI" or oq == "SÍ":
                buscar_libros()
            else:
                libros()
    if not nom_disp:
        print("\n=*=*=*= EL LIBRO |NO| ESTÁ DISPONIBLE =*=*=*=*=\n")
        oq = input("¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
        if oq == "SI" or oq == "SÍ":
            buscar_libros()
        else:
            libros()


# =======//===================//================//================//============//
def buscar_x_autor():
    x = input("Ingrese el AUTOR del libro: ").upper()
    aut_disp = False
    for i in range(len(autor_list)):
        if x == autor_list[i]:
            cod_disp = True
            print("\n=*=*=*= EL LIBRO ESTÁ DISPONIBLE =*=*=*=*=\n")
            print("AUTOR: ", autor_list[i])
            print("CÓDIGO: ", cod_lib_list[i])
            print("NOMBRE DEL LIBRO: ", libro_list[i])
            print("TOMO: ", tomo_list[i])
            print("OPINIÓN: ", opin_lib_list[i])
            oq = input("\n¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
            if oq == "SI" or oq == "SÍ":
                buscar_libros()
            else:
                libros()
    if not cod_disp:
        print("\n=*=*=*= EL LIBRO |NO| ESTÁ DISPONIBLE =*=*=*=*=\n")
        oq = input("¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
        if oq == "SI" or oq == "SÍ":
            buscar_libros()
        else:
            libros()


# =======//===================//================//================//============//
def devolver_libro():
    n = int(input("¿cuántos libros va a DEVOLVER?: "))
    for i in range(n):
        opin_lib_list.append(
            str(input("¿Qué OPINIÓN le merece el libro? (BUENA / MALA): ")).upper()
        )
        cod_lib_list.append(input("Ingrese CÓDIGO del libro: ").upper())
        tomo_list.append(input("Ingrese el TOMO del libro(tres dígitos): "))
        libro_list.append(input("Ingrese el NOMBRE del libro: ").upper())
        autor_list.append(input("Ingrese el AUTOR del libro: ").upper())
    print("\n...........ACTUALIZANDO LISTA ...................")
    print("....................20%............................")
    print("....................50%............................")
    print("...................100%..........................\n")
    lista_libros()


# =======//===================//================//================//============//
def lista_libros():
    n = len(cod_lib_list)
    print("|OPINIÓN  |CÓDIGO |TOMO |    NOMBRE DEL LIBRO    |       AUTOR      |")
    for i in range(n):
        print(
            "|",
            opin_lib_list[i],
            " |",
            cod_lib_list[i],
            " |",
            tomo_list[i],
            "|",
            libro_list[i],
            "              ",
            autor_list[i],
        )
    op = input("¿Desea continuar en esta acción?\n(SI/NO) : ")
    if op == "si" or op == "SI" or op == "sí" or op == "SÍ":
        libros()
    else:
        inicio()


# =======//===================//================//================//============//
def retirar_libro():
    y = str(input("Ingrese código del libro que desea tomar por préstamo: ")).upper()
    ret_lib_ = False
    for i in range(len(cod_lib_list)):
        if y == cod_lib_list[i]:
            rtl = i
            ret_lib_ = True
            print("\n=*=*=*= EL LIBRO ESTÁ DISPONIBLE =*=*=*=*=\n")
            cod_lib_list.remove(cod_lib_list[rtl])
            tomo_list.remove(tomo_list[rtl])
            libro_list.remove(libro_list[rtl])
            autor_list.remove(autor_list[rtl])
            opin_lib_list.remove(opin_lib_list[rtl])
            print("¡Usted ha RETIRADO el libro con éxito!")
            print("\n..............ACTUALIZANDO LISTA ............")
            print("....................20%........................")
            print("....................50%........................")
            print("...................100%......................\n")
            lista_libros()
            break
    if not ret_lib_:
        print("\n=*=*=*= EL LIBRO |NO| ESTÁ DISPONIBLE =*=*=*=*=\n")
    oq = input("¿Desea realizar otra BÚSQUEDA? (SI / NO) ").upper()
    if oq == "SI" or oq == "SÍ":
        buscar_libros()
    else:
        inicio()


# =======//===================//================//================//============//
def usuarios():
    print("-------------------------------------------------")
    print("------------ MODULO DE USUARIOS  ----------------")
    print("------------  1. REGISTRARSE --------------------")
    print("------------  2. DAR DE BAJA --------------------")
    print("------------  3. LISTA ACTUALIZADA --------------")
    print("------------  4. SALIR       --------------------")
    print("-------------------------------------------------")
    op = int(input("\n Señale que ACCIÓN desea realizar: "))
    if op == 1:
        print("Usted ha elegido REGISTRAR un usuario")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
        reg_usuario()
    else:
        if op == 2:
            print("Usted ha elegido DAR DE BAJA a un usuario")
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            baja_usuario()
        else:
            if op == 3:
                print("Usted ha elegido LISTA ACTUALIZADA")
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                list_usuarios()
            else:
                if op == 4:
                    inicio()
                else:
                    print("¡Error!\nOpción Inválida")
                    op = int(input("Señale que ACCIÓN quiere realizar: "))


# =======//===================//================//================//============//
def reg_usuario():
    usu = int(input("\n¿Cuántos usuarios va a REGISTRAR?: \n"))
    for i in range(usu):
        dni = validacion_dni()
        if dni:
            dni_usu_list.append(dni)
            nom_usu_list.append(input("\nIngrese 1er NOMBRE: ").upper())
            apl_usu_list.append(input("\nIngrese 1er APELLIDO: ").upper())
            tel_usu_list.append(input("\nIngrese su número de TELÉFONO:"))
            print("\n..............ACTUALIZANDO LISTA ...................")
            print("....................20%...............................")
            print("....................50%...............................")
            print("...................100%.............................\n")
            list_usuarios()
        else:
            print("DNI Inválido")
            print("¡Desea continuar?: ")
            aa = int(input("1.= SI, Intentar de nuevo // 2.= NO, Salir ."))
            if aa == 1:
                reg_usuario()
            else:
                if aa == 2:
                    usuarios()
    print("¡Desea realizar otro REGISTRO?: ")
    aa = int(input("1.= SI // 2.= NO ."))
    if aa == 1:
        reg_usuario()
    else:
        if aa == 2:
            usuarios()


# ===================================================//=========================//
def validacion_dni():
    dni = input("Ingrese DNI del usuario : ")
    c = 0
    for i in range(len(dni)):
        if (
            dni[i] == "0"
            or dni[i] == "1"
            or dni[i] == "2"
            or dni[i] == "3"
            or dni[i] == "4"
            or dni[i] == "5"
            or dni[i] == "6"
            or dni[i] == "7"
            or dni[i] == "8"
            or dni[i] == "9"
        ):
            c += 1
        else:
            continue
    if c == 8:
        return dni

    else:
        return False


# ===================================================//=========================//
def list_usuarios():
    n = len(dni_usu_list)
    print("|DNI       |TELÉFONO  |NOMBRE DE USUARIO    ")
    for i in range(n):
        print(
            "|",
            dni_usu_list[i],
            "|",
            tel_usu_list[i],
            "|",
            nom_usu_list[i],
            " ",
            apl_usu_list[i],
        )
    op = input("¿Desea continuar en esta acción?\n(SI/NO) : ")
    if op == "si" or op == "SI" or op == "sí" or op == "SÍ":
        usuarios()
    else:
        inicio()


# ===================================================//=========================//
def baja_usuario():
    y = input("Ingrese DNI que desea DEPURAR: ")
    ret_usu_ = False
    for j in range(len(dni_usu_list)):
        if y == dni_usu_list[j]:
            rtu = j
            ret_usu_ = True
            print("\n=*=*=*= EL DNI esta DEPURÁNDOSE =*=*=*=*=\n")
            dni_usu_list.remove(dni_usu_list[rtu])
            nom_usu_list.remove(nom_usu_list[rtu])
            apl_usu_list.remove(apl_usu_list[rtu])
            tel_usu_list.remove(tel_usu_list[rtu])
            print("¡Usted ha DEPURADO el usuario con éxito!")
            print("\n..............ACTUALIZANDO LISTA ............")
            print("....................20%........................")
            print("....................50%........................")
            print("...................100%......................\n")
            list_usuarios()
            break
    if not ret_usu_:
        print("\n=*=*=*= EL DNI NO EXISTE =*=*=*=*=\n")
        oq = input("¿Desea realizar otra DEPURACIÓN? (SI / NO) ").upper()
        if oq == "SI" or oq == "SÍ":
            baja_usuario()
        else:
            usuarios()


# ===================================================//=========================//
def documentos():
    print("-------------------------------------------------")
    print("------------ DOCUMENTOS        ------------------")
    print("------------  1. SOLICITUD   ------------------")
    print("------------  2. CONSULTAR SOL ------------------")
    print("------------  3. CANCELAR SOL  ------------------")
    print("------------  4. SALIR         ------------------")
    print("-------------------------------------------------")
    print("\n Aquí usted podrá generar DOCUMENTOS de su interés.")
    oa = int(input("\nSeñale que ACCIÓN quiere realizar: "))
    if oa == 1:
        print("\nUsted ha elegido realizar una SOLICITUD")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
        doc_solicit()
    else:
        if oa == 2:
            print("\nUsted ha elegido CONSULTAR SOLICITUDES")
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
            lista_solicitudes()
        else:
            if oa == 4:
                print("\nUsted ha elegido CANCELAR SOLICITUDES")
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
                cancel_solic()
            else:
                if oa == 5:
                    inicio()
                else:
                    print("¡Error!\nOpción Inválida")
                    oa = int(input("Señale que acción quiere realizar: "))


# ===================================================//=========================//
def doc_solicit():
    print("Aqui podrá usted realizar la SOLICITUD de una búsqueda.\n")
    sol = int(input("¿Cuantas SOLICITUDES hará?: "))
    for i in range(sol):
        dni = validacion_dni()
        for j in range(len(dni_usu_list)):
            if dni == dni_usu_list[j]:
                ok = j
                ok == True
                print("|DNI       |TELÉFONO  |NOMBRE DE USUARIO    ")
                print(
                    "|",
                    dni_usu_list[ok],
                    "|",
                    tel_usu_list[ok],
                    "|",
                    nom_usu_list[ok],
                    " ",
                    apl_usu_list[ok],
                    "\n",
                )
                print(
                    "Se evaluará su solicitud, por favor ingrese los datos a continuacion"
                )
                print(
                    "con el fin de revisar en las bodegas antiguas si existe el libro."
                )
                num_doc_list.append(
                    input("Ingrese número de SOLICITUD(EJ: S###): ").upper()
                )
                libro_solic.append(input("Ingrese el NOMBRE del libro: ").upper())
                autor_solic.append(input("Ingrese el AUTOR del libro: ").upper())
                gen_solic.append(
                    input("Ingrese el GÉNERO literáreo al que pertenece: ").upper()
                )
                oq = input("¿Desea realizar otra SOLICITUD? (SI / NO) ").upper()
                if oq == "SI" or oq == "SÍ":
                    doc_solicit()
                else:
                    documentos()
        else:
            print("DNI Inválido")
            print("Debe registrar el DNI")
            aa = int(input("1.= SI, Registrar // 2. = NO, Intentar de nuevo."))
            if aa == 1:
                reg_usuario()
            else:
                if aa == 2:
                    doc_solicit()


# ===================================================//=========================//
def lista_solicitudes():
    n = len(num_doc_list)
    print("|NÚM SOLC |GENERO     |LIBRO            |AUTOR        ")
    for i in range(n):
        print(
            "|",
            num_doc_list[i],
            "|",
            gen_solic[i],
            "|",
            libro_solic[i],
            " ",
            autor_solic[i],
        )
    op = input("¿Desea continuar en esta acción?\n(SI/NO) : ")
    if op == "si" or op == "SI" or op == "sí" or op == "SÍ":
        documentos()
    else:
        inicio()


# ===================================================//=========================//
def cancel_solic():
    y = input("Ingrese solicitud a CANCELAR: ")
    ret_sol_ = False
    for j in range(len(num_doc_list)):
        if y == num_doc_list[j]:
            rts = j
            ret_sol_ = True
            print("\n=*=*=*= La solicitud está CANCELÁNDOSE =*=*=*=*=\n")
            num_doc_list.remove(num_doc_list[rts])
            gen_solic.remove(gen_solic[rts])
            libro_solic.remove(libro_solic[rts])
            autor_solic.remove(autor_solic[rts])
            print("¡Usted ha CANCELADO la solicitud con éxito!")
            print("\n..............ACTUALIZANDO LISTA ............")
            print("....................20%........................")
            print("....................50%........................")
            print("...................100%......................\n")
            lista_solicitudes()
            break
    if not ret_sol_:
        print("\n=*=*=*= LA SOLICITUD NO EXISTE =*=*=*=*=\n")
        oq = input("¿Desea realizar otra CANCELACIÓN? (SI / NO) ").upper()
        if oq == "SI" or oq == "SÍ":
            cancel_solic()
        else:
            documentos()


inicio()
