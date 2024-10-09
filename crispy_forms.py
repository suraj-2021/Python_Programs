from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SampleForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    message = forms.CharField(widget=forms.Textarea, label='message')

    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
