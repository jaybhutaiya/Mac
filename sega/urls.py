from django.urls import path
from.import views

urlpatterns=[
    path('',views.home.as_view(),name='home'),
    path('course/',views.courses.as_view(),name='course'),
    path('college/',views.college.as_view(),name='college'),
    path('activity/',views.activity.as_view(),name='activity'),
    path('about/',views.about.as_view(),name='about'),
    path('blog/',views.blog.as_view(),name='blog'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('blockchain/',views.blockchain.as_view(),name='blockchain'),
    path('detail/<int:id>',views.detail, name='detail'),
]