import random

from data.geocoder import get_ll_span
from data.mapapi_PG import show_map


def main():
    # Список городов Золотого кольца.
    towns = ["Сергиев Посад",
             "Переславль-Залесский",
             "Ростов Великий",
             "Ярославль",
             "Кострома",
             "Иваново",
             "Суздаль",
             "Владимир"]
    random.shuffle(towns)

    for town in towns:
        print(f"Сейчас отображается {town}.")
        # Показываем карту с масштабом, подобранным по заданному объекту.
        ll, spn = get_ll_span(town)
        map_type = random.choice(["sat", "map"])
        if map_type == "map":
            spn = "0.001,0.001"
        ll_spn = "ll={ll}&spn={spn}".format(**locals())
        show_map(ll_spn, map_type)
        random.shuffle(towns)


if __name__ == "__main__":
    main()
