from django.contrib import admin
from django.urls import include,path
urlpatterns=[path("admin/",admin.site.urls),path("",include("dashboard.urls")),path("engineering/",include("engineering_dept.urls")),path("marketing/",include("marketing_dept.urls")),path("sales/",include("sales_dept.urls"))]
