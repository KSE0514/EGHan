from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products,name='save_deposit_products'),
    path('deposit-products/',views.deposit_products,name='deposit_products'),
    path('deposit-product-detail/<str:fin_prdt_cd>/',views.deposit_product_detail,name='deposit_product_detail'),
    # path('deposit-product-options/<str:fin_prdt_cd>/',views.deposit_product_options,name='deposit_product_options'),
    # path('deposit-products/top_rate/',views.top_rate,name='top_rate'),
    path('api_test/',views.api_test),  # 데이터 조회 용 경로
    path('api_test_saving/',views.api_test_saving),
    path('save-saving-products/',views.save_saving_products,name='save_saving_products'),
    path('deposit-saving-products/',views.deposit_saving_products,name='deposit_saving_products'),
    path('saving-product-detail/<str:fin_prdt_cd>/', views.saving_product_detail),
    path('exchange/',views.get_exchange_rate),
    path('deposit-product-detail/<str:fin_prdt_cd>/<int:user_pk>/',views.deposit_sign),
    path('saving-product-detail/<str:fin_prdt_cd>/<int:user_pk>/',views.saving_sign),
    path('userinfo/',views.user_profile),
    path('recommend-age/',views.recommend_products_by_age),
    path('recommend-salary/',views.recommend_products_by_salary),
    path('recommend-money/',views.recommend_products_by_money),
]