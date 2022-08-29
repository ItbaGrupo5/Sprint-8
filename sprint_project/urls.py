
from django.contrib import admin
from main import views as main_views
from django.conf  import settings
from django.urls import path,include


urlpatterns = [
    #Creamos un patrón url, en la raíz del sitio (cadena vacía) desde el que llamaremos a la vista views.home que tiene el nombre home.
    path('',main_views.home, name="home"), 
    path('prestamos/',main_views.prestamos, name="prestamos"), 
    path('cuentas/',main_views.cuentas, name="cuentas"), 
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/registro',main_views.registro, name="registro"),
    path('api/sucursales/', main_views.SucursalesLists.as_view(),name='api_sucursales' ) ,
    path('api/movimientos/', main_views.MovimientosLists.as_view(),name='api_movimientos' ),
    path('api/movimientos/<int:movimiento_id>/',main_views.MovimientosDetails.as_view()),
    path('api/prestamos/<int:cliente_id>/', main_views.PrestamosListCliente.as_view(),name='api_prestamos_list' ),
    path('api/datoscliente/<int:cliente_id>', main_views.DatosCliente.as_view(),name='api_datos_cliente' ),
    path('api/saldocuenta/<int:cliente_id>', main_views.SaldoCuenta.as_view(),name='api_saldo_cuenta' ),
    path('api/totalprestamocliente/<int:cliente_id>', main_views.TotalPrestamos.as_view(),name='api_total_prestamo_cliente' ),
    path('api/totalprestamosucursal/<int:sucursal_id>', main_views.TotalPrestamosSucursal.as_view(),name='sucursal' ),
    path('api/solicitudprestamo', main_views.SolicitudPrestamo.as_view(),name='solicitud_prestamo' ),
    path('api/eliminarprestamo/<int:prestamo_id>', main_views.EliminarPrestamo.as_view(),name='eliminar_prestamo' ),
    path('api/modificardireccion/<int:cliente_id>',main_views.ModificarDireccionCliente.as_view()),
    path('api/datostarjetacliente/<int:cliente_id>', main_views.DatosTarjetaCliente.as_view(),name='api_datos_tarjetas_cliente' )

    
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    