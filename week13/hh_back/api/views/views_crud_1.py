from django.http.response import JsonResponse
from api.models import Company,Vacancy
from django.http import Http404
from django.views.decorators.csrf import  csrf_exempt
import json

@csrf_exempt
def company_list(request):
    if request.method=='GET':
       companies = Company.objects.all()
       companies_json = [company.to_json() for company in companies]

       return JsonResponse(companies_json, safe = 0)
    elif request.method =='POST':
        request_body = json.loads(request.body)
       # print(request_body)
        company= Company.objects.create(name=request_body.get('name'))
        return JsonResponse(company.to_json())


















@csrf_exempt
def one_company(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        raise Http404

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method =='PUT':
        request_body = json.loads(request.body)
        company.description=request_body.get('description',company.description)
        company.city=request_body.get('city', company.city)
        company.address=request_body.get('address', company.address)
        company.name = request_body.get('name', company.name)
        company.save()
        return JsonResponse(company.to_json())
    elif request.method=='DELETE':
        company.delete()
        return JsonResponse({'delete':True})









def company_vacancy(request, company_id):
    vacancies = Vacancy.objects.all()
    info = []
    for item in vacancies:
        if item.id == company_id:
            info.append(item.to_json())
    return JsonResponse(info, safe=False)

def vacancy_list(request):
    vacancies= Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=0)


def one_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json())


def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)