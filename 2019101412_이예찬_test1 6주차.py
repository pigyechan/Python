num = input('용도: 1:주택용, 2:공업용, 3:산업용?')
if(num == '1'or num == '2'or num == '3' ):
    usage = int(input('사용량(kwh)?'))
    
    if(num == '1'):
        cost = float(910+(usage*88))
    if(num == '2'):
        cost = float(1600+(usage*182))
    if(num == '3'):
        cost = float(7300+(usage*275))

    print(f"용도:{num}, 사용량:{usage:.2f}, 전기요금:{cost:,.2f}원")
    
else:
    print('잘못 입력되었습니다.')

