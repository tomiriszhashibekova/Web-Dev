from django.urls import path
from api.views import company_list,company_vacancy,one_company,one_vacancy,vacancy_list,top_ten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', one_company),
    path('companies/<int:company_id>/vacancies/', company_vacancy),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', one_vacancy),
    path('vacancies/top_ten/', top_ten)
]