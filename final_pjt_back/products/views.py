from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
import requests
from django.http import JsonResponse
from .serializers import DepositProductsSerializer,DepositOptionsSerializer
from .models import DepositProducts,DepositOptions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Create your views here.


API_KEY = '58cc79feef643e06def232dd07ed0b75'

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def api_test(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth':API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response':response})

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth':API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    response = requests.get(URL, params=params).json()

    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')
    
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm' :fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny' :join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
        }

        serializer = DepositProductsSerializer(data=save_data)

        if serializer.is_valid():
            if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
                continue
            serializer.save()
        else:
            continue

    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')

        data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
    
        serializer = DepositOptionsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            fin_prdt_cd = li.get('fin_prdt_cd')
            product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            if DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd,intr_rate=intr_rate,intr_rate_type_nm=intr_rate_type_nm,intr_rate2=intr_rate2,save_trm=save_trm).exists():
                continue
            serializer.save(product=product)

    return JsonResponse({'message':'저장완료'})

# @api_view(['GET','POST'])
# def deposit_products(request):
#     if request.method == 'GET':
#         products = DepositProducts.objects.all()
#         serializers = DepositProductsSerializer(products,many=True)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         serializer = DepositProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def deposit_product_options(request,fin_prdt_cd):
#     product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
#     serializer = DepositOptionsSerializer(product,many=True)
#     return Response(serializer.data)



# @api_view(['GET'])
# def top_rate(request):
#     top_rate_option = DepositOptions.objects.order_by('-intr_rate2')
#     # print(top_rate_option)

#     product = top_rate_option[0].product

#     product_serializer = DepositProductsSerializer(product)
#     options = DepositOptions.objects.filter(product=product)
#     options_serializer = DepositOptionsSerializer(options,many=True)

#     data ={
#         'product':product_serializer.data,
#         'options':options_serializer.data
#     }
#     return Response(data)


@api_view(['GET'])
def age_recommend(request):
    print(request.user)
    # print(user)


@login_required
@api_view(['GET'])
def product_list(request):
    user = request.user  # 로그인된 사용자 정보
    # 여기서 user 정보를 사용하여 필요한 로직을 구현
    return render(request, 'products/product_list.html', {'user': user})