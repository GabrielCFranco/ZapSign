from django.urls import re_path
from crudHandler import views

urlpatterns =[
    re_path(r'^company/$', views.companyApi),
    re_path(r'^company/([0-9]+)$', views.companyApi),
    re_path(r'^documents/$', views.documentsApi),
    re_path(r'^documents/([0-9]+)$', views.documentsApi),
    re_path(r'^signers/$', views.signersApi),
    re_path(r'^signers/([0-9]+)$', views.signersApi),
    re_path(r'^documents_signers/', views.documents_signersApi),
]