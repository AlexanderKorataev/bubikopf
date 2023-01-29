from django.urls import path

from user_lessons import views

urlpatterns = [
    path('checkout/<slug:product_slug>/', views.checkout),
    path('customer/', views.Lessons.as_view()),
    ]