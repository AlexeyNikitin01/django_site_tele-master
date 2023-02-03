from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.db.models import Q

from main.models import TVSale


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = TVSale.objects.filter(
                Q(model_tv__icontains=query) | Q(description_tv__icontains=query)
            )
        paginator = Paginator(results, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'main/searching/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })
