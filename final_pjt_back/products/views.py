from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
import requests
from django.http import JsonResponse
from .serializers import DepositProductsSerializer,DepositOptionsSerializer,SavingProductsSerializer,SavingOptionsSerializer,RecommendedProductSerializer
from .models import DepositProducts,DepositOptions, SavingProducts, SavingOptions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.serializers import UserSerializer


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

@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(products,many=True)
        return Response(serializers.data)
#     if request.method == 'POST':
#         serializer = DepositProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deposit_product_detail(request,fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_product_options(request,fin_prdt_cd):
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(product,many=True)
    return Response(serializer.data)



#적금
@api_view(['GET'])
def api_test_saving(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth':API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response':response})


@api_view(['GET'])
def save_saving_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    result = response.get('result')

    if not result:
        return JsonResponse({'message': 'API 응답 데이터가 없습니다.'}, status=400)

    base_list = result.get('baseList')
    option_list = result.get('optionList')

    if not base_list or not option_list:
        return JsonResponse({'message': 'baseList 또는 optionList 데이터가 없습니다.'}, status=400)

    # SavingProducts 저장
    for li in base_list:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
        }

        serializer = SavingProductsSerializer(data=save_data)
        if serializer.is_valid():
            if not SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
                serializer.save()
            else:
                print(f"SavingProducts with fin_prdt_cd {fin_prdt_cd} already exists.")
        else:
            print(serializer.errors)  # 유효성 검사 오류 출력

    # SavingOptions 저장
    for li in option_list:
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')

        data = {
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }

        serializer = SavingOptionsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            try:
                product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                if not SavingOptions.objects.filter(product=product, intr_rate=intr_rate, intr_rate_type_nm=intr_rate_type_nm, intr_rate2=intr_rate2, save_trm=save_trm).exists():
                    serializer.save(product=product)
            except SavingProducts.DoesNotExist:
                print(f"SavingProducts with fin_prdt_cd {fin_prdt_cd} does not exist.")
        else:
            print(serializer.errors)  # 유효성 검사 오류 출력

    return JsonResponse({'message': '저장완료'})

@api_view(['GET','POST'])
def deposit_saving_products(request):
    if request.method == 'GET':
        products = SavingProducts.objects.all()
        serializers = SavingProductsSerializer(products,many=True)
        return Response(serializers.data)


@api_view(['GET'])
def saving_product_detail(request,fin_prdt_cd):
    product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer(product)
    return Response(serializer.data)


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



# 상품 가입하기
@api_view(['POST'])
def deposit_sign(request, fin_prdt_cd, user_pk):
    # cd에 맞는 적금 정보를 가지고옴
    deposit_info = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    # user_pk에 맞는 유저 정보를 가지고옴
    User_info = User.objects.get(pk=user_pk)
    # 만약 유저의 deposit(Manytomanyfield)에서 이미 존재한다면?
    if deposit_info in User_info.product_user.all():
        # 삭제
        User_info.product_user.remove(deposit_info)
    else:
        # 없으면 추가
        User_info.product_user.add(deposit_info)
    User_info.save()
    # 최신화 된 유저정보를 Response로 반환하기 위해 직렬화
    User_info = UserSerializer(User_info)
    # 반환
    return Response(User_info.data, status=status.HTTP_200_OK)


#적금 가입
@api_view(['POST'])
def saving_sign(request, fin_prdt_cd, user_pk):
    # cd에 맞는 적금 정보를 가지고옴
    saving_info = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    # user_pk에 맞는 유저 정보를 가지고옴
    User_info = User.objects.get(pk=user_pk)
    # 만약 유저의 deposit(Manytomanyfield)에서 이미 존재한다면?
    if saving_info in User_info.savingproduct_user.all():
        # 삭제
        User_info.savingproduct_user.remove(saving_info)
    else:
        # 없으면 추가
        User_info.savingproduct_user.add(saving_info)
    User_info.save()
    # 최신화 된 유저정보를 Response로 반환하기 위해 직렬화
    User_info = UserSerializer(User_info)
    # 반환
    return Response(User_info.data, status=status.HTTP_200_OK)


# 가입한 유저 정보 불러오기 위한 함수
from .serializers import UserSerializer

@api_view(['GET'])
def user_profile(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=401)
    
    serializer = UserSerializer(user)
    return Response(serializer.data)


# 환율 계산기
# exchange/views.py
from django.http import JsonResponse
import requests
import os
from datetime import datetime

