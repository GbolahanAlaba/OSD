from django import forms
from .models import *

class INVForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(INVForm, self).__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Inventory
        # fields = '__all__'

        fields = ['Product', 'Type', 'Category', 'Quantity', 'Vendor', 'Date', 'Comments']
        required = ('Product', 'Type', 'Category', 'Quantity', 'Vendor', 'Date')

    
        # self.fields['Type'].required = True
        # self.fields['Category'].required = True
        # self.fields['Quantity'].required = True
        # self.fields['Vendor'].required = True
        # self.fields['Date'].required = True



    