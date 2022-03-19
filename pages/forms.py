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
        self.fields['Question1'].label = "What is your favorite season?"

        
    #Basic Model Form Meta subclass. We use the felids parameter to manage the order of what is displayed.
    class Meta:
        model = Response
        fields = [
            'Question1',
        ]

        #fields = '__all__' #Use all model fields