from django.db import models

# Create your models here.
class Instructor(models.Model):
    
    Tipo_documento_choice = (
        ('C.C', 'Cedula de Ciudadania'),
        ('C.E', 'Cedula de Extranjeria'),
        ('T.I', 'Tarjeta de Identidad'),
        ('PAS', 'Pasaporte'),
    )
    
    Nivel_educativo_choice = (
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especialización'),
        ('MAE', 'Maestría'),
        ('DOC', 'Doctorado'),
    )
    
    documento_identidad = models.CharField(max_length=30)
    Tipo_documento_choice = models.CharField(max_length=30, choices=Tipo_documento_choice, default='C.C')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    anios_experiencia = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=30)
    programa = models.CharField(max_length=30)
    Nivel_educativo_choice = models.CharField(max_length=30, choices=Nivel_educativo_choice, default='MAE')
    ficha = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.documento_identidad} {self.activo}"