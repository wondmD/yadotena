#urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('addproduct/', views.register_product, name='product_add'),
    path('addsell/', views.register_sell, name='sell_form'),
    path('addexpence/', views.register_expense, name='expense_add'),
    path('tables/', views.tabels, name='tables'),
    path('login/', views.login_user, name='login'),
    # path('listproducts', views.ProductList.as_view(), name='product_list'),
    # path('listsells', views.SellList.as_view(), name='sell_list'),
    # path('listexpenses', views.ExpenseList.as_view(), name='expense_list'),
]