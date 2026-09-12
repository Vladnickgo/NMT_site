# -*- coding: utf-8 -*-
"""
Генератор HTML-файлов для сайта Optima.
Запуск:  python generate.py
"""

import os
from pathlib import Path

# ============================================================
# СПИСОК УРОКОВ
# Формат: (раздел, тема)
# Порядок сохраняется — от него зависит нумерация и навигация.
# ============================================================

SECTIONS = {
    "combined": {
        "title": "🎯 Комбіновані тести НМТ",
        "lessons": [
            "Вхідне діагностування",
            "Робота над комплексним завданням",
            "Робота з комплексним завданням",
            "Робота з комплексним завданням. Рівняння, системи рівнянь",
            "Робота з комплексним завданням. Дії зі степенями",
            "Робота з комплексним завданням. Розв'язування нерівностей",
            "Робота з комплексним завданням. Логарифми",
            "Робота з комплексним завданням. Функції",
            "Робота з комплексним завданням. Властивості функцій",
            "Робота з комплексним завданням. Прогресії",
            "Робота з комплексним завданням. Проміжне тестування. Геометричні задачі",
            "Робота з комплексним завданням. Геометричні задачі",
            "Робота з комплексним завданням. Стереометричні задачі",
        ],
    },
    "algebra": {
        "title": "📘 Алгебра",
        "lessons": [
            "Множини чисел та дії з ними. Числові та буквені вирази. Формули скороченого множення",
            "Відсотки. Пропорція",
            "Лінійні рівняння та рівняння, що зводяться до лінійних",
            "Лінійні, квадратні, дробово-раціональні рівняння; рівняння з модулем",
            "Дробово-раціональні вирази та дії з ними",
            "Показникові рівняння",
            "Нерівності та їх системи: лінійні, квадратичні, дробово-раціональні",
            "Логарифм числа. Перетворення виразів. Логарифмічні рівняння та нерівності",
            "Системи рівнянь. Лінійні, квадратні, дробово-раціональні рівняння; рівняння з модулем",
            "Степеневі вирази. Перетворення цілих виразів",
            "Арифметичний квадратний корінь. Вирази з коренями",
            "Квадратні рівняння (повні/неповні). Теорема Вієта. Розкладання квадратного тричлена на множники",
            "Рівняння, що зводяться до квадратних. Біквадратні рівняння",
            "Степінь з натуральним, цілим та раціональним показником",
            "Функції: поняття, види, графіки, властивості. Геометричні перетворення графіків",
            "Арифметична та геометрична прогресії",
            "Комбінаторика. Теорія ймовірності. Елементи статистики",
            "Тригонометрія. Одиничне коло. Тотожності. Формули зведення. Рівняння",
            "Похідна. Первісна. Типові задачі",
            "Завдання з параметром",
        ],
    },
    "geometry": {
        "title": "📐 Геометрія",
        "lessons": [
            "Основні фігури площини та їхні властивості: відрізки, кути. Коло, круг: елементи та основні властивості",
            "Трикутники. Види. Рівність та подібність трикутників. Кола трикутників",
            "Прямокутний трикутник та його розв'язування",
            "Чотирикутники. Види та властивості. Паралелограми. Площа",
            "Трапеція: види та властивості. Площа",
            "Вписані та центральні кути. Круг та його частини. Вписані та описані трикутники/чотирикутники. Правильні многокутники та кола",
            "Тригонометрія тупих кутів. Розв'язування довільних трикутників. Площа",
            "Координати та вектори на площині і в просторі",
            "Стереометрія. Розташування фігур в просторі",
            "Призма. Піраміда",
            "Циліндр. Конус",
            "Сфера. Куля",
        ],
    },
}

# ============================================================
# ШАБЛОН УРОКА
# ============================================================

