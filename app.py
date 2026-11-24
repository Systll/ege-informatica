import json
from pathlib import Path

from flask import Flask, abort, render_template

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
TASKS_DIR = BASE_DIR / "data" / "tasks"

TASK_TITLES = {
    1: "Анализ таблиц и графов",
    2: "Таблицы истинности логических выражений",
    3: "Базы данных",
    4: "Кодирование и декодирование информации",
    5: "Анализ алгоритмов для исполнителя",
    6: "Программа, управляющая исполнителем",
    7: "Объём изображений, звука и видео",
    8: "Комбинаторика",
    9: "Электронные таблицы",
    10: "Поиск слова в текстовом документе",
    11: "Вычисление количества информации",
    12: "Выполнение алгоритма для исполнителя",
    13: "IP-адреса и маска сети",
    14: "Системы счисления",
    15: "Истинность логических выражений",
    16: "Рекурсивные алгоритмы",
    17: "Обработка целочисленных данных из файла",
    18: "Электронные таблицы: путь по клеткам",
    19: "Теория игр (1 вопрос)",
    20: "Теория игр (2 вопроса)",
    21: "Теория игр (3 вопроса)",
    22: "Многопоточные процессы",
    23: "Динамическое программирование",
    24: "Обработка символьных строк",
    25: "Обработка целых чисел: маски и делители",
    26: "Сортировка и обработка данных",
    27: "Анализ данных: кластеры",
}


def load_task_data(number):
    """Читает data/tasks/<номер>.json целиком.
    Если файла ещё нет, возвращает пустой словарь."""
    path = TASKS_DIR / f"{number}.json"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def index():
    return render_template("index.html", titles=TASK_TITLES)


@app.route("/task/<int:number>")
def task(number):
    if number not in TASK_TITLES:
        abort(404)
    data = load_task_data(number)
    return render_template(
        "task.html",
        number=number,
        title=TASK_TITLES[number],
        formulation=data.get("formulation"),
        requirement=data.get("requirement"),
        types=data.get("types", []),
    )


if __name__ == "__main__":
    app.run(debug=True)