def get_exchange_rate(request):
    authkey = "WkgQAiW98R1p0dGJw4ssv16equukjVKB"
    # authkey = os.getenv('EXCHANGE_API_KEY')  # 환경변수에서 API 키를 가져옵니다
    print("API Key:", authkey)  # API 키를 출력하여 확인
    if not authkey:
        return JsonResponse({"error": "API key not found"}, status=500)
    
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&data=AP01"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=response.status_code)
    





## 추천 알고리즘

from django.shortcuts import render
from .models import DepositProducts, SavingProducts
from django.db.models import Q, F, Avg, StdDev
from collections import Counter
from django.db.models import IntegerField ,ExpressionWrapper, Case, When
import math

# 연령대 별 추천
@api_view(['GET'])
def recommend_products_by_age(request):
    # 현재 로그인된 사용자의 연령대 가져오기 (예시로 30대로 가정)
    user_age = request.user.age // 10
    # user_age = 34//10

    # 해당 연령대에 속하는 사용자들의 financial_products 가져오기
    users_in_age_group = User.objects.annotate(
    age_divided_by_10=ExpressionWrapper(
        F('age') / 10,
        output_field=IntegerField()
        )
    ).filter(
        age_divided_by_10=user_age
    )
    # 해당 연령대에 속하는 사용자들의 가입 상품코드를 모으기
    all_product_codes = []
    for user in users_in_age_group:
        if user.financial_products:
            all_product_codes.extend(user.financial_products.split(','))

    # 각 상품의 가입 횟수를 카운트
    product_counts = Counter(all_product_codes)
    # print(product_counts)
    # 가입 횟수가 많은 순으로 정렬된 상품 코드 목록 가져오기
    sorted_product_codes = [product_code for product_code, count in product_counts.most_common()]

    # print(sorted_product_codes)
    # 상품 코드를 사용하여 상품 객체들을 조회
    recommended_deposit_products = DepositProducts.objects.filter(fin_prdt_cd__in=sorted_product_codes)
    recommended_saving_products = SavingProducts.objects.filter(fin_prdt_cd__in=sorted_product_codes)

    
    # 추천 상품을 직렬화하여 응답으로 보냄 (필요시 직렬화 과정 추가 필요)
    deposit_serializer = DepositProductsSerializer(recommended_deposit_products, many=True)
    saving_serializer = SavingProductsSerializer(recommended_saving_products, many=True)
    # print(deposit_serializer.data)

    sorted_deposit_products = sorted(deposit_serializer.data, key=lambda x: sorted_product_codes.index(x['fin_prdt_cd']))[:5]
    sorted_saving_products = sorted(saving_serializer.data, key=lambda x: sorted_product_codes.index(x['fin_prdt_cd']))[:5]
    return Response({
        'recommended_deposit_products': sorted_deposit_products,
        'recommended_saving_products': sorted_saving_products
    })



# 연봉(소득분위) 별 추천
def get_salary_grade(salary):
    if salary <= 1622890:
        return 1
    elif salary <= 2700482:
        return 2
    elif salary <= 3781000:
        return 3
    elif salary <= 4861000:
        return 4
    elif salary <= 5401000:
        return 5
    elif salary <= 7022000:
        return 6
    elif salary <= 8102000:
        return 7
    elif salary <= 10802000:
        return 8
    elif salary <= 16203609:
        return 9
    else:
        return 10


