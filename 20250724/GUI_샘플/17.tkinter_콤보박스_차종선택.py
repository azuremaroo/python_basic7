import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk

# 여행 지역 선택 콤보 상자를 추가해서
# 선택한 여행 지역 정보 까지 추가적으로 label에 출력 해주시요!!

def btnclick():
    # 콤보 상자 선택 정보가 없을 경우
    # BrandCombo.current() ==> 선택항목 인덱스 반환
    # BrandCombo.get() ==> 선택항목 내용 반환
    if BrandCombo.current() == -1:
        SeledBrandModel.set("항목을 선택하시요!!")

    else:
        # 콤보상자 선택 정보 획득
        comb1_sel = BrandCombo.get()
        comb2_sel = modelcombo.get()
        # 선택정보 Label에 출력
        SeledBrandModel.set("차 브랜드 : {}, 차종 : {}".format(comb1_sel, comb2_sel))

        combo1text.set('차 브랜드 선택') # 콤보상자 초기화
        combo2text.set('차종 선택') # 콤보상자 초기화

def BrandSelect(event):
    BrandSel_Name = BrandCombo.get()
    BrandSel_idx = BrandCombo.current()
    if BrandSel_idx == -1:
        print(BrandSel_idx)
    else:
        # BrandSel_Name 선택에 따른 모델 정보 리스트 획득
        CarModellist.extend(CarBrandModelDict[BrandSel_Name])
        # 해당 모델 정보 리스트를 modelcombo 콤보박스 values 항목으로 업데이트
        modelcombo['values'] = CarModellist
        # 다른 brand 선택시 추가 되면 안됨으로 클리어
        CarModellist.clear()

mywind = tk.Tk()
# window 창크기 및 출력좌표 설정, 가로x세로 + 창 출력 위치 좌표
mywind.geometry("1200x600+500+200")


combo1text = tk.StringVar(master=mywind) # 일반 combobox 초기 출력값
combo1text.set('차 브랜드 선택') # 일반 combobox 초기 출력값

combo2text = tk.StringVar(master=mywind) # readonly combobox 초기 출력값
combo2text.set('차종 선택') # readonly combobox 초기 출력값

CarBrandModelDict ={
    '현대':['그랜저','아이오닉5','캐스퍼','아반떼'],
    '기아':['K5','K7','K8','니로','스포티지','쏘렌토'],
    '테슬라':['모델3','모델Y'],
    '르노코리아':['QM6','QM3','XM3','SM6'],
    '쉐보레':['스파크','트레일블레이저','크루즈','이쿼녹스'],
    'KG모빌리티':['티볼리','코란도','토레스']
}
CarBrandlist = ['현대','기아','테슬라','르노코리아','쉐보레','KG모빌리티']
CarModellist = []

nonamelb1 = tk.Label(mywind, text="   ")
nonamelb1.grid(row=0, column=0)

font=tkfont.Font(family="Consolas", size=17, weight="bold")
BrandNamelb1 = tk.Label(mywind, text="CarBrand 선택 : ", font=font)
BrandNamelb1.grid(row=1, column=1)

BrandCombo = ttk.Combobox(mywind, height=5, textvariable=combo1text, values=CarBrandlist,state='readonly')
# height : combobox 화살표 누를시 몇개까지 보여줄지 설정(콤보 높이 설정)
# 현 combo1은 combobox 창에 Edit 처럼 직접 입력이 가능함
BrandCombo.grid(row=1, column=2)

nonamelb2 = tk.Label(mywind, text="       ")
nonamelb2.grid(row=1, column=3)

BrandNamelb2 = tk.Label(mywind, text="CarModel 선택 : ", font=font)
BrandNamelb2.grid(row=1, column=4)


# # combo2의 combobox는 state='readonly' 설정으로
# # 임의의 입력 없이 오로지 Combobox에 설정된 값만 선택 가능함
modelcombo = ttk.Combobox(mywind, height=5, values=CarModellist,textvariable=combo2text,state='readonly')
modelcombo.grid(row=1, column=5)

nonamelb2 = tk.Label(mywind, text="       ")
nonamelb2.grid(row=1, column=6)

btn = tk.Button(mywind, text='선택하기',command=btnclick)
btn.grid(row=1, column=7)


nonamelb2 = tk.Label(mywind, text="   ")
nonamelb2.grid(row=2, column=0)

SeledBrandModel = tk.StringVar(master=mywind)

DisplayBrandModellb = tk.Label(mywind, text="선택된 차 브랜드 및 차종 출력",
                                textvariable=SeledBrandModel)
DisplayBrandModellb.grid(row=3, column=1)
SeledBrandModel.set('선택된 차 브랜드 및 차종 출력 ')


# 차 브랜드 선택 콤보 박스 (BrandCombo) 선택 이벤트 처리
BrandCombo.bind("<<ComboboxSelected>>",BrandSelect)


mywind.mainloop()