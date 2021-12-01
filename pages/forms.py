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
        self.fields['Question1'].label = "Is there such a thing as fate? Do we have free will to make our own choices?"
        self.fields['Question2'].label = "Is life completely random or does life have meaning?"
        self.fields['Question3'].label = "What should the goal of humanity be?"
        self.fields['Question4'].label = "What does every human in the world deserve; even those who have committed heinous crimes?"
        self.fields['Question5'].label = "Who build the pryamids?"

        
    #Basic Model Form Meta subclass. We use the felids parameter to manage the order of what is displayed.
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