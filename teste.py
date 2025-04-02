import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard LBV - Doações & Análises", layout="wide", page_icon="💖")

st.image("logo.png", width=100)

st.title("Dashboard de Doações e Análises – Legião da Boa Vontade (LBV)")
st.markdown("""
Esta aplicação interativa exibe os dados consolidados de 6 doações, com informações e análises detalhadas realizadas pela IA.  
Você pode escolher entre:
- **Global:** Visualizar as estatísticas consolidadas, métricas e gráficos de todas as doações.
- **Por ID:** Selecionar um ID de doação para ver todos os detalhes e a análise realizada para aquele registro.
""")

doacoes_data = [
    {
        "IdGravacao": 722740890,
        "NomeProfissional": "Kauana Braga Felix",
        "DataDoacao": "2024-12-10",
        "NomeDoador": "CLAUDETE APARECIDA DE FATIMA OLYMPIO",
        "DataNascimento": "1971-03-17",
        "DocumentoFiscalDoador": None,
        "Endereco": "RUA ARLEI DE SOUZA, 1096",
        "Bairro": "PARQUE RESIDENCIAL DA FRATERNIDADE",
        "Cidade": "SAO JOSE DO RIO PRETO",
        "Estado": "São Paulo",
        "IdDebitoDoacao": "4001739554",
        "CategoriaDoacao": "Doação",
        "NomeTitular": "CLAUDETE APARECIDA DE FATIMA OLYMPIO",
        "TipoRecebimento": "Elétrica",
        "ValorDoacao": 30.00,
        "EmpresaRecebimento": "Energisa - Mato G. do Sul"
    },
    {
        "IdGravacao": 722748725,
        "NomeProfissional": "Beatriz Isabela de Carvalho",
        "DataDoacao": "2024-12-10",
        "NomeDoador": "TEREZA GARCIA RIZATTO",
        "DataNascimento": "1938-12-06",
        "DocumentoFiscalDoador": None,
        "Endereco": "RUA JOSE GARCIA FERNANDES, 140",
        "Bairro": "JARDIM MARIA LUIZA",
        "Cidade": "JAU",
        "Estado": "São Paulo",
        "IdDebitoDoacao": "1436216440",
        "CategoriaDoacao": "Novo Cooperador",
        "NomeTitular": "",  # Campo em branco (idealmente deveria ser preenchido)
        "TipoRecebimento": "Telefone",
        "ValorDoacao": 10.00,
        "EmpresaRecebimento": "Vivo Fixo"
    },
    {
        "IdGravacao": 722787952,
        "NomeProfissional": "Mayara Costa da Silva",
        "DataDoacao": "2024-12-10",
        "NomeDoador": "DERCI MARQUES DA SILVA",
        "DataNascimento": "1974-10-05",
        "DocumentoFiscalDoador": None,
        "Endereco": "ENDERECO NAO INFORMADO, 0",
        "Bairro": None,
        "Cidade": "CUIABA",
        "Estado": "Mato Grosso",
        "IdDebitoDoacao": "65993283435",
        "CategoriaDoacao": "Doação",
        "NomeTitular": "",  # Deveria ser preenchido com o nome do doador
        "TipoRecebimento": "Telefone",
        "ValorDoacao": 10.00,
        "EmpresaRecebimento": "Claro Móvel"
    },
    {
        "IdGravacao": 722788258,
        "NomeProfissional": "Juliani Pereira de Souza",
        "DataDoacao": "2024-12-10",
        "NomeDoador": "DANILO SOUZA LIMA",
        "DataNascimento": "1986-04-13",
        "DocumentoFiscalDoador": None,
        "Endereco": "RUA JOAO VINTE E TRES, 16 LT 6",
        "Bairro": "CENTRO",
        "Cidade": "BONITO",
        "Estado": "Mato Grosso do Sul",
        "IdDebitoDoacao": "32665515",
        "CategoriaDoacao": "Doação",
        "NomeTitular": "DANILO SOUZA LIMA",
        "TipoRecebimento": "Elétrica",
        "ValorDoacao": 50.00,
        "EmpresaRecebimento": "Energisa - Mato G. do Sul"
    },
    {
        "IdGravacao": 722788328,
        "NomeProfissional": "Gisele Cristina Brasil de Jesus",
        "DataDoacao": "2024-12-10",
        "NomeDoador": "MARIA DO SOCORRO DENIZ COSTA",
        "DataNascimento": "1944-01-15",
        "DocumentoFiscalDoador": None,
        "Endereco": "RUA ENDERECO NAO INFORMADO, 0",
        "Bairro": None,
        "Cidade": "RIO DE JANEIRO",
        "Estado": "Rio de Janeiro",
        "IdDebitoDoacao": "21979809333",
        "CategoriaDoacao": "Doação",
        "NomeTitular": "",  # Ideal: preencher com o nome da doadora
        "TipoRecebimento": "Telefone",
        "ValorDoacao": 15.00,
        "EmpresaRecebimento": "Claro Móvel"
    },
    {
        "IdGravacao": 722750343,
        "NomeProfissional": "Bruna Rosa da Silva",
        "DataDoacao": "2024-12-10",
        "NomeDoador": "GILVANIA VIEIRA DE OLIVEIRA",
        "DataNascimento": "1976-03-11",
        "DocumentoFiscalDoador": None,
        "Endereco": "RUA A, 0",
        "Bairro": "CAICARA",
        "Cidade": "PRAIA GRANDE",
        "Estado": "São Paulo",
        "IdDebitoDoacao": "13981313046",
        "CategoriaDoacao": "Doação",
        "NomeTitular": "GILVANIA VIEIRA DE OLIVEIRA",
        "TipoRecebimento": "Telefone",
        "ValorDoacao": 50.00,
        "EmpresaRecebimento": "Claro Móvel"
    }
]

