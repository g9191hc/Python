# 공백(띄어쓰기)로 구분되는 두 수를 입력받아서 1이 될 때 까지, 뒤의 수로 앞의 수를 나눌 수 있으면 나누고 아니면 1을 빼는 알고리즘
# 2이상의 수는 항상 나누는 것이 유리하므로, 나누는 것을 빼는 것 보다 항상 우선시 해야하므로 그리디 알고리즘임

n, m = map(int, input().split()) #input()의 메서드인 split()은 default값이 공백임(띄어쓰기 여러개, 탭도 상관 없음)
count = 0 #나누거나 1을 빼는 횟수를 기록

while True: #매번 확인 후 나누거나 1을 빼는것이 아니므로 시간복잡도가 O(log)임
  target = (n // m) * m  #n을 m으로 나눈 몫을 target으로 저장
  count += n - target # target이 될 때 까지 n에서 1을 빼야하는 횟수.
  n = target
  if n < m :
    count += n-1
    print(count)
    break
  count += 1
  n //= m # 어짜피 n으로 m이 나누어 떨어지지만 /연산의 결과는 실수이므로, 정수로 반환하기 위해서는 // 연산자를 사용
  