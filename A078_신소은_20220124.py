# programmers - H-Index

"""
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
"""

citations.sort()
result = 0
for i in range(len(citations)):
    if citations[i] >= len(citations)-i:
        result = max(result, len(citations)-i)
return result