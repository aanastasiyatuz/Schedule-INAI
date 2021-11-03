from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegistrationForm

User = get_user_model()


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('books')
    success_message = 'Successfully registered'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration_form'] = self.get_form(self.get_form_class())
        return context

class SignInView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('books')
    success_message = 'Successfully login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.get_form(self.get_form_class())
        return context
