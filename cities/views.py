from typing import Any, Dict

from django.core.paginator import Paginator
from django.db.models import Count
from django.views.generic import TemplateView

from cities.models import Citizen, City


class CitizenView(TemplateView):
    template_name = 'cities/cities.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        city = self.kwargs['city']
        citizens = Citizen.objects.filter(city__name=city)
        paginator = Paginator(citizens, 20)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        context['city'] = city
        return context


class CityView(TemplateView):
    template_name = 'cities/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        top_cities = City.objects.annotate(
            num_citizens=Count('citizen')).order_by('-num_citizens')[:10]
        citizens = Citizen.objects.order_by('name')
        paginator = Paginator(citizens, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        context['top_cities'] = top_cities
        return context
