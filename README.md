# 🤖 Fábrica de Conteúdo com Agentes de IA

Este é um aplicativo interativo desenvolvido em **Streamlit** que utiliza o ecossistema **CrewAI** e modelos **Google Gemini** para automatizar a pesquisa na web e a redação de publicações de alta performance voltadas para o LinkedIn.

O sistema orquestra uma equipe multiplataforma de Agentes de Inteligência Artificial para buscar tendências em tempo real na internet e transformar dados brutos em textos persuasivos e engajadores.

---

## 👥 A Equipe de Agentes

O projeto utiliza o conceito de execução sequencial do CrewAI com dois agentes especialistas:

1. **Pesquisador Sênior de Tecnologia:** Navega na internet utilizando a ferramenta de busca `SerperDevTool` para extrair e estruturar dados factuais, atualizações e notícias recentes sobre o tema escolhido.
2. **Redator Técnico e Especialista em Engajamento:** Recebe o relatório compilado, aplica técnicas de copywriting e formata o conteúdo sob medida para a rede social (incluindo emojis, quebras de linha e hashtags).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Streamlit:** Interface web do usuário de forma rápida e fluida.
* **CrewAI:** Orquestração e gerenciamento do ciclo de vida dos agentes autônomos.
* **Google Gemini API (via Wrapper nativo do CrewAI):** Modelos de linguagem `gemini-1.5-flash` ou `gemini-2.5-flash` para inferência de alta velocidade.
* **Serper API:** Componente de busca programática em tempo real no Google Search.

---

## 🚀 Como Configurar e Executar Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/Celsojr30/meu-projeto-agentes.git](https://github.com/Celsojr30/meu-projeto-agentes.git)
cd meu-projeto-agentes

2. Configurar o Ambiente Virtual (venv)
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# No Windows (Prompt de Comando):
.\venv\Scripts\activate.bat
# No Linux/Mac:
source venv/bin/activate

3. Instalar as Dependências
pip install -r requirements.txt

4. Configurar as Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto. Adicione suas credenciais do Google AI Studio e do Serper:
GEMINI_API_KEY=Sua_Chave_Privada_Do_Gemini
SERPER_API_KEY=Sua_Chave_Privada_Do_Serper

💻 Executando o Aplicativo
Com o ambiente ativo e as chaves devidamente configuradas, inicialize o servidor do Streamlit:
streamlit run app.py

O navegador abrirá automaticamente o painel de controle. Insira o tema tecnológico desejado, escolha a versão do Gemini na barra lateral e clique em Iniciar Pesquisa e Redação.

🔒 Segurança
As credenciais e tokens privados de acesso às APIs nunca devem ser enviados para repositórios públicos. O arquivo .gitignore deste projeto está pré-configurado para ignorar:

.env (Chaves de acesso locais)

venv/ (Módulos e interpretador local)

__pycache__/ (Arquivos compilados do Python)
