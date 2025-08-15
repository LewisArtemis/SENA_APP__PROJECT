from django import forms
from .models import Instructor

class InstructorForm(forms.Form):
    documento_identidad = forms.CharField(max_length=20, label="Documento de Identidad", help_text="Ingrese el numero de documento de identidad del instructor.")
    Tipo_documento = forms.ChoiceField(choices=Instructor.Tipo_documento_choice, label="Tipo de Documento", help_text="Seleccione el tipo de documento del instructor.")
    nombre = forms.CharField(max_length=100, label="Nombre", help_text="Ingrese el nombre del instructor.")
    apellido = forms.CharField(max_length=100, label="Apellido", help_text="Ingrese el apellido del instructor.")
    correo = forms.EmailField(required=False, label="Correo Electónico", help_text="Ingrese el correo electrónico del instructor.")
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", help_text="Ingrese la fecha de nacimiento del instructor.")
    anios_experiencia = forms.IntegerField(min_value=0, label="Años de Experiencia", help_text="Ingrese los años de experiencia del instructor.")
    ciudad = forms.CharField(max_length=100, required=False, label="Ciudad", help_text="Ingrese la ciudad de residencia del instrcutor.")
    programa = forms.CharField(max_length=100, required=False, label="Programa", help_text="Ingrese el programa.")
    Nivel_educativo = forms.ChoiceField(choices=Instructor.Nivel_educativo_choice, label="Nivel Educativo", help_text="Seleccione el nivel educativo del instructor.")
    ficha = forms.CharField(max_length=30, label="Ficha", help_text="Ingrese la ficha.")
    activo = forms.BooleanField(required=False, initial=True, label="Activo", help_text="Indique si el instructor está activo.")
    
    
    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        
        if not documento or not nombre or not apellido:
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data
    
    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento
    
    def save(self):
        #Metodo para guardar el instructor en la base de datos
        try:
            instructor = Instructor.objects.create(
                documento_identidad=self.cleaned_data['documento_identidad'],
                Tipo_documento=self.cleaned_data['Tipo_documento_choice'],
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                correo=self.cleaned_data.get('correo', ''),
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                anios_experiencia=self.cleaned_data['anios_experiencia'],
                ciudad=self.cleaned_data.get('ciudad', ''),
                programa=self.cleaned_data.get('programa', ''),
                Nivel_educativo=self.cleaned_data['Nivel_educativo_choice'],
                ficha=self.cleaned_data['ficha'],
                activo=self.cleaned_data.get('activo', True),
            )
            return instructor
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el instructor: {str(e)}")