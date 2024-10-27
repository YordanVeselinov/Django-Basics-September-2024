from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from MyMusicApp.albums.models import Album
from MyMusicApp.profiles.forms import ProfileCreateForm
from MyMusicApp.utils import get_user_obj


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj()  # None or QuerySet

        if profile:
            return ['profile/home-with-profile.html']

        return ['profile/home-no-profile.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Call the base method to get existing context
        context['albums'] = self.get_queryset()  # Add albums to context
        context['form'] = self.get_form()  # Include the profile creation form
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
