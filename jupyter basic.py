# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 주피터 노트북 사용법
# * Shift + Enter 키를 누르면 셀이 실행되고 커서가 다음셀로 이동합니다.
# * Enter 키를 누르면 다시 편집상태로 돌아옵니다.
# * Esc 키를 누르고
#     * a 키를 누르면 위에 셀이 추가됩니다.
#     * b 키를 누르면 아래에 셀이 추가됩니다.
#     * dd 키를 누르면 셀이 삭제됩니다.
#     * m 키를 누르면 문서 셀로 변경됩니다.
#     * y 키를 누르면 코드 셀로 변경됩니다.
#
#
# ## 마크다운(Markdown)이란?
# * 코드와 함께 문서화를 하실 수 있습니다.
# * 문서화를 할 수 있는 `문법`입니다.
# ```
# 여러 줄의 설명을
# 줄바꿈으로 쓰고자 할 때
# ```

print("Hello World!")

a = 1
b = 2
a + b 

for i in range(10000000000):
    print(i)
