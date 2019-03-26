from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import forms
# Create your views here.


def index(request):
    return render(request, 'loginSignup/index.html')


# def Signup_view(request):
#     if request.method == 'POST':
#         form = forms.Signup_form(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             return HttpResponse('great weve signed you up!')
#         else:
#             return HttpResponse('form is invalid')
#     else:
#         form = forms.Signup_form()

#     return render(request, 'loginSignup/registration.html', {'form':form})
     

def Signup_view(request):
    registered = False
    if request.method == 'POST':
        form = forms.Signup_form(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(form.errors)
    else:
        form = forms.Signup_form()
    return render(request, 'loginSignup/registration.html',
                  {'form': form,
                           'registered': registered})
