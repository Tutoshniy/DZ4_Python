def dictionary(**kwargs):
    answer = dict([])
    for value, key in kwargs.items():
        answer.update([(f'{key}', value)])
    return answer


print(dictionary(химия=5, физика=4))
