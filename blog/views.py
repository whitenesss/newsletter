from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Blog


# Create your views here.
class BlogDetailView(DetailView):
    """
    Контроллер отвечающий за отображение детальной страницы блога
    """
    model = Blog
    template_name = 'blog/blog_detaul.html'

    def get_object(self, queryset=None):
        object = super().get_object(queryset)

        object.count_view += 1
        object.save(update_fields=['count_view'])

        return object
