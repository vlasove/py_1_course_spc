soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']

days = int(input()) #10000000

mult = days // 5 + 1
soups = soups * mult 
for i in range(days): #0,1,2,3,4,5,6,7,8,9
    print(soups[i])