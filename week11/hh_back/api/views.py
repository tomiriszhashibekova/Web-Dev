from django.http.response import JsonResponse
from api.models import Company,Vacancy
from django.http import Http404


def company_list(request):

    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe = 0)


def one_company(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json())

def company_vacancy(request, company_id):
    vacancies = Vacancy.objects.all()
    info = []
    for item in vacancies:
        if item.company_id.id == company_id:
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