from django import forms
from django.forms.models import inlineformset_factory
from .models import Store, MenuItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


BaseMenuItemFormSet = inlineformset_factory(
    parent_model=Store, model=MenuItem, fields=('name', 'price',), extra=1,
)

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('name', 'notes',)
    
    def __init__(self, *args, submit_title='Submit', **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        if submit_title:
            self.helper.add_input(Submit('submit', submit_title))

class MenuItemFormSet(BaseMenuItemFormSet):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False     #不需要，我們自己包
        self.helper.disable_csrf = True  #Storeform 已經有CSRF token，不需要重複產生。

