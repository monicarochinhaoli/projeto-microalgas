
import streamlit as st
from pathlib import Path

# =====================================================
# CONFIGURAÇÃO INICIAL
# =====================================================

st.set_page_config(
    page_title="Microalgas e Agricultura Sustentável",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Caminho da pasta de imagens
PASTA_IMAGENS = Path("imagens")


def exibir_imagem(nome_arquivo, legenda, use_container_width=True):
    """Exibe a imagem se o arquivo estiver disponível."""
    caminho = PASTA_IMAGENS / nome_arquivo

    if caminho.exists():
        st.image(
            str(caminho),
            caption=legenda,
            use_container_width=use_container_width
        )
    else:
        st.warning(
            f"Imagem não encontrada: {caminho}. "
            "Confira se o arquivo está na pasta imagens."
        )


# =====================================================
# SEÇÃO 1 - APRESENTAÇÃO DO PROJETO
# =====================================================

with st.container(border=True):

    st.title("Microalgas e Agricultura Sustentável")

    st.subheader(
        "Cultivo de Limnospira sp. em efluente de carcinicultura"
    )

    st.write("""
    O projeto investiga o cultivo da microalga Limnospira sp.
    utilizando efluente da carcinicultura como meio alternativo
    de cultivo.

    A pesquisa busca avaliar o crescimento da microalga, as
    características da biomassa produzida, seu perfil
    fito-hormonal e seu potencial de aplicação como
    bioestimulante na agricultura.
    """)

    exibir_imagem(
        "cultivo.jpg",
        "Cultivo de Limnospira sp."
    )

    st.caption(
        "Projeto de pesquisa desenvolvido no Doutorado em Agronomia – IF Goiano."
    )


# =====================================================
# SEÇÃO 2 - CONTEXTUALIZAÇÃO E JUSTIFICATIVA
# =====================================================

st.write("---")

st.header("🌱 Contextualização da pesquisa")

st.write("""
A carcinicultura é uma atividade importante para a produção
de alimentos e para o desenvolvimento econômico de regiões
costeiras. Entretanto, seu funcionamento gera efluentes
contendo nutrientes e matéria orgânica, cujo descarte
inadequado pode contribuir para impactos ambientais.

Nesse contexto, o cultivo de microalgas surge como uma
alternativa biotecnológica para o aproveitamento desses
efluentes. Esses microrganismos apresentam capacidade de
assimilar nutrientes dissolvidos na água e produzir biomassa
com potencial de utilização em diferentes setores.
""")

st.header("🔬 Justificativa")

st.write("""
A utilização de efluentes da carcinicultura no cultivo de
Limnospira sp. pode contribuir para estratégias de
reaproveitamento de nutrientes e produção sustentável
de biomassa.

Além disso, a investigação do perfil fito-hormonal dessa
biomassa poderá ampliar o conhecimento sobre seu potencial
de aplicação como bioestimulante agrícola, contribuindo
para o desenvolvimento de alternativas biotecnológicas
associadas à agricultura sustentável.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "♻️ **Reaproveitamento**\n\n"
        "Valorização de nutrientes presentes nos efluentes."
    )

with col2:
    st.info(
        "🧫 **Biotecnologia**\n\n"
        "Cultivo e caracterização de biomassa microalgal."
    )

with col3:
    st.info(
        "🌾 **Agricultura**\n\n"
        "Investigação do potencial bioestimulante da biomassa."
    )


# =====================================================
# SEÇÃO 3 - OBJETIVOS DA PESQUISA
# =====================================================

st.write("---")

st.header("🎯 Objetivos da pesquisa")

st.subheader("Objetivo geral")

st.write("""
Avaliar o cultivo de Limnospira sp. em efluente de
carcinicultura, considerando o crescimento microalgal,
as características da biomassa produzida, seu perfil
fito-hormonal e seu potencial como bioestimulante agrícola.
""")

st.subheader("Objetivos específicos")

objetivos = [
    "Avaliar o crescimento de Limnospira sp. em diferentes proporções de efluente de carcinicultura.",
    "Monitorar parâmetros físico-químicos dos meios de cultivo durante o desenvolvimento da microalga.",
    "Caracterizar a biomassa microalgal obtida ao final dos cultivos.",
    "Investigar o perfil de fitormônios presentes na biomassa produzida.",
    "Avaliar o potencial bioestimulante da biomassa em plantas cultivadas.",
    "Investigar a viabilidade do aproveitamento de efluentes aquícolas na produção de biomassa com aplicação agrícola."
]

for i, objetivo in enumerate(objetivos, start=1):
    st.write(f"**{i}.** {objetivo}")


# =====================================================
# SEÇÃO 4 - METODOLOGIA DA PESQUISA
# =====================================================

st.write("---")

st.header("🧪 Metodologia experimental")

st.write("""
A pesquisa será desenvolvida em etapas experimentais,
envolvendo o cultivo de Limnospira sp. em diferentes
proporções de efluente de carcinicultura, o acompanhamento
do crescimento microalgal e a caracterização da biomassa.
""")

st.subheader("1. Cultivo da microalga")

st.write("""
A microalga Limnospira sp. será cultivada em meio Zarrouk
(controle) e em meios preparados com diferentes proporções
de efluente de carcinicultura.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Controle", "0%")

with col2:
    st.metric("Tratamento 1", "25%")

with col3:
    st.metric("Tratamento 2", "50%")

with col4:
    st.metric("Tratamento 3", "100%")

st.subheader("2. Monitoramento do crescimento")

st.write("""
Durante o cultivo, serão acompanhados o desenvolvimento
da biomassa microalgal e parâmetros físico-químicos dos
meios, incluindo pH e indicadores de crescimento.
""")

st.subheader("3. Caracterização da biomassa")

st.write("""
A biomassa obtida será submetida a procedimentos de
preparo e caracterização, incluindo a investigação
de sua composição e do perfil de fitormônios.
""")

st.subheader("4. Avaliação do potencial bioestimulante")

st.write("""
A biomassa microalgal será investigada quanto ao seu
potencial de aplicação como bioestimulante agrícola,
por meio de ensaios com plantas cultivadas.
""")


# =====================================================
# SEÇÃO 5 - RESULTADOS ESPERADOS
# =====================================================

st.write("---")

st.header("📊 Resultados esperados")

st.write("""
Espera-se que os resultados contribuam para ampliar
o conhecimento sobre o cultivo de Limnospira sp.
em efluentes de carcinicultura e sobre as possibilidades
de utilização da biomassa microalgal na agricultura.
""")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🧫 Produção de biomassa")
        st.write("""
        - Identificação das condições de cultivo mais favoráveis.
        - Avaliação do crescimento microalgal.
        - Caracterização da biomassa produzida.
        """)

with col2:
    with st.container(border=True):
        st.subheader("🌱 Potencial bioestimulante")
        st.write("""
        - Investigação do perfil fito-hormonal.
        - Avaliação da aplicação da biomassa em plantas.
        - Identificação de possíveis respostas bioestimulantes.
        """)

st.info("""
**Contribuição esperada:** integrar a biotecnologia de microalgas,
o reaproveitamento de efluentes aquícolas e o desenvolvimento
de alternativas sustentáveis para a agricultura.
""")


# =====================================================
# SEÇÃO 6 - INSTITUIÇÃO E EQUIPE
# =====================================================

st.write("---")

st.header("🎓 Instituição e equipe")

st.write("""
**Programa:** Doutorado em Agronomia

**Instituição:** Instituto Federal Goiano – IF Goiano

**Área de pesquisa:** Tecnologias sustentáveis em sistemas
de produção e uso do solo e água.
""")

st.write("**Pesquisadora:** Mônica Rocha de Oliveira")
st.write("**Orientador:** Prof. Dr. Edson Luiz Souchie")


# =====================================================
# SEÇÃO 7 - GALERIA DE IMAGENS
# =====================================================

st.write("---")

st.header("📸 Galeria do projeto")

st.write("""
Registros das atividades experimentais e das aplicações
biotecnológicas relacionadas à pesquisa.
""")

col1, col2, col3 = st.columns(3)

with col1:
    exibir_imagem(
        "cultivo.jpg",
        "Cultivo de Limnospira sp."
    )

with col2:
    exibir_imagem(
        "laboratorio.jpg",
        "Atividades laboratoriais"
    )

with col3:
    exibir_imagem(
        "agricultura.jpg",
        "Aplicações agrícolas"
    )


# =====================================================
# SEÇÃO 8 - RODAPÉ
# =====================================================

st.write("---")

st.markdown(
    """
    <div style="text-align: center;">
        <h4>Microalgas e Agricultura Sustentável</h4>
        <p>Projeto de Doutorado em Agronomia</p>
        <p>Instituto Federal Goiano – IF Goiano</p>
        <p>2026</p>
        <small>Pesquisa, inovação e sustentabilidade.</small>
    </div>
    """,
    unsafe_allow_html=True
)
