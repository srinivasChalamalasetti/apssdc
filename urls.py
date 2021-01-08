from django.urls import path
from Details import views
from django.contrib.auth import views as g

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    path('rg/',views.register,name="reg"),
    path('ds/',views.dashboard,name="dsh"),
    path('pf/',views.prfle,name="pfe"),
    path('upf/',views.updf,name="upfe"),
    path('vd/',views.vds,name="vd1"),
    path('vid/',views.vdds,name="vd2"),
    path('vlid/',views.vi,name="vd3"),
    path('vdd/',views.lik,name="vd4"),
    path('vvd/',views.su,name="vd5"),
    path('vod/',views.sd,name="vd6"),
    path('ord/',views.ordls,name="or"),
    path('corli/',views.corlist,name="cor"),
    path('abc/',views.companies,name="dc"),
    path('lg/',g.LoginView.as_view(template_name="sd/login.html"),name="lgn"),
    path('lgg/',g.LogoutView.as_view(template_name="sd/logout.html"),name="lgo"),

]
