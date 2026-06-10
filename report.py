def print_report(data):
    """
    Выводит отчёт по домену в читаемом виде.

    Args:
        data (dict): Словарь с обработанными данными о домене.
    """
    if not data:
        print("Нет данных для отображения.")
        return

    print("\n=== ОТЧЁТ О ДОМЕНЕ ===")
    print(f"Домен: {data.get('domain_name')}")
    print(f"Владелец: {data.get('owner')}")
    print(f"Регистратор: {data.get('registrar')}")
    print(f"Дата регистрации: {data.get('creation_date')}")
    print(f"Дата окончания регистрации: {data.get('expiration_date')}")
    print(f"Дата обновления: {data.get('updated_date')}")
    print(f"Серверы имён: {data.get('name_servers')}")
    print(f"Статус: {data.get('status')}")
    print(f"Страна: {data.get('country')}")


