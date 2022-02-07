tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):

    for i in range(len(tutors)):
       yield (tutors[i], klasses[i] if i < len(klasses) else None)
# актуально ли тут использовать zip?


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))

#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration