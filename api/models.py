from django.db import models

#class Acceso(models.Model):
#    nombreAula = models.CharField(max_length=200)
#    nombreProfesor = models.CharField(max_length=200)
#    password = models.CharField(max_length=20)
#    pub_date = models.DateTimeField('fecha de registro',auto_now=True)
STATUS_CHOICES = (
        ('a', 'a'),
        ('b', 'b'),
        
    )

class Zona(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TipoAula(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Aula(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='a')
    zona = models.ForeignKey(Zona,on_delete=models.CASCADE)
    tipo_aula = models.ForeignKey(TipoAula,on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateTimeField('fecha...', null=True , blank=True)
    def __str__(self):
        return self.nombre
    
class DetalleAcceso(models.Model):
    fecha_nacimiento = models.DateTimeField('fecha..DA.', auto_now=True , blank=True)
    aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    timestamps = models.DateTimeField('fecha...', null=True , blank=True)


class Acceso(models.Model):
    tipo_acceso = models.CharField(max_length=50 , null=True)
    fecha = models.DateTimeField('fecha...', null=True , blank=True)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.persona.nombre
#====
class Rol(models.Model):
    rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Configuracion(models.Model):
    fecha_inicio = models.DateTimeField('fechaInicio', null=True , blank=True)
    fecha_fin = models.DateTimeField('fechaFin', null=True , blank=True)
    dias_laborales = models.IntegerField()
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    

    



    



