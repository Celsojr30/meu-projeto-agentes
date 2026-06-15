import os
import streamlit as st
from dotenv import load_dotenv
from crewai import LLM, Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da página do Streamlit
st.set_page_config(page_title="Agentes de Conteúdo IA", page_icon="🤖", layout="wide")

st.title("🤖 Fábrica de Conteúdo com Agentes de IA")
st.markdown("Insira um tema de tecnologia para que nossa equipe de agentes pesquise na internet em tempo real e crie um post otimizado para o LinkedIn.")

# Sidebar para configurações básicas
st.sidebar.header("Configurações")
modelo_selecionado = st.sidebar.selectbox("Modelo LLM", ["gemini/gemini-1.5-flash", "gemini/gemini-2.5-flash"])

# Campo de entrada para o usuário definir o tema
tema_usuario = st.text_input(
    "Qual o tema do post?", 
    placeholder="Ex: Novidades do ecossistema de automação RPA e IA este ano"
)

# Botão para iniciar o processo
if st.button("🚀 Iniciar Pesquisa e Redação"):
    if not tema_usuario:
        st.warning("Por favor, digite um tema antes de iniciar.")
    else:
        # Criando containers de status na tela para o usuário acompanhar o progresso
        with st.status("🤖 Agentes trabalhando no seu post... (Isso pode levar um minutinho)", expanded=True) as status:
            
            try:
                # 1. Inicializar LLM e Ferramentas
                gemini_llm = LLM(
                    #model="gemini/gemini-2.5-flash",    # Prefixo oficial para o provedor interno
                    model=modelo_selecionado,    # Prefixo oficial para o provedor interno
                    api_key=os.getenv("GEMINI_API_KEY"), # Passa a chave explicitamente para evitar falhas
                    temperature=0.5
                )

                ferramenta_busca = SerperDevTool()

                st.write("🕵️‍♂️ Agente Pesquisador está navegando na web...")
                
                # 2. Configurar Agentes
                pesquisador = Agent(
                    role="Pesquisador Sênior de Tecnologia",
                    goal="Buscar na internet e sintetizar as notícias e tendências mais recentes sobre o tema fornecido.",
                    backstory="Analista de inteligência de mercado focado em dados factuais e novidades quentes.",
                    tools=[ferramenta_busca],
                    verbose=True,
                    llm=gemini_llm
                )

                escritor = Agent(
                    role="Redator Técnico e Especialista em Engajamento",
                    goal="Transformar relatórios de pesquisas em tempo real em posts atraentes para o LinkedIn.",
                    backstory="Copywriter renomado que transforma dados brutos em textos altamente engajadores e bem formatados.",
                    verbose=True,
                    llm=gemini_llm
                )

                # 3. Configurar Tarefas
                tarefa_pesquisa = Task(
                    description=f"Utilize a ferramenta de busca para encontrar as notícias ou lançamentos mais recentes sobre o tema: '{tema_usuario}'.",
                    expected_output="Um relatório em tópicos com as principais novidades encontradas.",
                    agent=pesquisador
                )

                tarefa_escrita = Task(
                    description="Com base no relatório do pesquisador, crie um post formatado para o LinkedIn.",
                    expected_output="Um post de LinkedIn completo, com emojis, ganchos atraentes e hashtags.",
                    agent=escritor
                )

                # 4. Executar o Crew
                st.write("✍️ Agente Escritor está redigindo o post final...")
                equipe = Crew(
                    agents=[pesquisador, escritor],
                    tasks=[tarefa_pesquisa, tarefa_escrita],
                    process=Process.sequential
                )
                
                # Executa o processo e captura o resultado
                resultado_final = equipe.kickoff()
                
                # Atualiza o status para sucesso
                status.update(label="✅ Processo concluído com sucesso!", state="complete", expanded=False)

                # 5. Exibir o resultado final na tela de forma elegante
                st.success("✨ Seu post está pronto!")
                
                # Criando uma caixa de texto formatada para exibição
                st.markdown("### 📝 Resultado Final (Pronto para copiar):")
                st.text_area(label="", value=str(resultado_final), height=400)
                
            except Exception as e:
                status.update(label="❌ Ocorreu um erro no processo.", state="error")
                st.error(f"Erro: {e}")