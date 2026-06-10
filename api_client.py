import whois


def get_domain_info(domain_name):
    """
    Получает сырые WHOIS-данные по домену.

    Args:
        domain_name (str): Доменное имя (например, yandex.ru)

    Returns:
        dict: Сырые данные WHOIS
    """
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as error:
        print(f"Ошибка при получении данных для домена {domain_name}: {error}")
        return None