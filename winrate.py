import math

k = -1.5 #극대화값
MetaA = [0.7, 0.9, 0.5] #메타점수
MetaB = [1.1, 1.5, 1.4]
MapA = [0.1, 0.3, 0.4] #맵점수
MapB = [1.6, 1.5, 1.8]
BrawlerA = [0.2, 0.1, 0.5] #각 브롤러 상성들의 평균을 모아둔거 (브롤러1의 상대 평균 상성, 브롤러2의 상대 평균 상성, 브롤러3의 상대 평균 상성)
BrawlerB = [1.5, 1.8, 1.8]

def CalPointA(n):
    pt = 0
    for i in range(n):
        pt += MetaA[i]*0.4 + MapA[i]*0.3 + BrawlerA[i]*0.3
    return pt

def CalPointB(n):
    pt = 0
    for i in range(n): 
        pt += MetaB[i]*0.4 + MapB[i]*0.3 + BrawlerB[i]*0.3
    return pt

getWinRate = lambda diff: round(1 / (1 + math.exp(k * diff)) * 100, 2) #승률 구하는 로지스터 공식
print(getWinRate(CalPointA(3) - CalPointB(3)))
