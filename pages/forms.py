from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Response



#These forms take in responce objects to Question from the user.
class ResponseForm(forms.ModelForm):        

    # Crispy forms initializer
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = 'submit'
        self.fields['Stregthen_social_safety_nets'].widget.attrs = {'rows': 2}
        self.fields['Nationalize_healthcare'].widget.attrs = {'rows': 2}
        self.fields['Climate_responce'].widget.attrs = {'rows': 2}
        self.fields['Should_we_limit_urban_sprall'].widget.attrs = {'rows': 2}
        self.fields['Do_you_support_or_oppose_globalization'].widget.attrs = {'rows': 2}
        self.helper.add_input(Submit('submit', 'Submit'))
        
    #Basic model Form meta tag. We use feilds to manage the order of what in displayed.
    class Meta:
        model = Response
        fields = [
        'Stregthen_social_safety_nets',
        'Nationalize_healthcare',
        'Climate_responce',
        'Should_we_limit_urban_sprall',
        'Do_you_support_or_oppose_globalization']

        #fields = '__all__' #Use all model fields