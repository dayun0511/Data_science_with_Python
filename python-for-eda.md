# python for data analysis
* 파이썬 공식 튜토리얼 : https://docs.python.org/3/tutorial/

# Zen of python
* 파이썬의 철학이 잘 담겨있는 Zen of python을 출력해봅니다.
* import를 통해 파이썬의 라이브러리나 패키지를 가져올 수 있습니다.


```python
# PEP20
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    

# boolean
* 파이썬에는 명시적인 것이 암시적인 것보다 낫다라는 철학이 있습니다.
* True나 False는 0과 1로도 표현할 수 있으나 명시적으로 표현하기 위해 True와 False를 사용합니다.


```python
# True를 출력해 보세요.
True
```




    True




```python
# False를 출력해 보세요.
False
```




    False




```python
# True는 1과 같음을 표현해 보세요. 파이썬에서는 같음을 비교할 때 == 연산을 사용합니다.
True == 1
```




    True




```python
# False는 0과 같음을 표현해 보세요. 파이썬에서는 같음을 비교할 때 == 연산을 사용합니다.
False == 0
```




    True




```python
# 하지만 True는 문자 1과는 다릅니다. 1을 따옴표로 감싸면 문자열이 됩니다.
True == "1"
```




    False




```python
# 문자열 1과 True는 다릅니다.
True != "1"
```




    True




```python
# False도 마찬가지 입니다.
False == "0"
```




    False




```python
# False는 문자열 0과 다릅니다.
False != "0"
```




    True




```python
# and 연산으로 True 값끼리 비교합니다.
# and 는 모든값이 True 일 때만 True 가 됩니다.
True and True
```




    True




```python
# and 는 조건 중 하나라도 False 라면 False가 됩니다.
True and False
```




    False




```python
# or 는 하나만 True 라도 True가 됩니다.
True or False
```




    True



# Number and String
* 숫자 1과 문자 "1"은 다릅니다. 숫자1과 문자1의 데이터 타입을 출력해보세요.
* 데이터 타입을 표현할 때 type을 통해 데이터를 출력합니다.


```python
# 숫자 1을 출력해 보세요.
1
```




    1




```python
# 문자 1을 출력해 보세요.
"1"
```




    '1'




```python
# 숫자 1의 데이터 타입을 출력해 보세요.
type(1)
```




    int




```python
# 문자 1의 데이터 타입을 출력해 보세요.
type("1")
```




    str




```python
# 문자 1과 숫자 1을 비교합니다.
1 == "1"
```




    False



# Strings and Lists
* https://docs.python.org/3/tutorial/introduction.html#strings
* https://docs.python.org/3/tutorial/introduction.html#lists


```python
# "Hello World!"를 출력해 봅니다.
"Hello World"
```




    'Hello World'




```python
# 주소 "경기도 성남시 분당구"를 출력해 봅니다.
"경기도 성남시 분당구"
```




    '경기도 성남시 분당구'



|연산자|기능|
|---|---|
|==|비교연산|
|=|할당연산|

## strings


```python
# til 이라는 변수에 문자열을 담아봅니다.
til = "Today I Learned"
til
```




    'Today I Learned'




```python
# 모두 소문자로 만들어 보세요.
til.lower()
```




    'today i learned'




```python
# 모두 대문자로 만들어 보세요.
til.upper()
```




    'TODAY I LEARNED'



## lists


```python
# 비어있는 리스트를 만듭니다. lang이라는 변수에 담습니다.
lang = []
lang
```




    []




```python
# python, java, c를 원소에 추가합니다.
lang.append("python")
lang.append("java")
lang.append("c")
lang
```




    ['python', 'java', 'c']




```python
# lang이라는 변수에 담겨있는 언어명을 인덱싱을 통해 가져옵니다.
lang[0]
```




    'python'




```python
# 1번 인덱스를 가져옵니다.
lang[1]
```




    'java'




```python
# 마지막 인덱스를 가져옵니다.
lang[-1]
```




    'c'



# Control Flow
* [4 - More Control Flow Tools - Python documentation](https://docs.python.org/3/tutorial/controlflow.html)
* 제어문 - 조건문, 반복문


```python
# 반복문을 통해 리스트의 원소를 하나씩 출력합니다.
for i in lang:
    print(i)
