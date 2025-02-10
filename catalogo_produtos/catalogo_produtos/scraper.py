from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def coletar_produtos():
    url = "https://www.mercadolivre.com.br"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"{url}/search?search_type=search&item_id=Computador%20Gamer%20i7%2016gb%20ssd%201tb")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.ui-search-layout__item")))
    produtos = []

    elementos = driver.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")

    for el in elementos:
        try:
            nome = el.find_element(By.CSS_SELECTOR, "h2").text
            imagem_url = el.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
            preco = el.find_element(By.CSS_SELECTOR, ".price-tag-fraction").text.replace('.', '')
            preco = float(preco.replace(',', '.'))
            link = el.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

            parcelamento = el.find_element(By.CSS_SELECTOR, ".ui-search-installments__text").text if el.find_elements(By.CSS_SELECTOR, ".ui-search-installments__text") else None
            frete_gratis = bool(el.find_elements(By.CSS_SELECTOR, ".ui-search-item__shipping--free"))

            produto = {
                "nome": nome,
                "imagem_url": imagem_url,
                "preco": preco,
                "parcelamento": parcelamento,
                "link": link,
                "tipo_entrega": "Normal",
                "frete_gratis": frete_gratis,
            }
            produtos.append(produto)
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")

    driver.quit()
    return produtos