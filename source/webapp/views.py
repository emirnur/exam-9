from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    model = Photo
    template_name = 'index.html'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'detail.html'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'create.html'
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = Photo.objects.create(author=self.request.user, photo=form.cleaned_data['photo'],
                                           sign=form.cleaned_data['sign'])

        return HttpResponseRedirect(self.get_success_url())


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.photo_author(self.request.user)

    def photo_author(self, user):
        return self.get_object().author == user


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'photo'
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        return super().has_permission() or self.photo_author(self.request.user)

    def photo_author(self, user):
        return self.get_object().author == user