LESSON_TEMPLATE = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Урок {num:02d}: {title} — Optima</title>
    <link rel="stylesheet" href="../style.css">
    <script>
        MathJax = {{
            tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }},
            svg: {{ fontCache: 'global' }}
        }};
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
</head>
<body>
    <header class="site-header">
        <div class="container">
            <a href="../index.html" class="logo">📐 Optima</a>
            <p class="tagline">Підготовка до НМТ з математики</p>
        </div>
    </header>

    <main class="container lesson-page">
        <div class="lesson-header">
            <p class="breadcrumb">
                <a href="../index.html">Головна</a> ›
                <a href="../index.html#{section_id}">{section_title}</a> ›
                Урок {num:02d}
            </p>
            <h1>{title}</h1>
        </div>

        <article class="lesson-content">

            <h2>Мета заняття</h2>
            <p><em>Тут буде мета уроку.</em></p>

            <h2>Теоретична довідка</h2>
            <p><em>Тут буде теорія. Формули записуються в LaTeX між знаками $ ... $.</em></p>
            <p>Наприклад: $a^2 + b^2 = c^2$</p>

            <div class="example">
                <div class="example-title">Приклад 1</div>
                <p><em>Умова прикладу.</em></p>
                <p><strong>Розв'язання:</strong></p>
                <p><em>Покрокове розв'язання.</em></p>
                <p><strong>Відповідь:</strong> ...</p>
            </div>

            <!-- ===== ТЕСТ ===== -->
            <div class="test">
                <div class="test-title">📝 Перевірте себе</div>

                <!-- Питання 1: вибір варіанта -->
                <div class="question">
                    <p class="question-text">1. Текст питання?</p>
                    <div class="options">
                        <button class="option" data-correct="false" onclick="checkChoice(this, false)">Варіант A</button>
                        <button class="option" data-correct="true"  onclick="checkChoice(this, true)">Варіант B (правильний)</button>
                        <button class="option" data-correct="false" onclick="checkChoice(this, false)">Варіант C</button>
                        <button class="option" data-correct="false" onclick="checkChoice(this, false)">Варіант D</button>
                    </div>
                    <p class="feedback"></p>
                </div>

                <!-- Питання 2: введення відповіді -->
                <div class="question">
                    <p class="question-text">2. Текст питання? У відповідь запишіть число.</p>
                    <div class="input-answer">
                        <input type="text" placeholder="Ваша відповідь">
                        <button class="btn" onclick="checkInput(this, '0')">Перевірити</button>
                    </div>
                    <p class="feedback"></p>
                </div>

                <!-- Питання 3: введення + показати розв'язок -->
                <div class="question">
                    <p class="question-text">3. Текст питання?</p>
                    <div class="input-answer">
                        <input type="text" placeholder="Ваша відповідь">
                        <button class="btn" onclick="checkInput(this, '0')">Перевірити</button>
                        <button class="btn secondary" onclick="toggleSolution(this)">👁 Показати розв'язок</button>
                    </div>
                    <p class="feedback"></p>
                    <div class="solution">
                        <div class="solution-title">Розв'язання:</div>
                        <p><em>Тут буде розв'язання.</em></p>
                    </div>
                </div>

            </div>
        </article>

        <nav class="lesson-nav">
            {nav_prev}
            {nav_next}
        </nav>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>© Optima — підготовка до НМТ</p>
        </div>
    </footer>

    <script src="../script.js"></script>
</body>
</html>
"""

# ============================================================
# ШАБЛОН ГЛАВНОЙ СТРАНИЦЫ
# ============================================================

INDEX_HEADER = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Optima — підготовка до НМТ з математики</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <a href="index.html" class="logo">📐 Optima</a>
            <p class="tagline">Підготовка до НМТ з математики</p>
        </div>
    </header>

    <main class="container">
        <section class="intro">
            <h1>Курс математики для підготовки до НМТ</h1>
            <p>Повний курс: комбіновані тести, алгебра, геометрія. Теорія, приклади, тести.</p>
        </section>
"""

