# Desafio Catálogo de Ofertas

Este é o projeto "Desafio Catálogo de Ofertas". Este README fornece instruções sobre como configurar e executar o projeto.

## Pré-requisitos

- UV (gerenciador de dependências)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/rafaelcaet/desafio-catalogo-ofertas.git
    cd desafio-catalogo-ofertas
    ```

2. Inicie o projeto com o UV:

    ```bash
        uv init
    ```

3. Instale as dependências usando UV:

    ```bash
        uv add <nome_da_dependencia>
    ```

## Executando o Projeto

Para iniciar o projeto, execute o seguinte comando:

```bash
uv run manage.py runserver
```

### Após rodar o projeto, é necessário acessar o endpoint '/produtos' para que seja executado o webscrapping e mostre o resultado da execucao

### Caso queira ver a lista, basta acessar o endpoint '/produtos/lista'

## Estrutura do Projeto

- `catalogo_produtos/`: Contém o código-fonte do projeto.
- `/catalogo_produtos`: Contém o webscrapper e as demais funcionalidades
