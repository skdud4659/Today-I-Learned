# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

n = int(input())  #26
chk = n
new_n = 0         #새로운 수
temp = 0          #첫째 자리와 두번째 자리를 더한 수
count = 0         #사이클 수

#while 반복문 : 조건문이 참인 동안에 아래 문장이 반복해서 수행된다.
while True : 
    #// : 나누기 연산 후 정수 부분의 몫
    #% : 나누기 연산 후 나머지
    #n을 10으로 나누면 10의 자리 숫자가 몫, 1의 자리 숫자가 나머지가 되어 이 두 수를 더해준다.
    temp = n//10 + n%10            #8
    #new_n은 1의 자리 숫자였던 나머지에 10을 곱해 10의 자리 숫자로 만들고 temp의 나머지를 1의 자리에 위치하게 한다.
    new_n = (n%10)*10 + temp%10    #68
    #반복문이 돌아갈때마다 count에 1씩 더해준다.
    count += 1
    n = new_n
    if new_n == chk:
        break
print(count)