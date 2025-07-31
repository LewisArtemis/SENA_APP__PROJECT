from django.db import models

# Create your models here.

class Programa(models.Model):
    Nivel_FORMACION_CHOICES = [
        ('AUX', 'Auxiliar'),
        ('OPE', 'Operario'),
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('ESP', 'Especialización'),
        ('COM', 'Complementario'),
    ]
    
    Modalidad_CHOICES = [
        ('PRE', 'Presencial'),
        ('VIR', 'Virtual'),
        ('MIX', 'Mixta'),
    ]
    
    ESTADO_CHOICES =[
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
        ('SUS', 'Suspendido'),
        ('CAN', 'Cancelado'),
    ]
    
    codigo = models.CharField(max_length=30, unique=True, verbose_name="Codigo del Programa")
    nombre = models.CharField(max_length=200, verbose_name= "Nombre del Programa")
    nivel_formacion = models.CharField(max_length= 6, choices=Nivel_FORMACION_CHOICES, verbose_name="Nivel de Formacion")
    modalidad = models.CharField(max_length=6, choices=Modalidad_CHOICES, default='PRE', verbose_name="Modalidad")
    duracion_meses = models.PositiveIntegerField(verbose_name="Duración en Meses")
    duracion_horas = models.PositiveIntegerField(verbose_name="Duración en Horas")
    centro_formacion = models.CharField(max_length=200, verbose_name="Centro de Formación")
    regional = models.CharField(max_length=100, verbose_name="Regional")
    estado = models.CharField(max_length=3,choices=ESTADO_CHOICES, default='ACT', verbose_name="Estado")
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación del Programa")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Programa de Formacion"
        verbose_name_plural = "Programas de Formacion"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def get_duracion_completa(self):
        return f"{self.duracion_meses} meses({self.duracion_horas} horas)"
    
    def is_activo(self):
        return self.estado == 'ACT'
    