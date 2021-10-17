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
        self.helper.add_input(Submit('submit', 'Submit'))
        
    #Basic model Form meta tag. We use feilds to manage the order of what in displayed.
    class Meta:
        model = Response
        fields = [
        'Question1',
        'Question2',
        'Question3',
        'Question4',
        'Question5'
        ]

        #fields = '__all__' #Use all model fields