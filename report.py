import textwrap


def print_report(data):
    if not data:
        print("Нет данных для отображения.")
        return

    print("\n" + "=" * 60)
    print("ОТЧЁТ О ДОМЕНЕ".center(60))
    print("=" * 60)

    rows = [
        ("Домен", data.get("domain_name")),
        ("Владелец", data.get("owner")),
        ("Регистратор", data.get("registrar")),
        ("Дата регистрации", data.get("creation_date")),
        ("Дата окончания", data.get("expiration_date")),
        ("Дата обновления", data.get("updated_date")),
        ("Серверы имён", data.get("name_servers")),
        ("Статус", data.get("status")),
        ("Страна", data.get("country")),
    ]

    label_width = 18
    value_width = 40  # ширина правой колонки

    for key, value in rows:
        # если список (например name_servers)
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)

        if value is None:
            value = "—"

        wrapped_lines = textwrap.wrap(str(value), width=value_width)

        # первая строка
        print(f"{key:<{label_width}} | {wrapped_lines[0] if wrapped_lines else ''}")

        # остальные строки — с отступом вместо ключа
        for line in wrapped_lines[1:]:
            print(f"{'':<{label_width}} | {line}")

    print("=" * 60)


if __name__ == "__main__":
    test_data = {
        "domain_name": "test.com",
        "owner": "Test Inc",
        "registrar": "Test Registrar",
        "creation_date": "2020-01-01",
        "expiration_date": "2030-01-01",
        "updated_date": "2025-01-01",
        "name_servers": [
            "ns1.super-long-domain-name-example.com",
            "ns2.another-very-long-dns-server-name-test.net",
            "ns3.third-extremely-long-name-for-testing-purposes.org",
        ],
        "status": "active",
        "country": "US",
    }

    print_report(test_data)