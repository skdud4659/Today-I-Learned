n=int(input())         #26


bag=0
while n>=0:           #26은 0보다 큼
    if n % 5 == 0 :   #26은 6의 배수가 아님
        bag += n//5
        print(bag)
        break
    n-=3              #3kg 무게를 추가하기 위해 26에서 3을 뺀 23
    bag+=1            #3kg 봉지 1개 추가 > 23을 가지고 다시 반복 하면 결국 20이 나옴 > 20으로 반복문을 돌리면 5의 배수이기 때문에 몫인 4봉지가 추가되어 총 6봉지
else:
    print(-1)         #최소 키로 봉지가 3kg이기 때문에 n에서 3키로를 뺐을 때 -값이 나오면 -1이 프린트됨

