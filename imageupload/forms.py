from django import forms  
from .models import  *
class HotelForm(forms.ModelForm):  
    class Meta:  
        model = Hotel
        fields = "__all__"  

class HotelForm1(forms.ModelForm):  
    class Meta:  
        model = Hotel1
        fields = "__all__"  

class HotelForm2(forms.ModelForm):  
    class Meta:  
        model = Hotel2
        fields = "__all__"  

class HotelForm3(forms.ModelForm):  
    class Meta:  
        model = Hotel3
        fields = "__all__"  

class HotelForm4(forms.ModelForm):  
    class Meta:  
        model = Hotel4
        fields = "__all__"  