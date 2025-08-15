from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=30, label="Código", help_text="Ingrese el codigo del programa.")
    nombre = forms.CharField(max_length=200, label="Nombre", help_text="Ingrese el nombre del programa.")
    nivel_formacion = forms.ChoiceField(choices=Programa.Nivel_FORMACION_CHOICES, label="Nivel de Formación", help_text="Seleccione el nivel de formacion del programa.")
    modalidad = forms.ChoiceField(choices=Programa.Modalidad_CHOICES, label="Modalidad", help_text="Seleccione la modalidad del programa.")
    duracion_meses = forms.IntegerField(min_value=0, label="Duración en Meses", help_text="Ingrese la duracion en meses del programa.")
    duracion_horas = forms.IntegerField(min_value=0, label="Duración en Horas", help_text="Ingrese la duracion en horas del programa.")
    centro_formacion = forms.CharField(max_length=200, label="Centro de formación", help_text="Ingrese el centro de formacion.")
    regional = forms.CharField(max_length=100, label="Regional")
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, label="Estado", help_text="Seleccione el estado del programa.")
    fecha_creacion = forms.DateField(label="Fecha de Creación", help_text="Ingrese la fecha de creacion del programa.")
    fecha_registro = forms.DateField(label="Fecha de Registro", help_text="Ingrese la fecha de registro del programa.")
    
    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')
        nivel_formacion = cleaned_data.get('nivel_formacion')
        
        if not codigo or not nombre or not nivel_formacion:
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isdigit():
            raise forms.ValidationError("El codigo solo debe contener números.")
        return codigo
    
    def save(self):
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data.get('nivel_formacion'),
                modalidad=self.cleaned_data.get('modalidad'),
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data.get('estado'),
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data['fecha_registro']
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al creae el programa: {str(e)}")