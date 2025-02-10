from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrap_products():
    url = "https://lista.mercadolivre.com.br/computador-gamer-i7-16gb-ssd-1tb#D[A:Computador%20Gamer%20i7%2016gb%20ssd%201tb]"

    # Configuração do WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Para rodar sem abrir a janela (opcional)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        # Aceitar cookies
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Aceitar cookies']"))
        ).click()
    except Exception:
        print("Nenhum botão de cookies encontrado ou já aceito.")

    # Aguardar o carregamento dos produtos
    time.sleep(3)

    # Rolar a página para carregar mais itens
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    produtos = []
    elements = driver.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")

    for elem in elements:
        try:
            # Nome do produto
            nome_produto = elem.find_element(By.CSS_SELECTOR, "h2.ui-search-item__title").text

            # Imagem
            imagem_produto = elem.find_element(By.CSS_SELECTOR, "img.ui-search-result-image__element").get_attribute("src")

            # Preço
            preco_fraction = elem.find_element(By.CSS_SELECTOR, "span.andes-money-amount__fraction").text.replace('.', '')
            preco_cents = elem.find_element(By.CSS_SELECTOR, "span.andes-money-amount__cents").text if elem.find_elements(By.CSS_SELECTOR, "span.andes-money-amount__cents") else '00'
            preco_produto = float(f"{preco_fraction}.{preco_cents}")

            # Link
            link_produto = elem.find_element(By.CSS_SELECTOR, "a.ui-search-link").get_attribute("href")

            # Parcelamento
            opcao_parcelamento = elem.find_element(By.CSS_SELECTOR, "div.ui-search-installments").text if elem.find_elements(By.CSS_SELECTOR, "div.ui-search-installments") else None

            # Frete Grátis
            frete_gratis = bool(elem.find_elements(By.CSS_SELECTOR, "span.ui-search-item__shipping--free"))

            produto = {
                "nome_produto": nome_produto,
                "imagem_produto": imagem_produto,
                "preco_produto": preco_produto,
                "opcao_parcelamento": opcao_parcelamento,
                "link_produto": link_produto,
                "tipo_entrega": "Normal",
                "frete_gratis": frete_gratis,
            }
            produtos.append(produto)
            print("Produto encontrado:", produto)

        except Exception as e:
            print(f"Erro ao extrair produto: {e}")

    driver.quit()
    return produtos

if __name__ == "__main__":
    produtos = scrap_products()
    print(f"{len(produtos)} produtos encontrados!")
