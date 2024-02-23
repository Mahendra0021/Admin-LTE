from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
             'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput( render_value=True,attrs={'class':'form-control','id':'passwordid'}),
     
        }
        