df = pd.DataFrame(doacoes_data)
df["DataDoacao"] = pd.to_datetime(df["DataDoacao"])
df["DataNascimento"] = pd.to_datetime(df["DataNascimento"])

analysis_data = [
    {
        "IdGravacao": 722740890,
        "Campos": [
            {"Campo": "IdGravacao", "Analise": "Corresponde ao arquivo/transcrição.", "Conclusao": "Correto"},
            {"Campo": "NomeProfissional", "Analise": "Na transcrição, a atendente não deixou claro seu nome; o JSON traz ‘Kauana Braga Felix’.", "Conclusao": "Sem divergência aparente."},
            {"Campo": "DataDoacao", "Analise": "O áudio menciona: ‘Hoje é dia dez do doze de dois mil e vinte e quatro’.", "Conclusao": "Correto"},
            {"Campo": "NomeDoador", "Analise": "O doador no canal 1 soa como ‘Laalbete’ versus ‘Claudete’.", "Conclusao": "Coerente; o JSON registra o nome correto."},
            {"Campo": "DataNascimento", "Analise": "A transcrição não menciona a data; o JSON a lista.", "Conclusao": "Sem contradição."},
            {"Campo": "DocumentoFiscalDoador", "Analise": "CPF pedido mas não registrado.", "Conclusao": "Aceitável – campo null."},
            {"Campo": "Endereco", "Analise": "Áudio não cita endereço, mas o JSON vem com ‘RUA ARLEI DE SOUZA, 1096’.", "Conclusao": "Coerente."},
            {"Campo": "Bairro", "Analise": "Não mencionado no áudio, mas presente no JSON.", "Conclusao": "Sem divergência."},
            {"Campo": "Cidade", "Analise": "Áudio não menciona cidade; JSON registra ‘SAO JOSE DO RIO PRETO’.", "Conclusao": "Correto."},
            {"Campo": "Estado", "Analise": "Áudio não menciona, mas JSON consta.", "Conclusao": "Correto."},
            {"Campo": "DocumentoFiscalDoacao", "Analise": "Sem divergência.", "Conclusao": "Ok."},
            {"Campo": "IdDebitoDoacao", "Analise": "Áudio cita o código da conta de energia (‘40 0173-9554’).", "Conclusao": "Correto."},
            {"Campo": "CategoriaDoacao", "Analise": "É doação em conta de energia.", "Conclusao": "Correto."},
            {"Campo": "NomeTitular", "Analise": "Áudio confirma titularidade.", "Conclusao": "Correto."},
            {"Campo": "TipoRecebimento", "Analise": "Conta de energia (CPFL).", "Conclusao": "Correto."},
            {"Campo": "ValorDoacao", "Analise": "Confirma doação extra de 30 reais.", "Conclusao": "Correto."},
            {"Campo": "EmpresaRecebimento", "Analise": "Áudio diz ‘Energisa’ etc.", "Conclusao": "Correto."}
        ],
        "Observacao": "O nome da doadora no canal 1 soa como ‘Laalbete’ mas o sistema registra oficialmente ‘CLAUDETE APARECIDA DE FATIMA OLYMPIO’."
    },
    {
        "IdGravacao": 722748725,
        "Campos": [
            {"Campo": "IdGravacao", "Analise": "Presente no nome do arquivo.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeProfissional", "Analise": "Não foi verbalizado na transcrição; JSON tem ‘Beatriz Isabela de Carvalho’.", "Conclusao": "⚠️ Não verificável."},
            {"Campo": "DataDoacao", "Analise": "‘Hoje é dia 10/12/2024’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeDoador", "Analise": "‘TEREZA GARCIA RIZATTO’ – mencionado.", "Conclusao": "✅ Correto."},
            {"Campo": "DataNascimento", "Analise": "‘6/12/38’ citado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoador", "Analise": "CPF mencionado, mas sem número.", "Conclusao": "✅ Correto."},
            {"Campo": "Endereco", "Analise": "‘RUA JOSE GARCIA FERNANDES, 140’ citado.", "Conclusao": "✅ Correto."},
            {"Campo": "Bairro", "Analise": "‘JARDIM MARIA LUIZA’ citado.", "Conclusao": "✅ Correto."},
            {"Campo": "Cidade", "Analise": "‘JAU’ mencionado.", "Conclusao": "✅ Correto."},
            {"Campo": "Estado", "Analise": "Inferido via contexto.", "Conclusao": "⚠️ Presumivelmente correto."},
            {"Campo": "DocumentoFiscalDoacao", "Analise": "Sem documento fiscal.", "Conclusao": "✅ Correto."},
            {"Campo": "IdDebitoDoacao", "Analise": "‘1436216440’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "CategoriaDoacao", "Analise": "‘Novo Cooperador’ não mencionado na fala.", "Conclusao": "⚠️ Não verificável."},
            {"Campo": "NomeTitular", "Analise": "Campo ficou em branco, mesmo confirmando titularidade.", "Conclusao": "❌ Incorreto."},
            {"Campo": "TipoRecebimento", "Analise": "‘Telefone’ – confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "ValorDoacao", "Analise": "10 BRL confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "EmpresaRecebimento", "Analise": "‘Vivo Fixo’ confirmado.", "Conclusao": "✅ Correto."}
        ],
        "Observacao": "A maioria dos campos está correta. Atenção especial ao NomeTitular, que ficou em branco."
    },
    {
        "IdGravacao": 722787952,
        "Campos": [
            {"Campo": "IdGravacao", "Analise": "Número consta na URL/arquivo.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeProfissional", "Analise": "‘Mayara Costa da Silva’ – identificada como ‘Mayara Costa’.", "Conclusao": "✅ Correto."},
            {"Campo": "DataDoacao", "Analise": "Data ‘10/12/2024’ confirmada.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeDoador", "Analise": "‘DERCI MARQUES DA SILVA’ – pronunciado como ‘Desci’ ou ‘Derci’.", "Conclusao": "✅ Correto."},
            {"Campo": "DataNascimento", "Analise": "‘5/10/74’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoador", "Analise": "CPF aparece parcialmente sem número.", "Conclusao": "✅ Correto."},
            {"Campo": "Endereco", "Analise": "‘ENDERECO NAO INFORMADO, 0’ – conforme citado.", "Conclusao": "✅ Correto."},
            {"Campo": "Bairro", "Analise": "Ficou em branco.", "Conclusao": "✅ Correto."},
            {"Campo": "Cidade", "Analise": "‘CUIABA’ mencionado.", "Conclusao": "✅ Correto."},
            {"Campo": "Estado", "Analise": "‘Mato Grosso’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoacao", "Analise": "Sem documento fiscal.", "Conclusao": "✅ Correto."},
            {"Campo": "IdDebitoDoacao", "Analise": "‘65993283435’ formado com DDD ‘65’.", "Conclusao": "✅ Correto."},
            {"Campo": "CategoriaDoacao", "Analise": "É uma doação.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeTitular", "Analise": "Ficou vazio, mas o doador confirma ser titular.", "Conclusao": "Incompleto – deveria conter o nome do doador."},
            {"Campo": "TipoRecebimento", "Analise": "‘Telefone’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "ValorDoacao", "Analise": "10 BRL confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "EmpresaRecebimento", "Analise": "‘Claro Móvel’ mencionado.", "Conclusao": "✅ Correto."}
        ],
        "Observacao": "O campo NomeTitular está vazio. Ideal preencher com o nome do doador."
    },
    {
        "IdGravacao": 722788258,
        "Campos": [
            {"Campo": "IdGravacao", "Analise": "Número consta na URL/arquivo.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeProfissional", "Analise": "‘Juliani Pereira de Souza’ – o áudio apresenta ‘Juliane’; diferença mínima.", "Conclusao": "✅ Correto."},
            {"Campo": "DataDoacao", "Analise": "Data ‘10/12/2024’ confirmada.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeDoador", "Analise": "‘DANILO SOUZA LIMA’ – confirmado (com acréscimo de ‘Souza’).", "Conclusao": "✅ Correto."},
            {"Campo": "DataNascimento", "Analise": "‘13/04/1986’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoador", "Analise": "CPF mencionado parcialmente; campo null.", "Conclusao": "✅ Correto."},
            {"Campo": "Endereco", "Analise": "‘RUA JOAO VINTE E TRES, 16 LT 6’ citado.", "Conclusao": "✅ Correto."},
            {"Campo": "Bairro", "Analise": "‘CENTRO’ – confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "Cidade", "Analise": "‘BONITO’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "Estado", "Analise": "‘Mato Grosso do Sul’ mencionado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoacao", "Analise": "Sem documento fiscal.", "Conclusao": "✅ Correto."},
            {"Campo": "IdDebitoDoacao", "Analise": "‘32665515’ – derivado de ‘10/3266 555-5’.", "Conclusao": "Coerente."},
            {"Campo": "CategoriaDoacao", "Analise": "É uma doação.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeTitular", "Analise": "O doador confirma ser titular; JSON registra o mesmo.", "Conclusao": "✅ Correto."},
            {"Campo": "TipoRecebimento", "Analise": "‘Elétrica’ – a conta é de energia.", "Conclusao": "✅ Correto."},
            {"Campo": "ValorDoacao", "Analise": "50 BRL – a doação extra.", "Conclusao": "✅ Correto."},
            {"Campo": "EmpresaRecebimento", "Analise": "‘Energisa - Mato G. do Sul’ confirmado.", "Conclusao": "✅ Correto."}
        ],
        "Observacao": "Embora o total da conta seja 95, este registro refere-se apenas ao valor extra de 50, conforme o fluxo interno."
    },
    {
        "IdGravacao": 722788328,
        "Campos": [
            {"Campo": "IdGravacao", "Analise": "Número consta no arquivo.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeProfissional", "Analise": "‘Gisele Cristina Brasil de Jesus’ – a atendente se apresenta como ‘Gisele Brasil’.", "Conclusao": "✅ Correto."},
            {"Campo": "DataDoacao", "Analise": "Data ‘10/12/2024’ confirmada.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeDoador", "Analise": "‘MARIA DO SOCORRO DENIZ COSTA’ – o áudio apresenta variação, mas o JSON usa ‘DENIZ’.", "Conclusao": "✅ Correto."},
            {"Campo": "DataNascimento", "Analise": "‘15/01/1944’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoador", "Analise": "CPF solicitado mas campo permanece null.", "Conclusao": "✅ Correto."},
            {"Campo": "Endereco", "Analise": "‘ENDERECO NAO INFORMADO, 0’ – conforme áudio.", "Conclusao": "✅ Correto."},
            {"Campo": "Bairro", "Analise": "‘CENTRO’ – não citado, mas informado no sistema.", "Conclusao": "Sem contradição."},
            {"Campo": "Cidade", "Analise": "‘RIO DE JANEIRO’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "Estado", "Analise": "‘Rio de Janeiro’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "DocumentoFiscalDoacao", "Analise": "Sem documento fiscal.", "Conclusao": "✅ Correto."},
            {"Campo": "IdDebitoDoacao", "Analise": "‘21979809333’ – formado internamente.", "Conclusao": "✅ Correto."},
            {"Campo": "CategoriaDoacao", "Analise": "É uma doação via conta telefônica.", "Conclusao": "✅ Correto."},
            {"Campo": "NomeTitular", "Analise": "Ficou vazio, mas deveria conter o nome da doadora.", "Conclusao": "Ausência – ideal preencher com o nome."},
            {"Campo": "TipoRecebimento", "Analise": "‘Telefone’ confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "ValorDoacao", "Analise": "15 BRL – confirmado.", "Conclusao": "✅ Correto."},
            {"Campo": "EmpresaRecebimento", "Analise": "‘Claro Móvel’ confirmado.", "Conclusao": "✅ Correto."}
        ],
        "Observacao": "O campo NomeTitular está vazio, embora a doadora confirme ser titular."
    }
]


modo = st.sidebar.radio("Selecione o Modo de Visualização:", ["Global", "Por ID"])


if modo == "Global":
    st.header("Visão Global das Doações")
    
    st.subheader("Dados das Doações")
    st.dataframe(df.reset_index(drop=True))
    
    st.subheader("Métricas Gerais")
    total_doacoes = df.shape[0]
    valor_total = df["ValorDoacao"].sum()
    valor_medio = df["ValorDoacao"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Doações", total_doacoes)
    col2.metric("Valor Total (R$)", f"{valor_total:,.2f}")
    col3.metric("Valor Médio (R$)", f"{valor_medio:,.2f}")
    
    st.subheader("Visualizações Interativas")
    
    fig_bar = px.bar(
        df, 
        x="NomeDoador", 
        y="ValorDoacao", 
        color="EmpresaRecebimento",
        title="Valor das Doações por Doador",
        labels={"ValorDoacao": "Valor (R$)", "NomeDoador": "Doador"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    fig_pie = px.pie(
        df, 
        names="TipoRecebimento", 
        values="ValorDoacao",
        title="Distribuição dos Valores por Tipo de Recebimento"
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    fig_hist = px.histogram(
        df, 
        x="ValorDoacao", 
        nbins=10, 
        title="Distribuição dos Valores das Doações",
        labels={"ValorDoacao": "Valor (R$)"}
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    
    df_emp = df.groupby("EmpresaRecebimento")["ValorDoacao"].agg(["mean", "sum", "count"]).reset_index()
    fig_bar_emp = px.bar(
        df_emp, 
        x="EmpresaRecebimento", 
        y="mean", 
        title="Valor Médio das Doações por Empresa",
        labels={"mean": "Valor Médio (R$)"}
    )
    st.plotly_chart(fig_bar_emp, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Desenvolvido para a Legião da Boa Vontade (LBV) – Juntos pela transformação social!")


else:
    st.header("Detalhes da Doação por ID")
    ids_analise = [str(item["IdGravacao"]) for item in analysis_data]
    selected_id = st.selectbox("Selecione o ID da Doação:", ids_analise)
    
    # Buscar a análise selecionada
    selected_analysis = next(item for item in analysis_data if str(item["IdGravacao"]) == selected_id)
    
    # Exibir os dados da doação correspondente (buscando no DataFrame)
    doacao_info = df[df["IdGravacao"] == int(selected_id)]
    st.subheader("Dados da Doação")
    st.dataframe(doacao_info.reset_index(drop=True))
    
    st.subheader("Análise Completa da Doação (Resultados da IA)")
    for campo in selected_analysis["Campos"]:
        st.markdown(f"**Campo:** {campo['Campo']}")
        st.markdown(f" - **Análise da IA:** {campo['Analise']}")
        st.markdown(f" - **Conclusão da IA:** {campo['Conclusao']}")
        st.markdown("---")
    st.markdown("**Observação Geral:**")
    st.info(selected_analysis["Observacao"])
    
    st.markdown("---")
    st.markdown("### Desenvolvido para a Legião da Boa Vontade (LBV) – Juntos pela transformação social!")
