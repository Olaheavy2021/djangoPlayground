from django.shortcuts import render, redirect

from users.forms import UserRegisterForm

from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            first_name = form.cleaned_data.get('first_name')

            messages.success(request, f'Hello {first_name}, Your account has been created! Now you can login!')

            return redirect('login')
    else:

        form = UserRegisterForm()

        return render(request, 'users/register.html', {'form': form, 'title': 'Student Registration'})
