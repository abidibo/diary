from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404

import melissa

class DiaryView(ListView):
    """ List of all pages
    """
    model = melissa.models.Page
    queryset = melissa.models.Page.objects.all()
    template_name = 'melissa/diary.html'
    paginate_by = 5

class PageView(DetailView):
    """ List of all pages
    """
    model = melissa.models.Page
    queryset = melissa.models.Page.objects.all()
    template_name = 'melissa/page.html'

