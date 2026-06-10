from api_client import get_domain_info


def normalize_value(value):
    """
    Если значение является списком, возвращает первый элемент.
    """
    if isinstance(value, list):
        return value[0] if value else None
    return value


def process_domain_info(domain_info):
    """
    Извлекает нужные данные из сырых WHOIS-данных.

    Args:
        domain_info (dict): Сырые WHOIS-данные.

    Returns:
        dict: Обработанные данные.
    """
    if not domain_info:
        return None

    processed_data = {
        "domain_name": normalize_value(domain_info.get("domain_name")),
        "owner": (
            normalize_value(domain_info.get("org"))
            or normalize_value(domain_info.get("registrant_name"))
            or normalize_value(domain_info.get("name"))
        ),
        "registrar": normalize_value(domain_info.get("registrar")),
        "creation_date": normalize_value(domain_info.get("creation_date")),
        "expiration_date": normalize_value(domain_info.get("expiration_date")),
        "updated_date": normalize_value(domain_info.get("updated_date")),
        "name_servers": domain_info.get("name_servers"),
        "status": normalize_value(domain_info.get("status")),
        "country": normalize_value(domain_info.get("country")),
    }

    return processed_data

