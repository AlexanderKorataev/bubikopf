from django.urls import path, include

from order import views 

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.LatestOrdersList.as_view()),
    path('orders/<slug:randomID>/', views.OrderDetail.as_view()),
    path('user_orders/', views.UserOrdersList.as_view()),
]
