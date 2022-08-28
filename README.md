# Entrega de repositorio Sprint 8

* OBTENER DATOS DE UN CLIENTE

Un cliente autenticado puede consultar sus propios datos.

      http://127.0.0.1:8000/api/datoscliente/ Numero de DNI
      
* OBTENER SALDO DE CUENTA DE UN CLIENTE

Un cliente autenticado puede obtener el tipo de cuenta y su saldo.

      http://127.0.0.1:8000/api/saldocuenta/ Numero de DNI

* OBTENER MONTO DE PRESTAMOS DE UN CLIENTE

Un cliente autenticado puede obtener el tipo de préstamo y total del mismo.
  
      http://127.0.0.1:8000/api/totalprestamocliente/ Numero de DNI
 
* OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL

 Un empleado autenticado puede obtener el listado de préstamos otorgados deuna sucursal determinada.
 
      http://127.0.0.1:8000/api/totalprestamosucursal/ Numero de DNI
 
* OBTENER TARJETAS ASOCIADAS A UN CLIENTE

 Un empleado autenticado puede obtener el listado de tarjetas de crédito de uncliente determinado.
 
      http://127.0.0.1:8000/api/datostarjetacliente/ Numero de DNI

* GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE

Un empleado autenticado puede solicitar un préstamo para un cliente, registradoel mismo y acreditando el saldo en su cuenta.

      http://127.0.0.1:8000/api/solicitudprestamo
      Json:  {"monto":2000 ,"fecha_inicio": "", "tipo":"A","cliente_id":"39549327"}
    
* ANULAR SOLICITUD DE PRESTAMO DE CLIENTE

Un empleado autenticado puede anular un préstamo para un cliente, revirtiendoel monto correspondiente.

      http://127.0.0.1:8000/api/eliminarprestamo/  ID de prestamo
 
* MODIFICAR DIRECCION DE UN CLIENTE

El propio cliente autenticado o un empleado puede modificar las direcciones.
      
      http://127.0.0.1:8000/api/modificardireccion/  Numero de DNI
      Json:  {"calle":"AV. Cordoba","altura":41}
      
* LISTADO DE TODAS LAS SUCURSALES

Un endpoint público que devuelve el listado todas las sucursales con lainformación correspondiente.

      http://127.0.0.1:8000/datostarjetacliente/ Numero de DNI

