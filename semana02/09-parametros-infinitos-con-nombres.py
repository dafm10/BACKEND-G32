# En Python también se pueden pasar N parámetros con el nombre del parámetro usando los **kwargs (keyword arguments)
def crear_perfil(id, **datos):
    # Se necesita enviar un correo de bienvenida si a la función se le pasa el parámetro correo ó email
    print(id)
    print(datos)

crear_perfil(id="1", nombre="Eduardo", edad=30)
crear_perfil(id="2", nombre="Valeria", nacionalidad="Peruana", estado_civil="Viuda")