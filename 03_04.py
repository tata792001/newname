#l=[(23,12),(12,26),(34,67),(34,23),(256,45)]
#l=sorted(l, key=lambda x: x[1], reverse=True)
#print(l)

#stroka=["qwe","qwewd","dfhrvreg","swre","fergfee"]
#print(sorted(stroka, key=len, reverse=True))


#l="у попа была собака"
def f(l):
    for i in l.split():
        yield i ###возвращает одно из этих слов###

    #ptint(next(l))

    #a=f(l)


a = f("b cyjdf htibntkmysq  jq")
for i in a:
    print(i)
#print(next(a))### следующее число###