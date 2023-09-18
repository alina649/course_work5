from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Blog
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'preview', 'sign_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogListView(ListView):
    """Контроллер блога для просмотра списка статей"""
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_published=True)
        return queryset


class BlogDetailView(DetailView):
    """Контроллер блога для детального просмотра статьи"""

    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Контроллер блога для редактирования статьи"""

    model = Blog
    fields = ('title', 'description', 'preview', 'sign_published', )

    def get_success_url(self):
        """
        Переопределение url-адреса для перенаправления
        после успешного редактирования
        """

        return reverse('blog:view', args=[self.object.pk])


class BlogDelete(DeleteView):
    """Контроллер блога для удаления статьи"""

    model = Blog
    success_url = reverse_lazy('blog:list')
