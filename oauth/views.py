from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import CustomerForm


def index(request):
    return render(request, 'oauth/index.html')


class CustomerFormView(View):
    form_class = CustomerForm
    template_name = 'oauth/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'error_message': False})

    def post(self, request):
        form = self.form_class(request.POST)

        def pass_match():
            password = form.cleaned_data['password']
            password2 = request.POST['verifypass']
            if password == password2:
                return True
            else:
                return False

        if form.is_valid() and pass_match():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('oauth:index')

        elif not pass_match():
            return render(request, self.template_name, {'form': form,  'error_message': True})

        return render(request, self.template_name, {'form': form})
