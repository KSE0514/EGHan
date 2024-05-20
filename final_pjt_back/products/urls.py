from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products,name='save_deposit_products'),
    # path('deposit-products/',views.deposit_products,name='deposit_products'),
    # path('deposit-product-options/<str:fin_prdt_cd>/',views.deposit_product_options,name='deposit_product_options'),
    # path('deposit-products/top_rate/',views.top_rate,name='top_rate'),
    path('api_test/',views.api_test),  # 데이터 조회 용 경로
    path('age/', views.age_recommend),
    path('list/',views.product_list),
    path('exchange/',views.get_exchange_rate),
]