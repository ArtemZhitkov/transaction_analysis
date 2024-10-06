from unittest.mock import patch

import pandas as pd
import pytest


@pytest.fixture
def sample_excel_file():
    return "test_data.xlsx"


@pytest.fixture
def mock_logger():
    with patch('src.utils.logger') as mock_logger:
        yield mock_logger


@pytest.fixture
def test_df() -> pd.DataFrame:
    transactions = [
        {"Номер карты": "1234", "Сумма операции": "-100.0", "Кэшбэк": "1.0", "Категория": "Продукты"},
        {"Номер карты": "1234", "Сумма операции": "-200.0", "Кэшбэк": "2.0", "Категория": "Продукты"},
        {"Номер карты": "5678", "Сумма операции": "-50.0", "Кэшбэк": "0.5", "Категория": "Продукты"},
    ]
    return pd.DataFrame(transactions)


@pytest.fixture
def test_df_nan() -> pd.DataFrame:
    transactions = [
        {"Номер карты": "1234", "Сумма операции": "-100.0", "Кэшбэк": "1.0", "Категория": "Продукты"},
        {"Номер карты": "nan", "Сумма операции": "-200.0", "Кэшбэк": "2.0", "Категория": "Продукты"},
        {"Номер карты": "5678", "Сумма операции": "-50.0", "Кэшбэк": "0.5", "Категория": "Продукты"},
    ]
    return pd.DataFrame(transactions)


@pytest.fixture
def test_df_not_cashback() -> pd.DataFrame:
    transactions = [
        {"Номер карты": "1234", "Сумма операции": "-100.0", "Категория": "Продукты"},
        {"Номер карты": "5678", "Сумма операции": "-50.0", "Категория": "Продукты"},
    ]
    return pd.DataFrame(transactions)


@pytest.fixture
def test_empty_df() -> pd.DataFrame:
    transactions = [{}]
    return pd.DataFrame(transactions)


@pytest.fixture
def test_df_top_5() -> pd.DataFrame:
    transactions = [
        {
            "Дата операции": "20.06.2023 12:00:00",
            "Сумма платежа": -100.0,
            "Категория": "Еда",
            "Описание": "Покупка еды",
        },
        {
            "Дата операции": "21.06.2023 12:00:00",
            "Сумма платежа": -200.0,
            "Категория": "Транспорт",
            "Описание": "Оплата проезда",
        },
        {
            "Дата операции": "22.06.2023 12:00:00",
            "Сумма платежа": -50.0,
            "Категория": "Развлечения",
            "Описание": "Кино",
        },
        {
            "Дата операции": "23.06.2023 12:00:00",
            "Сумма платежа": -300.0,
            "Категория": "Магазины",
            "Описание": "Покупка одежды",
        },
        {
            "Дата операции": "24.06.2023 12:00:00",
            "Сумма платежа": -20.0,
            "Категория": "Кофе",
            "Описание": "Кофе на вынос",
        },
        {
            "Дата операции": "25.06.2023 12:00:00",
            "Сумма платежа": -400.0,
            "Категория": "Магазины",
            "Описание": "Покупка техники",
        },
    ]
    return pd.DataFrame(transactions)
