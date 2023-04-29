from django.shortcuts import render, redirect
from django.views import View
from .models.user import User
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username_tobe_check = request.POST.get('username')
        password_tobe_check = request.POST.get('password')

        try:
            username_actual = User.objects.get(username=username_tobe_check)
            try:
                if username_actual:
                    flag = check_password(password_tobe_check, username_actual.password)

                    if flag:
                        request.session['username'] = username_actual.username
                        return redirect('indexpage')
                    else:
                        return render(request, 'login.html')
            except:
                return render(request, 'login.html')
        except:
            return render(request, 'login.html')



class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('indexpage')


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        error_message = None
        # try:
        username = request.POST.get('usernameS')
        password = request.POST.get('passwordS')

        try:
            try:
                username_db = User.objects.get(username=username)
                error_message = "email already exists"
                print(error_message)
                data = {
                    'error_message': error_message
                }
                return render(request, 'signup.html', data)
            except:
                if len(password) < 7:
                    error_message = "password too short"
                    data = {
                        'error_message': error_message
                    }
                    return render(request, 'signup.html', data)
                else:
                    user = User(username=username, password=password)
                    print("username:-" + username)
                    user.password = make_password(password)
                    user.save()
                    return redirect('indexpage')
        except:
            return render(request, 'signup.html')


class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self,request):
        return render(request, 'index.html')


class outdoor(View):
    def get(self,request):
        return render(request,'outdoor.html')
    

class Indoor(View):
    def get(self,request):
        return render(request,'indoor.html')
    
class timing(View):
    def get(self,request):
        return render(request,'timing.html')

class timing_all(View):
    def get(self,request):
        return render(request,'timing_all.html')

class register(View):
    def get(self,request):
        return render(request,'register.html')


class Success(View):
    def get(self,request):
        return render(request,'success.html')

    def post(self,request):
        return render(request,'success.html')

class Devices(View):
    def get(self,request):
        return render(request,'trackyourDevices.html')
    

class PayNow(View):
    def get(self,request):
        return render(request,'payment.html')


class Success_Custom(View):
    def get(self, request):
        return render(request, 'success_custom.html')

    def post(self,request):
        slot = request.POST.get('sport')
        print(slot)
        data = {
            'slots': slot,
        }
        return render(request,'success_custom.html',data)


    
