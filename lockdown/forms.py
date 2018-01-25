from django import forms

class NameForm(forms.Form):
    host_name = forms.CharField(label='host_name', max_length=100)
    admin_username = forms.CharField(label='admin_username', max_length=100)
    #admin_password = forms.CharField(label='admin_password', max_length=100,widget=forms.PasswordInput())
    admin_password = forms.CharField(label='admin_password', max_length=100)
    command = forms.CharField(label='command', max_length=100)
