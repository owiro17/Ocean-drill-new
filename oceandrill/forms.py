from django import forms
from django.core.validators import RegexValidator
from django.contrib import messages
phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'input'}),min_length=3)
    second_name = forms.CharField(label="Second Name", widget=forms.TextInput(attrs={'class':'input'}),min_length=3)
    email = forms.CharField(label="email " ,widget=forms.EmailInput(attrs={'class':'input',}))
    phone = forms.CharField(label="Phone number " ,widget=forms.TextInput(attrs={'class':'input','placeholder':'0712345678'}),max_length=13,min_length=10,validators=[phone_validator])
    message = forms.CharField(label='Your Message', widget=forms.Textarea(attrs={'class':'input', 'id':'message-box' , 'name':'message'}), required=False)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Please enter your first name')
        return first_name

    def clean_second_name(self):
        second_name = self.cleaned_data.get('second_name')
        if not second_name:
            raise forms.ValidationError('Please enter your secon name')
        return second_name
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Please enter your email')
        return email
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('Please enter a valid phone number')
        return phone
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError('Please enter your message')
        return message