```

    python
    java
    c
    


```python
# 위 코드에서 python일 때는 그대로 출력하고 나머지 텍스트는 "기타"라고 출력합니다.
# 출력 결과가 아래의 순서로 나오도록 합니다.
# python
# 기타
# 기타
for i in lang:
    if i == "python":
        print("python")
    else:
        print("기타")
```

    python
    기타
    기타
    


```python
# 특정 횟수만큼 반복문을 실행하도록 합니다.
count = len(lang)
for i in range(count):
    print(lang[i])
```

    python
    java
    c
    


```python
# for문과 if문을 함께 사용해 봅니다.
# 짝수일 때 python을 홀수일 때 java를 출력합니다.
for i in range(1,10):
    if i % 2 == 0:
        print("python")
    else:
        print("java")
```

    java
    python
    java
    python
    java
    python
    java
    python
    java
    


```python
# enumerate를 사용하면 인덱스 번호와 원소를 같이 가져올 수 있습니다.
for i, val in enumerate(lang):
    print(i, val)
```

    0 python
    1 java
    2 c
    

# 문자열


```python
# 주소를 address 변수에 담습니다.
address = " 경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층 "
address
```




    ' 경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층 '




```python
# 앞뒤 공백을 제거합니다.
# 데이터 전처리 시 주로 사용합니다.
'''address.strip으로 공백을 제거하고 다시 address 변수에 담아야 전처리가 완성된다.'''
address = address.strip()
address
```




    '경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층'




```python
# 문자열의 길이
len(address)
```




    33




```python
# 공백으로 문자열 분리
address_list = address.split()
address_list
```




    ['경기도', '성남시', '분당구', '불정로', '6', 'NAVER', '그린팩토리', '16층']




```python
# 리스트 길이
len(address_list)
```




    8



* 슬라이싱, startswith, in을 통해 문자열에 경기가 있는지 확인하기


```python
# 슬라이싱으로 문자 가져오기
address[:2]
```




    '경기'




```python
# startswith를 사용하면 특정 문자가 포함되는지 여부를 확인할 수 있습니다.
address.startswith("경기")
```




    True




```python
# in 을 사용하게 되면 특정 문자열을 포함하고 있는지 여부를 확인할 수 있습니다.
"경기" in address
```




    True



# 리스트
* 문자열에서 쓰는 방법과 비슷하게 메소드 등을 사용할 수 있습니다.
* 차이를 비교해 보세요


```python
# 인덱싱으로 리스트의 원소 가져오기 - 주소에서 구를 가져와 gu라는 변수에 담아보세요.
gu = address_list[2]
gu
```




    '분당구'




```python
# 인덱싱으로 리스트의 원소 가져오기 - 주소에서 도로명을 가져와 street라는 변수에 담아보세요
street = address_list[3]
street
```




    '불정로'




```python
# 리스트의 마지막을 가져옵니다.
address_list[-1]
```




    '16층'




```python
# "  ".join(리스트)를 사용하면 리스트를 공백 문자열을 연결할 수 있습니다.
# 리스트로 분리된 문자열을 다시 연결합니다.
'''따옴표 사이에 공백을 추가해야 공백이 포함된 형태로 연결된다.'''
" ".join(address_list)
```




    '경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층'




```python
# in을 사용하게 되면 리스트에 해당 데이터를 포함하고 있는지 여부를 확인할 수 있습니다.
# "경기"가 리스트에 포함되는지를 봅니다.
'''리스트에 있는 원소를 비교할 때는 반드시 텍스트가 전부 매치 되어야 True 값이 출력된다.'''
"경기도" in address_list
```




    True




```python
# in을 사용하게 되면 리스트에 해당 데이터를 포함하고 있는지 여부를 확인할 수 있습니다.
# "분당구"가 리스트에 포함되는지를 봅니다.
"분당구" in address_list
```




    True




```python

```
