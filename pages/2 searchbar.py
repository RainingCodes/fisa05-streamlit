import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 텍스트를 입력받아서 해당 텍스트와 일치하는 이미지를 화면에 출력하는 검색창을 만들어 주세요.


ani_name = st.text_input('애니메이션 이름 입력')

if ani_name:
    for ani in ani_list:
        if ani_name in ani:
            st.image(img_list[ani_list.index(ani)])

# b = st.text_input("애니메이션 이름을 입력하세요")

# for i in range(3): # 하드코딩 - 숫자, 변수명을 고정된 값으로 작성해놓는
#     if b in ani_list[i] :
#         st.image(img_list[i])

# 소프트코딩 - 변화가 많은 데이터를 사용할 때는 변수의 변화에 따라 코드도 함께 바뀌며 동작하는 것을 권장합니다.
if tmp_input := st.text_input('에니메이션을 입력해주세요.'):
     for i, el in enumerate(ani_list):
         if tmp_input in el:
             st.image(img_list[i])