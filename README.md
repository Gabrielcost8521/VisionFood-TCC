# 🍽️ VisionFood

**VisionFood** é um projeto de acessibilidade que oferece um sistema de cardápio digital desenvolvido para auxiliar pessoas com deficiência visual na escolha de refeições em restaurantes, promovendo inclusão, autonomia e praticidade.

## 📱 Funcionalidades

- Tela de **cadastro** e **login** com validação.
- Página inicial com listagem de **restaurantes**.
- Redirecionamento para leitura de **QR Code**.
- Página de **cardápio visual** com pratos, descrições e preços.
- Navegação entre páginas fluida.
- Banco de dados com armazenamento de usuários via SQLite.

## 💡 Tecnologias Utilizadas

- **Frontend:**
  - HTML5
  - CSS3 (com layout inspirado no Figma)
  - JavaScript (validação de formulário)
- **Backend:**
  - Python 3 + Flask
- **Banco de Dados:**
  - SQLite3
- **Design de Interface:**
  - Criado no Figma e convertido para código.

## 📂 Estrutura de Diretórios

```bash
visionfood/
├── static/
│   ├── img/                        # Imagens utilizadas nas telas
│   ├── cadastro-style.css
│   ├── login-style.css
│   ├── restaurantes-style.css
│   ├── cameraqr-style.css
│   ├── cardapio-style.css
│   └── ...                         # Arquivos de estilo globais
├── templates/
│   ├── cadastro.html
│   ├── login.html
│   ├── restaurantes.html
│   ├── cameraqr.html
│   └── cardapio.html
├── visionfood.db                  # Banco de dados SQLite
├── app.py                         # Código principal do Flask
└── README.md                      # Documentação do projeto

▶️ Como Executar o Projeto
1 ° Clone o repositório ou baixe os arquivos.

2 °Instale o Flask:
bash
pip install flask

3° Execute o servidor:
bash
python app.py

4° Acesse no navegador:
http://localhost:5000

👤 Autores 
Gabriel Costa e Nicolas Castro

