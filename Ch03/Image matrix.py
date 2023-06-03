import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from dataset.mnist import load_mnist

np.set_printoptions(linewidth=150,threshold=1000)   # 소수점 컨트롤 할 수 있는 함수

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False, normalize=False)

print(x_train[0])

print(t_train[0])