import hashlib
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render_to_response
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.template import RequestContext

from .forms import SignupForm, SigninForm, ForgotPasswordForm

class HomePageView(View):

    def get(self, request, *args, **kwargs):
        context = RequestContext(request)
        u = User.objects.get(username=request.user)
        greet_user = u
        try:
            up = UserProfile.objects.get(user=u)
        except:
            up = None
        
        context['user'] = u
        context['userprofile'] = up

        # Displays user and Greet
        #Automatic display to HTML using message framework
        messages.add_message(request, messages.INFO, ("Hello %s" % greet_user))
        
        return render_to_response("base.html", 
                               locals(), 
                               context_instance=context)

# class SignupView(CreateView):
#     model = User
#     form_class = SignupForm
#     template_name = "signup.html"
#     success_url = reverse_lazy('signin')
#     success_message = "Account is created. Now you can sign in."

#     def form_valid(self, form):
#         if user is not None:
#             login(request, user)
#             return redirect(reverse_lazy('home'))
#         else:
#             messages.error(request, self.error_message)

#         messages.success(self.request, self.success_message)
#         return super(SignupView, self).form_valid(form)

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy('signin')
    success_message = "Account is created. Now you can sign in."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(SignupView, self).form_valid(form)

class SigninView(FormView):
    template_name = "signin.html"
    form_class = SigninForm
    success_url = reverse_lazy('home')
    error_message = "Wrong username or password"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = authenticate(
                # email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))
            else:
                messages.error(request, self.error_message)

            return self.render_to_response(
                self.get_context_data(form=form)
            )
        else:
            return self.form_invalid(form, **kwargs)


class ForgotPasswordView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('signin')
    success_message = 'New password is sent in your email inbox'

    def form_valid(self, form):
        m = hashlib.md5()
        data_encoded = datetime.today()
        data_encoded = str(data_encoded)
        m.update(
            "{email}{secret}{date}".format(
                email=form.cleaned_data['email'],
                secret=settings.SECRET_KEY,
                date=(data_encoded)
            )
        )
        new_password = m.hexdigest()[:8]

        user = User.objects.get(email=form.cleaned_data['email'])
        user.set_password(new_password)
        user.save()

        send_mail(
            'Notejam password reset',
            'Hi, {}. Your new password is {}.'.format(
                 form.cleaned_data['email'],
                 new_password
            ),
            'from@notejamapp.com',
            [form.cleaned_data['email']],
            fail_silently=False
        )
        messages.success(self.request, self.success_message)

        return super(ForgotPasswordView, self).form_valid(form)


class AccountSettingsView(FormView):
    form_class = PasswordChangeForm
    template_name = 'settings.html'
    success_url = reverse_lazy('home')
    success_message = 'Password is successfully changed'

    # def get_user(request):
    #     context = RequestContext(request)
    #     u = User.objects.get(username=request.user)
        
    #     context['user'] = u
    #     return context)

    def get_form_kwargs(self):
        kwargs = super(AccountSettingsView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(AccountSettingsView, self).form_valid(form)
