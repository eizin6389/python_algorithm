def gengo(year):
    if year >= 2019:
        return "令和"+str(year-2019+1)+"年"
    elif year < 2019 and year >= 1989:
        return "平成"+str(year-1989+1)+"年"
    elif year < 1989 and year >= 1926:
        return "昭和"+str(year-1926+1)+"年"
    elif year < 1926 and year >= 1912:
        return "大正"+str(year-1912+1)+"年"
    else:
        return "明治"+str(year-1868+1)+"年"

for i in range(1869, 2021):
    print(str(i) +" "+gengo(i))
