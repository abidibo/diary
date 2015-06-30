from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404

import filippo

class DiaryView(ListView):
    """ List of all pages
    """
    model = filippo.models.Page
    queryset = filippo.models.Page.objects.all()
    template_name = 'filippo/diary.html'
    paginate_by = 5

class PageView(DetailView):
    """ List of all pages
    """
    model = filippo.models.Page
    queryset = filippo.models.Page.objects.all()
    template_name = 'filippo/page.html'

