from django.urls import path
from api.views import company_vacancy,one_company,one_vacancy,vacancy_list,top_ten
from api.views.views_cbv import APIView, CompanyListAPIView, OneCompanyAPIView, CompanyVacancyAPIView, \
    OneVacancyAPIView, VacancyListAPIView
from api.views.views_fbv import company_list,company_vacancy,one_company,vacancy_list,one_vacancy
#from api.views.views_generic import CompanyListAPIView,OneCompanyAPIView,CompanyVacancyAPIView,VacancyListAPIView,OneVacancyAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    # path('companies/', company_list),
    # path('companies/<int:company_id>/', one_company),
    # path('companies/<int:company_id>/vacancies/', company_vacancy),
    # path('vacancies/', vacancy_list),
    # path('vacancies/<int:vacancy_id>/', one_vacancy),
    # path('vacancies/top_ten/', top_ten)
    path('login/',obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', OneCompanyAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacancyAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', OneVacancyAPIView.as_view()),
]