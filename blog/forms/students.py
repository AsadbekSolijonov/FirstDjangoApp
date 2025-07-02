from django import forms

from blog.models.students import Student


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'image', 'phone', 'total_points', 'birthday', 'payed']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
