

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        subTotal = self.session.get("subTotal")
        ultimaOperacion = self.session.get("ultimaOperacion")

        # 0. No se ha realizado operación 
        # 1. Se ha agregado un producto
        # 2. Se ha eliminado un producto
        # 3. Se ha limpiando el carrito
        # 4. Se ha decrementado la cantidad de unidades
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
            self.session["ultimaOperacion"] = 0
            self.ultimaOperacion = self.session["ultimaOperacion"]
            self.session["subTotal"] = 0
            self.subTotal = self.session["subTotal"]
        else:
            self.carrito = carrito
            self.ultimaOperacion = ultimaOperacion
            self.subTotal = subTotal


            
    
    def agregar(self, producto):
        id = str(producto.pk)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.pk,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "precio": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio

        self.ultimaOperacion = 1;
        self.guardar_carrito()


    def guardar_carrito(self):
        self.actualizarSubTotal()
        self.session["carrito"] = self.carrito
        self.session["ultimaOperacion"] = self.ultimaOperacion
        self.session["subTotal"] = self.subTotal
        self.session.modified = True

    def limpiar(self):
        self.ultimaOperacion = 3
        self.carrito = {}
        self.guardar_carrito()

    def actualizarSubTotal(self):
        total = 0   
        for key,value in self.carrito.items():
            total += int(value["acumulado"])
        self.subTotal = total
    
    def eliminar(self, producto):
        id = str(producto.pk)
        if id in self.carrito:
            del self.carrito[id]
            self.ultimaOperacion = 2
            self.guardar_carrito()
    
    def eliminarUnidad(self, producto):
        id = str(producto.pk)
        if id in self.carrito:
            self.carrito[id]["cantidad"] -= 1
            self.ultimaOperacion = 4
            self.guardar_carrito()
        

    def actualizarCantidad(self, id, cant):
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] = cant
            self.carrito[id]['acumulado'] = cant * self.carrito[id]['precio']
            self.guardar_carrito()
        
    def inicializarCarrito(self, producto, cant):
        self.limpiar()
        self.carrito[producto.pk] = {
                "producto_id" : producto.pk,
                "nombre": producto.nombre,
                "acumulado": producto.precio * cant,
                "precio": producto.precio,
                "cantidad": cant
        }
        self.guardar_carrito()