from django import forms
from .models import Order
from robot.models import Robot

class OrderForm(forms.ModelForm):
    robot = forms.ModelChoiceField(queryset=Robot.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ["robot", "name", "phone"]