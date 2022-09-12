from django.views.generic.list import ListView
from .models import Quote

class QuotesList(ListView):
    model = Quote
    template_name: str = 'clipboard/index.html'
    context_object_name = "quotes"
    
    def get_queryset(self):
        return Quote.objects.all().order_by('created')
    

