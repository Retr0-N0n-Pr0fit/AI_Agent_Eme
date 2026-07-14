import streamlit as st
import pandas as pd
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(page_title="Eme-Bot Ranchito", page_icon="🌾", layout="wide")
st.title("🧑‍🌾 Eme-Bot: Consejera de Eme Ranchito 🌾")

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ Error: No se encontró la clave GEMINI_API_KEY en los secretos.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

DOCS_FOLDER = "."

with st.sidebar:
    st.header("🌾 Gestión de Granja")
    st.subheader("Subir Nuevos Documentos")
    
    archivos_nuevos = st.file_uploader(
        "Carga archivos PDF o CSV adicionales para expandir el conocimiento del agente:", 
        type=["pdf", "csv"], 
        accept_multiple_files=True
    )
    
    st.write("---")
    st.subheader("📚 Documentos Vigentes")
    
    documentos_activos = []
    if os.path.exists(DOCS_FOLDER):
        documentos_activos = [f for f in os.listdir(DOCS_FOLDER) if f.endswith(('.pdf', '.csv'))]
    
    if archivos_nuevos:
        for f in archivos_nuevos:
            documentos_activos.append(f"🆕 {f.name} (En memoria)")
            
    if documentos_activos:
        for doc in documentos_activos:
            st.markdown(f"- `{doc}`")
    else:
        st.info("No se encontraron archivos PDF o CSV en la raíz.")


def cargar_base_conocimiento(archivos_extra):
    textos_contexto = []
    
    if os.path.exists(DOCS_FOLDER):
        for archivo in os.listdir(DOCS_FOLDER):
            ruta_completa = os.path.join(DOCS_FOLDER, archivo)
            
            if archivo.endswith(".pdf"):
                try:
                    loader = PyPDFLoader(ruta_completa)
                    paginas = loader.load()
                    for p in paginas:
                        textos_contexto.append(f"[Fuente: {archivo}, Página: {p.metadata.get('page', 0) + 1}] {p.page_content}")
                except Exception as e:
                    pass
            
            elif archivo.endswith(".csv"):
                try:
                    df = pd.read_csv(ruta_completa)
                    for idx, row in df.iterrows():
                        fila = ", ".join([f"{col}: {val}" for col, val in row.items()])
                        textos_contexto.append(f"[Fuente: {archivo}, Fila: {idx+1}] {fila}")
                except Exception as e:
                    pass
                    
    if archivos_extra:
        for archivo_subido in archivos_extra:
            with open(archivo_subido.name, "wb") as f:
                f.write(archivo_subido.getbuffer())
            
            if archivo_subido.name.endswith(".pdf"):
                loader = PyPDFLoader(archivo_subido.name)
                paginas = loader.load()
                for p in paginas:
                    textos_contexto.append(f"[Fuente: Extra ({archivo_subido.name}), Página: {p.metadata.get('page', 0) + 1}] {p.page_content}")
            
            elif archivo_subido.name.endswith(".csv"):
                df = pd.read_csv(archivo_subido.name)
                for idx, row in df.iterrows():
                    fila = ", ".join([f"{col}: {val}" for col, val in row.items()])
                    textos_contexto.append(f"[Fuente: Extra ({archivo_subido.name}), Fila: {idx+1}] {fila}")
            
            os.remove(archivo_subido.name)
                
    return "\n\n".join(textos_contexto)


contexto_unificado = cargar_base_conocimiento(archivos_nuevos)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

system_prompt = (
    "Eres Eme-Bot, la consejera e Inteligencia Artificial oficial de Eme Ranchito (Edición 2026).\n"
    "Responde de manera amable, servicial, profesional y con un toque cálido (puedes usar expresiones norteñas o de campo de forma sutil si es oportuno, como 'vecino').\n"
    "Básate estrictamente en el contexto proveído para responder.\n"
    "Si la información no se encuentra en los documentos, di amablemente que no dispones de ese dato en este momento.\n\n"
    "Contexto de Eme Ranchito:\n{context}"
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "¡Hola, vecino! Bienvenido a Eme Ranchito. Soy Eme-Bot 🧑‍🌾🌾. ¿En qué te puedo ayudar hoy? Puedo resolver tus dudas sobre nuestras políticas, privacidad o preguntas frecuentes."
        }
    ]

for msg in st.session_state.messages:
    avatar_chat = "🧑‍🌾" if msg["role"] == "assistant" else "👤"
    with st.chat_message(msg["role"], avatar=avatar_chat):
        st.write(msg["content"])

if usuario_input := st.chat_input("Pregúntale a Eme-Bot..."):
    st.session_state.messages.append({"role": "user", "content": usuario_input})
    with st.chat_message("user", avatar="👤"):
        st.write(usuario_input)

    with st.chat_message("assistant", avatar="🧑‍🌾"):
        mensajes_finales = prompt_template.format_messages(context=contexto_unificado, input=usuario_input)
        respuesta = llm.invoke(mensajes_finales)
        st.write(respuesta.content)
        
    st.session_state.messages.append({"role": "assistant", "content": respuesta.content})
