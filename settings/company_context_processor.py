from .models import Company
from categorys.models import Category



def get_company_data(request):
    data = Company.objects.last()
    category = Category.objects.all()
    return {'company_data':data, 'categorys':category}


