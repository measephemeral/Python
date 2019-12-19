# 로또 번호를 랜덤으로 뽑아주는 프로그램
import random

numbers = range(1,46)
# [1,2,3,....,45] 와 비슷

# 6개의 숫자를 뽑아 출력해주는 프로그램 작성하기

lotto = random.sample(numbers, 6)
print(sorted(lotto))