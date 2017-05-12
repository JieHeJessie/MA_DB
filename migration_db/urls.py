"""MA_DB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from migration_db import views

urlpatterns = [
   url(r'^MA_DB/$',views.login, name='login'),
   url(r'^MA_DB/login_result$',views.login_result, name='login_result'),
   url(r'^MA_DB/register$',views.register, name='register'),
   url(r'^MA_DB/register_result$',views.register_result, name='register_result'),
   url(r'^node/(?P<node_name_slug>[\w\-]+)/$',views.node, name='node'),
   url(r'^MA_DB/index$',views.index, name='index'),
   url(r'^MA_DB/quote$',views.quote_page,name='quote_page'),
   url(r'^MA_DB/import$',views.import_page,name='import_page'),
   url(r'^MA_DB/import_project$',views.import_project,name='import_project'),
url(r'^MA_DB/read_project$',views.read_project,name='read_project'),
   url(r'^MA_DB/invoice$',views.invoice_page,name='invoice_page'),
   url(r'^MA_DB/search$',views.search,name='search'),
url(r'^MA_DB/search_result$',views.search_result,name='search_result'),
   url(r'^MA_DB/quote_grant$',views.quote_grant,name='quote_grant'),
   url(r'^MA_DB/invoice_result$',views.invoice_result,name='invoice_result'),
   url(r'^MA_DB/quote_status$',views.quote_status,name='quote_status'),
   url(r'^MA_DB/quote_status_result$',views.quote_status_result,name='quote_status_result'),

   url(r'^MA_DB/quote_grant_result$', views.quote_grant_result, name='quote_grant_result'),
   url(r'^MA_DB/quote_company$', views.quote_company, name='quote_company'),

url(r'^MA_DB/quote_company_result$', views.quote_company_result, name='quote_company_result'),
   url(r'^MA_DB/(?P<quote_id>[0-9]*)/quote_grant_detail/$', views.quote_grant_detail, name='quote_grant_detail'),
   url(r'^MA_DB/(?P<quote_id>[0-9]*)/quote_status_detail/$', views.quote_status_detail, name='quote_status_detail'),
url(r'^MA_DB/(?P<invoice_id>[0-9]*)/invoice_detail/$', views.invoice_detail, name='invoice_detail'),
url(r'^MA_DB/(?P<quote_id>[0-9]*)/quote_company_detail/$', views.quote_company_detail, name='quote_ompany_detail'),
url(r'^MA_DB/(?P<search_id>[0-9]*)/search_detail/$', views.search_detail, name='search_detail'),
   url(r'^MA_DB/import$',views.import_page,name='import_page'),

   # url(r'^MA_DB/import_project$',views.import_project,name='import_projet'),
   #url(r'^MA_DB/UM/projects_list/$',views.projects_list, name ='projects_list'),
   url(r'^MA_DB/(?P<node_name_slug>[\w\-]+)/projects_list/$',views.projects_list, name='node'),
   url(r'^MA_DB/(?P<pro_id>[0-9]*)/project_detail/$',views.project_detail,name ='project_detail'),
   url(r'^MA_DB/(?P<node_name_slug>[\w\-]+)/income_chart/$',views.node_chart,name ='node_chart'),
   url(r'^MA_DB/(?P<node_name_slug>[\w\-]+)/filter_infor/$',views.filter_page,name ='filterpage'),
   url(r'^MA_DB/(?P<node_name_slug>[\w\-]+)/filter_result$',views.filter_result,name ='filterresult'),
   url(r'^MA_DB/chart_page/$',views.chart_page,name ='chart_page'),
   url(r'^MA_DB/chart_page/chartbynode$',views.chartbynode,name ='chartbynode'),
   url(r'^MA_DB/state_page/$',views.state_page,name ='state_page'),

   url(r'^MA_DB/state_page/allNodesByState_result$',views.filter_state,name ='state_result'),
   url(r'^MA_DB/com/$', views.compute_ab,name='compute'),
   url(r'^MA_DB/com/add/$', views.add,name='add'),
   url(r'^admin/', admin.site.urls),
]
