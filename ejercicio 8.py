rol = input("Ingrese su rol (admin/usuario): ").strip().lower()
if rol == "admin":
        print("Acceso permitido")
else:
        print("Acceso denegado")