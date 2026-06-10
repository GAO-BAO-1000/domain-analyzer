from api_client import get_domain_info
from data_processor import process_domain_info
from report import print_report


def main():
    domain_name = input("Введите доменное имя: ")

    # Получаем сырые данные WHOIS
    domain_info = get_domain_info(domain_name)

    # Обрабатываем данные
    processed_data = process_domain_info(domain_info)

    # Выводим отчёт
    print_report(processed_data)


if __name__ == "__main__":
    main()