@api_view(['GET'])
def recommend_products_by_salary(request):
    # 현재 로그인된 사용자의 연봉 가져오기 (예시로 30대로 가정)
    user_salary = request.user.salary
    # user_salary = 3482904
    user_salary_grade = get_salary_grade(user_salary)

    # 동일 소득 등급에 속하는 사용자들의 financial_products 가져오기
    users_in_salary_grade = User.objects.annotate(
        salary_grade=Case(
            When(salary__lt=1622890, then=1),
            When(salary__lt=2700482, then=2),
            When(salary__lt=3781000, then=3),
            When(salary__lt=4861000, then=4),
            When(salary__lt=5401000, then=5),
            When(salary__lt=7022000, then=6),
            When(salary__lt=8102000, then=7),
            When(salary__lt=10802000, then=8),
            When(salary__lt=16203609, then=9),
            default=10,
            output_field=IntegerField()
        )
    ).filter(
        salary_grade=user_salary_grade
    )

    # 해당 소득 등급에 속하는 사용자들의 가입 상품코드를 모으기
    all_product_codes = []
    for user in users_in_salary_grade:
        if user.financial_products:
            all_product_codes.extend(user.financial_products.split(','))

    # 각 상품의 가입 횟수를 카운트
    product_counts = Counter(all_product_codes)

    # 가입 횟수가 많은 순으로 정렬된 상품 코드 목록 가져오기
    sorted_product_codes = [product_code for product_code, count in product_counts.most_common()]

    # 상품 코드를 사용하여 상품 객체들을 조회
    recommended_deposit_products = DepositProducts.objects.filter(fin_prdt_cd__in=sorted_product_codes)
    recommended_saving_products = SavingProducts.objects.filter(fin_prdt_cd__in=sorted_product_codes)

    # 추천 상품을 직렬화하여 응답으로 보냄 (필요시 직렬화 과정 추가 필요)
    deposit_serializer = DepositProductsSerializer(recommended_deposit_products, many=True)
    saving_serializer = SavingProductsSerializer(recommended_saving_products, many=True)

    # 직렬화된 결과를 정렬
    sorted_deposit_products = sorted(deposit_serializer.data, key=lambda x: sorted_product_codes.index(x['fin_prdt_cd']))[:5]
    sorted_saving_products = sorted(saving_serializer.data, key=lambda x: sorted_product_codes.index(x['fin_prdt_cd']))[:5]

    return Response({
        'recommended_deposit_products': sorted_deposit_products,
        'recommended_saving_products': sorted_saving_products
    })



# 자산별 추천
def get_percentile_rank(value, values):
    # 자산이 상위 몇프로인지 계산
    sorted_values = sorted(values)
    rank = sorted_values.index(value) / len(sorted_values)
    return rank * 100

@api_view(['GET'])
def recommend_products_by_money(request):
    # 모든 사용자의 자산 정보를 가져옴
    all_users = User.objects.all()
    user_money_list = [user.money for user in all_users]

    # 현재 로그인된 사용자의 자산 가져오기 (예시로 로그인된 사용자의 id를 1로 가정)
    current_user = User.objects.get(id=request.user.id)
    user_money = current_user.money
    # user_money = 48391334

    # 자산의 평균과 표준편차 계산
    # avg_money = sum(user_money_list) / len(user_money_list)
    # std_dev_money = math.sqrt(sum((x - avg_money) ** 2 for x in user_money_list) / len(user_money_list))

    # 사용자의 자산이 상위 몇 퍼센트인지 계산
    user_percentile = get_percentile_rank(user_money, user_money_list)

    # 사용자의 자산이 속하는 구간 계산
    asset_group = min(4, int(user_percentile // 20)) + 1

    # 해당 자산 구간에 속하는 사용자들의 financial_products 가져오기
    percentile_range = [(i * 20, (i + 1) * 20) for i in range(5)]
    lower_bound, upper_bound = percentile_range[asset_group - 1]
    
    users_in_asset_group = [user for user in all_users if lower_bound <= get_percentile_rank(user.money, user_money_list) < upper_bound]
    
    # 해당 자산 구간에 속하는 사용자들의 가입 상품코드를 모으기
    all_product_codes = []
    for user in users_in_asset_group:
        if user.financial_products:
            all_product_codes.extend(user.financial_products.split(','))

    # 각 상품의 가입 횟수를 카운트
    product_counts = Counter(all_product_codes)

    # 가입 횟수가 많은 순으로 정렬된 상품 코드 목록 가져오기
    sorted_product_codes = [product_code for product_code, count in product_counts.most_common()]

    # 상품 코드를 사용하여 상품 객체들을 조회
    recommended_deposit_products = DepositProducts.objects.filter(fin_prdt_cd__in=sorted_product_codes)
    recommended_saving_products = SavingProducts.objects.filter(fin_prdt_cd__in=sorted_product_codes)

    # 추천 상품을 직렬화하여 응답으로 보냄 (필요시 직렬화 과정 추가 필요)
    deposit_serializer = DepositProductsSerializer(recommended_deposit_products, many=True)
    saving_serializer = SavingProductsSerializer(recommended_saving_products, many=True)

    # 직렬화된 결과를 정렬
    sorted_deposit_products = sorted(deposit_serializer.data, key=lambda x: sorted_product_codes.index(x['fin_prdt_cd']))[:5]
    sorted_saving_products = sorted(saving_serializer.data, key=lambda x: sorted_product_codes.index(x['fin_prdt_cd']))[:5]

    return Response({
        'recommended_deposit_products': sorted_deposit_products,
        'recommended_saving_products': sorted_saving_products
    })