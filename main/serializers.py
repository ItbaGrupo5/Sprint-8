from rest_framework import serializers

from .models import Sucursales
from .models import Movimientos
from .models import Prestamos
from .models import Clientes
from .models import Cuentas
from .models import Direcciones
from .models import Tarjetas


class ClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Clientes
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class CuentasSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cuentas
        #indicamos que use todos los campos
        fields = ['tipo', 'saldo']
        #les decimos cuales son los de solo lectura 



class SucursalesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Sucursales
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 



class MovimientosSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movimientos
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class DireccionesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Direcciones
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura         




class PrestamosSerializer(serializers.ModelSerializer):
     class Meta:
        model = Prestamos
        fields = "__all__"
        
class PrestamoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Prestamos
        fields = ['monto', 'tipo']


class TarjetasSerializer(serializers.ModelSerializer):
     class Meta:
        model = Tarjetas
        fields = "__all__"