from datetime import datetime
from time import sleep

import pytest
# 1) Использовать Python/Java, подключить библиотеку Selenium Webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import csv


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def test_select_product():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--windows-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    # 2) С помощью Selenium открыть браузер, открыть страницу

    base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login;"

    driver.get(base_url)
    sleep(1)

    # 3) Авторизоваться пользователем «Harry Potter»;
    button_customer_login_locator = '//button[@class="btn btn-primary btn-lg"]'
    button_customer_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, button_customer_login_locator)))
    button_customer_login.click()
    sleep(1)

    drop_down_your_name_locator = '//select[@id="userSelect"]'
    drop_down_your_name = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, drop_down_your_name_locator)))
    # drop_down_your_name.click()
    # sleep(1)
    # drop_down_your_name.send_keys(Keys.DOWN * 2)
    # sleep(1)

    drop_down_list = Select(drop_down_your_name)
    drop_down_list.select_by_value("2")
    drop_down_your_name.send_keys(Keys.ENTER)
    sleep(1)
    login_button_locator = '//button[@class="btn btn-default"]'
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, login_button_locator)))

    login_button.click()
    sleep(1)

    # 4) Вычислить N-е число Фибоначчи, где N - это текущий день месяца + 1.

    day_number = int(datetime.utcnow().strftime("%d")) + 1

    my_fibo = fibonacci(day_number)

    # 5) Выполнить пополнение счета (Deposit) на сумму равную вычисленному в п.4 числу;

    deposit_button_locator = '//button[@ng-click="deposit()"]'
    deposit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, deposit_button_locator)))
    deposit_button.click()
    sleep(1)

    amount_placeholder_locator = '//input[@placeholder="amount"]'
    amount_placeholder = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, amount_placeholder_locator)))
    amount_placeholder.send_keys(my_fibo)
    sleep(1)

    deposit_submit_locator = '//button[@type="submit"]'
    deposit_submit = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, deposit_submit_locator)))
    deposit_submit.click()
    sleep(1)

    # 6) Выполнить списание со счета (Withdrawl) на сумму равную вычисленному в п.4 числу;

    withdrawl_button_locator = '//button[@ng-click="withdrawl()"]'
    withdrawal_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, withdrawl_button_locator)))
    withdrawal_button.click()
    sleep(1)

    amount_placeholder_w_locator = '//input[@placeholder="amount"]'
    amount_placeholder_w = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, amount_placeholder_w_locator)))
    amount_placeholder_w.send_keys(my_fibo)
    sleep(1)

    withdrawl_submit_locator = '//button[text()="Withdraw"]'
    withdrawal_submit = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, withdrawl_submit_locator)))
    withdrawal_submit.click()
    sleep(1)

    balance_locator = '//strong[@class="ng-binding"][2]'
    balance = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, balance_locator))).text
    assert balance == '0'
    print(balance)

    # 8) Открыть страницу транзакций и проверить наличие обеих транзакций;

    transaction_button_locator = '//button[@ng-class="btnClass1"]'
    transaction_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_button_locator)))
    transaction_button.click()
    sleep(1)

    transaction_credit_value_locator = '//tr[@id="anchor0"]/child::td[2]'
    transaction_credit_value = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_credit_value_locator))).text
    assert transaction_credit_value == str(my_fibo)

    transaction_credit_text_locator = '//tr[@id="anchor0"]/child::td[3]'
    transaction_credit_text = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_credit_text_locator))).text
    print(transaction_credit_text)

    transaction_credit_date_locator = '//tr[@id="anchor0"]/child::td[1]'
    transaction_credit_date = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_credit_date_locator))).text
    print(transaction_credit_date)

    credit = f'{transaction_credit_date} {transaction_credit_value} {transaction_credit_text}'

    transaction_debit_locator = '//tr[@id="anchor1"]/child::td[2]'
    transaction_debit_value = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_debit_locator))).text
    assert transaction_debit_value == str(my_fibo)

    transaction_debit_date_locator = '//tr[@id="anchor1"]/child::td[1]'
    transaction_debit_date = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_debit_date_locator))).text
    print(transaction_debit_date)

    transaction_debit_text_locator = '//tr[@id="anchor1"]/child::td[3]'
    transaction_debit_text = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, transaction_debit_text_locator))).text
    print(transaction_debit_text)

    debit = f'{transaction_debit_date} {transaction_debit_value} {transaction_debit_text}'

    # 9) Сформировать файл формата csv, в который выгрузить данные о
    # проведенных транзакциях;
    # Файл должен содержать строки следующего формата
    # <Дата-времяТранзакции Сумма ТипТранзакции>, где
    # Формат Дата-времяТранзакции - "ДД Месяц ГГГГ ЧЧ:ММ:СС"
    # Формат Сумма - число
    # Формат ТипТранзакции - значение из списка [Credit, Debit]

    with open("transaction.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow([credit])
        writer.writerow([debit])
