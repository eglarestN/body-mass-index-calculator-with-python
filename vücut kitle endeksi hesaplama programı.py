person_height=float(input("height (m):"))
person_weight=int(input("weight (kg):"))

index=person_weight/(person_height*person_height)

if index<=18:
	print(f"\n weak BMİ {index}")
elif index>18 and index <=25:
	print(f"\n fat BMİ{index}")
elif index>25 and index<=30:
	print(f"\n obese BMİ {index}")
elif index>30:
	print(f"\n extremely obese BMİ {index}")