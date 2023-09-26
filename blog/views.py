from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Blog
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from service.models import Mailing

from random import sample

from users.models import User


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
        """Создаем счетчик просмотров"""
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


def HomeIndex(request):
    """Домашняя страница"""
    mailing_count = Mailing.objects.all().count()
    active_count = Mailing.objects.filter(status=Mailing.STATUS_CHOICES == 'created').count()
    count_article = User.objects.all().count()
    article_all = Blog.objects.all()

    min_article = min(3, count_article)
    article = sample(list(article_all), min(3, len(list(article_all))))

    context = {
        'mailing_count': mailing_count,
        'active_count': active_count,
        'article': article
    }
    return render(request, 'blog/home.html', context)
