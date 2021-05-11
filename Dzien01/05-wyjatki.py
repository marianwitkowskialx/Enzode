
# Wyjątki

try:
    l = [0,1,2,3,4]
    #1/0
    #x = l[111]
    raise StopIteration("brak danych")
except ZeroDivisionError as exc:
    print("Nie dziel przez zero", exc)
except IndexError as exc:
    print("Wartość poza zakresem", exc)
except BaseException as exc:
    print("Wystąpił wyjątek" ,exc)
else:
    # wykona się, jesli nie bylo wyjatku
    print("Obyło się bez wyjątku")
finally:
    print("zawsze się wykona")
