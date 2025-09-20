purchases = ['1000','2000','3000','삼천','3000']
# 총 구매금액 
total = 0
for p in purchases:
    try:
        total += int(p)
    except:
        pass
    
print(f'총구매액 : {total}')