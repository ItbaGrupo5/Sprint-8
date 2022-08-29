#Sprint 8 - Primera aplicacion
#Vamos a importar un método del módulo django.http llamado HttpResponse
from django.shortcuts import render, HttpResponse
from .forms import PrestamoForm
from .forms import RegistroForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import esEmpleado
from .models import Direcciones, Movimientos, Tarjetas
from .models import Clientes
from .models import Cuentas
from .models import Prestamos
from .models import Empleados
from .models import ids
from datetime import date
from .serializers import DireccionesSerializer, SucursalesSerializer 
from .serializers import ClienteSerializer
from .models import Sucursales
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from .serializers import MovimientosSerializer 
from .serializers import PrestamoSerializer 
from .serializers import PrestamosSerializer 
from .serializers import CuentasSerializer 
from .serializers import TarjetasSerializer

def home(request):
    if request.user.username:
        #cliente= Clientes.objects.get(cliente_id=int(request.user.username))
        cliente=request.user.username

        return render(request,"main/home.html", {'cliente' : cliente})
    else:    
        return render(request,"main/home.html")


@login_required
def cuentas(request):

    row_cliente_id= ids.objects.filter(username=request.user.username)[0]
    
    movimientos= Movimientos.objects.filter(cliente_id=row_cliente_id.cliente_id).order_by('-id')

    return render(request,"main/cuentas.html", {'movimientos': movimientos})




#Agregamos la vista de contacto que teniamos en la aplicacion de prueba
@login_required
def prestamos(request):
    #creamos una isntancia del formulario
    prestamo_form = PrestamoForm
    #validamos que ocurrio una peticiPreson POST
    if request.method == "POST":
        #Traemos los datos enviados
        prestamo_form = prestamo_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if prestamo_form.is_valid():
            monto = request.POST.get('monto','')
            tipo = request.POST.get('tipo','')

            try:
                row_cliente_id= ids.objects.filter(username=request.user.username)[0]
                cliente_id =row_cliente_id.cliente_id
                #Generamos el prestamo
                #hay que poner un if consultando si ya se excedio el limite
                #manando un denied q mostrara un mensaje en el template
                prestamo = Prestamos(cliente_id=cliente_id,monto=monto, tipo=tipo, fecha_inicio=date.today())
                movimiento = Movimientos(cliente_id=cliente_id,importe=monto,fecha=date.today())
                movimiento.save()
                prestamo.save()
                return redirect(reverse('prestamos')+"?ok")
            except:
                return redirect(reverse('home'))
        #En lugar de renderizar el template de prestamoo hacemos un redireccionamiento enviando una variable OK
        
    return render(request,"main/prestamos.html",{'form': prestamo_form})


def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        #Traemos los datos enviados
        registro_form = registro_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        #if registro_form.is_valid():
        cliente_id= request.POST.get('cliente_id','')
        usuario= request.POST.get('username','')
        email = request.POST.get('email','')
        pwd = request.POST.get('pwd','')
        print(cliente_id,email,pwd)
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        try:
            persona= Clientes.objects.filter(cliente_id=cliente_id)[0]
            tipo='cliente'
        except:
            persona= Empleados.objects.filter(cliente_id=cliente_id)[0]
            tipo='empleado'

        dni = ids(cliente_id=cliente_id,username=usuario,tipo=tipo)
        dni.save()
        user = User.objects.create_user(usuario, email, pwd)
        user.save()
        print('creado')
        #En lugar de renderizar el template de prestamoo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('login'))
    return render(request,"main/registro.html",{'form': registro_form})



#----------------Punto uno--------------------
class DatosCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cliente_id):
        #clientes = Clientes.objects.all()
        
        username = request.user
        owner=cliente_id
        try:
            user=ids.objects.filter(username=username).first()
            dni=user.cliente_id
        except:
            dni = -1
        if (dni == owner or user.tipo == 'empleado' ):
            datos = Clientes.objects.filter(cliente_id=cliente_id)
            serializer = ClienteSerializer(datos[0])

        
            if datos:

                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('no coincide el dni ni es empleado',status=status.HTTP_404_NOT_FOUND)
