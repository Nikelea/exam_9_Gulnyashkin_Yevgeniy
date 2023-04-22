from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from publications.models import Publication
from publications.forms import PublicationForm, CommentForm


def like_publication(request, pk):
    publication = get_object_or_404(Publication, id=request.POST.get('publication_id'))
    if request.user in publication.likes.all():
        publication.likes.remove(request.user)
        publication.likes_counter = publication.likes.count()
    else:
        publication.likes.add(request.user)
        publication.likes_counter = publication.likes.count()
    publication.save()
    return HttpResponseRedirect(reverse('publications:detail', args=[str(pk)]))


class IndexView(ListView):
    context_object_name = 'publications'
    model = Publication
    ordering = ('-created_at')
    template_name = 'publication/publication_list.html'


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        user = get_object_or_404(get_user_model(), pk=self.request.user.pk)
        publication = form.save(commit=False)
        publication.user = user
        publication.save()
        return redirect('publications:index')



class PublicationView(DetailView):
    template_name = 'publication/publication.html'
    model = Publication
    pk_url_kwarg = 'publication_pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CommentForm
        return context


class PublicationDelete(PermissionRequiredMixin, DeleteView):
    model = Publication

    def has_permission(self):
        return self.get_object().user == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse('publications:index')
    
class PublicationEdit(PermissionRequiredMixin, UpdateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication/update.html'

    def has_permission(self):
        return self.get_object().user == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse('publications:detail', kwargs={'publication_pk': self.object.pk})
    