INDEX_FOOTER = """    </main>

    <footer class="site-footer">
        <div class="container">
            <p>© Optima — підготовка до НМТ</p>
        </div>
    </footer>
</body>
</html>
"""

# ============================================================
# ЛОГИКА ГЕНЕРАЦИИ
# ============================================================

def slugify_section(section_id):
    """ID раздела для якоря на главной."""
    return section_id


def build_flat_list():
    """Возвращает плоский список всех уроков:
    [(section_id, section_title, index_in_section, global_index, title), ...]
    """
    flat = []
    for section_id, data in SECTIONS.items():
        for i, title in enumerate(data["lessons"], start=1):
            flat.append({
                "section_id": section_id,
                "section_title": data["title"],
                "num": i,
                "title": title,
            })
    return flat


def make_nav(flat, idx):
    """Строит HTML для кнопок 'Попередній' / 'Наступний'."""
    prev_html = '<span class="disabled">← Попередній</span>'
    next_html = '<span class="disabled">Наступний →</span>'

    if idx > 0:
        p = flat[idx - 1]
        prev_html = f'<a href="{p["section_id"]}-{p["num"]:02d}.html">← {p["title"][:40]}</a>'

    if idx < len(flat) - 1:
        n = flat[idx + 1]
        next_html = f'<a href="{n["section_id"]}-{n["num"]:02d}.html">{n["title"][:40]} →</a>'

    return prev_html, next_html


def generate_lessons():
    flat = build_flat_list()
    lessons_dir = Path("lessons")
    lessons_dir.mkdir(exist_ok=True)

    created = 0
    skipped = 0

    for idx, lesson in enumerate(flat):
        filename = f'{lesson["section_id"]}-{lesson["num"]:02d}.html'
        filepath = lessons_dir / filename

        if filepath.exists():
            skipped += 1
            continue

        nav_prev, nav_next = make_nav(flat, idx)
        html = LESSON_TEMPLATE.format(
            num=lesson["num"],
            title=lesson["title"],
            section_id=lesson["section_id"],
            section_title=lesson["section_title"],
            nav_prev=nav_prev,
            nav_next=nav_next,
        )
        filepath.write_text(html, encoding="utf-8")
        created += 1

    return created, skipped, flat


def generate_index(flat):
    """Генерирует index.html со всеми карточками."""
    index_path = Path("index.html")
    if index_path.exists():
        print("⚠️  index.html уже существует — пропускаю.")
        print("   (Если хотите перегенерировать — удалите его вручную.)")
        return False

    parts = [INDEX_HEADER]

    for section_id, data in SECTIONS.items():
        parts.append(f'        <section class="section" id="{section_id}">')
        parts.append(f'            <h2>{data["title"]}</h2>')
        parts.append('            <div class="lessons-grid">')

        for i, title in enumerate(data["lessons"], start=1):
            parts.append(
                f'                <a href="lessons/{section_id}-{i:02d}.html" class="lesson-card">'
            )
            parts.append(f'                    <span class="lesson-num">{i:02d}</span>')
            parts.append(f'                    <span class="lesson-title">{title}</span>')
            parts.append('                </a>')

        parts.append('            </div>')
        parts.append('        </section>')
        parts.append('')

    parts.append(INDEX_FOOTER)
    index_path.write_text("\n".join(parts), encoding="utf-8")
    return True


def main():
    print("=" * 60)
    print("  Генератор сайту Optima")
    print("=" * 60)

    created, skipped, flat = generate_lessons()
    print(f"\n📄 Уроки:")
    print(f"   Створено:      {created}")
    print(f"   Пропущено:     {skipped} (файли вже існують)")
    print(f"   Всього уроків: {len(flat)}")

    index_ok = generate_index(flat)
    if index_ok:
        print("\n🏠 index.html — створено")
    else:
        print("\n🏠 index.html — пропущено")

    print("\n✅ Готово! Відкрийте index.html у браузері.")


if __name__ == "__main__":
    main()