from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from yushen.models import Part
# Create your views here.


''' home page
'''
class IndexView(generic.TemplateView):
    template_name = 'yushen/index.html'
'''
def index(request):
    #return HttpResponse("Welcome to Yushen Elevator Parts Company")
    return render(request, 'yushen/index.html')
'''

''' products list page
'''
class ProductsView(generic.ListView):
    template_name = 'yushen/products.html'
    context_object_name = 'parts_list'
    
    def get_queryset(self):
        'return all the parts in the database'
        return Part.objects.all()
'''
def products(request):
    parts_list = Part.objects.all()
    context = {'parts_list':parts_list}
    return render(request, 'yushen/products.html', context)
'''

''' product detail page
    @param part_db_id: the unicode number grepped from urls: '^products/detail_identifier=(?P<part_db_id>\d)'
'''
class PartDetailView(generic.DetailView):
    model = Part
    template_name = 'yushen/detail.html'
'''
def detail(request, part_db_id):
    # get the object from database with primary key == part_db_id
    part = get_object_or_404(Part, pk=part_db_id)
    context = {'identifier':part.identifier, 'type':part.type, 'elevator': part.elevator}
    return render(request, 'yushen/detail.html', context)
'''
