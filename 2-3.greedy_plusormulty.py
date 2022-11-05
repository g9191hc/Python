#0~9중 임의의 수로 이루어진 연속된 숫자열을 받아서, 왼쪽부터 순서대로 더하거나 곱하여 가장 큰 수를 만드는 문제
#왼쪽의 계산된 수와 그 다음수 둘 중 하나가 2이상일 경우는 곱하는게 무조건 유리함

num = input()  # input함수는 default가 문자열임. 예를들어 1234를 입력하면 "1","2","3","4"의 문자로 받아들임.
leftnum = int(num[0]) #첫번째 숫자를 정수로 변경

for i in range(1, len(num)):
  nextnum = int(num[i])
  if leftnum <= 1 or nextnum <= 1 :
    leftnum += nextnum
  else :
    leftnum *= nextnum
  
print(leftnum)