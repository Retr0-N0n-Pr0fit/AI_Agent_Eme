# 🧑‍🌾 Eme-Bot: Consejera de Eme Ranchito 🌾

Eme-Bot es un asistente conversacional inteligente desarrollado para **Granja Eme Ranchito**. Utiliza un sistema RAG (Generación Aumentada por Recuperación) para responder preguntas sobre políticas corporativas, estatutos operacionales y privacidad de datos, basándose estrictamente en los documentos del repositorio.

---

## 🚀 Características

* **RAG Dinámico (Base de Conocimiento):** Escanea y lee automáticamente cualquier archivo PDF o CSV que se encuentre en la raíz del repositorio.
* **Contexto Inteligente:** Utiliza el modelo `gemini-2.5-flash` de Google a través de LangChain, ofreciendo respuestas claras, profesionales y con un toque cálido de campo.
* **Carga de Archivos al Vuelo:** Permite a los usuarios subir PDFs o CSVs adicionales desde la barra lateral de Streamlit para expandir el conocimiento del bot durante la sesión.
* **Interfaz Limpia:** Panel de chat interactivo diseñado con Streamlit y avatares personalizados.

---

## 🛠️ Tecnologías Utilizadas

* **Framework de la Aplicación:** [Streamlit](https://streamlit.io/)
* **Orquestación de IA:** [LangChain](https://www.langchain.com/)
* **Modelo de Lenguaje:** Google Gemini (`gemini-2.5-flash`)
* **Lectura de Documentos:** `PyPDFLoader` y `pandas`

---

## 📂 Estructura del Repositorio

```text
├── manual_faqs_eme_ranchito.pdf
├── manual_politicas_y_privacidad_eme_ranchito.pdf
├── requirements.txt
├── streamlit_app.py
└── README.md
```
## ⚙️ Instalación y Configuración Local
Si deseas ejecutar este proyecto en tu computadora de forma local, sigue estos pasos:

## 1. Clona el repositorio:
```text
git clone [https://github.com/Retr0-N0n-Pr0fit/AI_Agent_Eme.git](https://github.com/Retr0-N0n-Pr0fit/AI_Agent_Eme.git)
cd AI_Agent_Eme
```
## 2. Instala las librerías necesarias:
```text
pip install -r requirements.txt
```
## 3. Configura tu API Key de Gemini:
Crea una carpeta llamada ```.streamlit``` en la raíz del proyecto, y dentro de ella crea un archivo llamado ```secrets.toml```. Añade tu clave de la siguiente manera:
```text
Ini, TOML
GEMINI_API_KEY = "tu_api_key_real_de_gemini_aqui"
```
## 4. Inicia la aplicación:
```text
streamlit run streamlit_app.py
```
## 🧑‍💻 ¿Cómo Funciona por Detrás?
1. **Documentos Base**: Al arrancar, el script busca en la raíz (```.```) cualquier archivo ```.pdf``` o ```.csv```. Extrae su texto y lo unifica para crear el contexto de la granja.

2. **Archivos Temporales**: Si usas el botón de la interfaz para subir un archivo, este se procesa e integra al contexto únicamente mientras la pestaña del navegador siga abierta.

3. **Control de Alucinaciones**: El sistema operativo de la IA (System Prompt) obliga a Gemini a responder únicamente con la información de los documentos procesados. Si el usuario pregunta algo que no viene en los manuales, el bot dirá amablemente que no cuenta con esa información.
---

# 💬 Ejemplos de Interacción (Preguntas Frecuentes)

Para validar que el agente está leyendo correctamente los documentos y no alucinando, puedes realizar las siguientes consultas de prueba en el chat. 

A continuación se listan las preguntas clave con las respuestas reales que genera **Eme-Bot**:

### ❓ Pregunta 1: ¿Qué productos venden en la granja y cuáles son sus precios ajustados corporativos?
> **Eme-Bot:** ¡Hola! Con gusto te comparto la información sobre los productos que vendemos en Granja Eme Ranchito y sus precios ajustados corporativos. Como sabes, nuestros precios reflejan la calidad artesanal y orgánica de nuestros productos, así como la certificación de "Artesano" o "Gemólogo".
> 
> Aquí tienes la lista, vecino:
> * **Queso de Vaca Estándar:** 322 o
> * **Queso de Cabra Reserva:** 525 o
> * **Mayonesa Premium:** 399 o
> * **Mayonesa de Pato:** 525 o
> * **Cerveza de Trigo Fina:** 280 o
> * **Vino de Fruta Ancestral:** 3,150 o
> * **Mermelada de Arándano:** 210 o
> * **Lingote de Hierro Puro:** 150 o (Tasa minera)
> * **Diamante de Veta Profunda:** 975 o (Con Gemólogo)
> 
> Espero que esta información te sea muy útil. ¡Estamos para servirte!

### ❓ Pregunta 2: ¿Cuál es la política o regla para vender frutas del invernadero o la producción de huevos y leche?
> **Eme-Bot:** ¡Hola! Con gusto te explico la política de Eme Ranchito respecto a la venta de frutas del invernadero, huevos y leche.
> 
> Mira, aquí en la granja tenemos una regla muy clara, la **"Regla del Valor Agregado de Eme Ranchito"**, que busca maximizar el beneficio y la eficiencia. Por eso, se prohíbe la venta directa de materias primas en su estado natural crudo.
> 
> Esto significa que:
> * **La leche** (ya sea de vaca o cabra) se destina de inmediato a nuestras prensas para ser transformada en queso.
> * **Los huevos** (de cualquier tamaño o especie, incluso los de pato o sombríos) se usan exclusivamente en nuestras máquinas de mayonesa para elaborar aderezos gourmet.
> * **Las frutas** cosechadas en el huerto y el invernadero se clasifican: las de alto contenido de azúcar van a la destilería para hacer vino, y las bayas o frutas con menor valor base se usan para producir mermeladas en tarros de conserva.
> 
> Así que, vecino, la idea es que todos nuestros productos salgan con un procesamiento secundario que les añade un valor especial. Solo en casos de excedentes extraordinarios que superen nuestra capacidad de procesamiento, o mediante acuerdos de trueque estratégicos con otros agricultores del valle, se podría considerar la venta de materias primas crudas.
> 
> ¡Esperamos que esta información te sea de mucha utilidad!

### ❓ Pregunta 3: ¿Qué hacen con las geodas y qué restricciones hay en la minería los días de mala suerte?
> **Eme-Bot:** ¡Hola, vecino! Con gusto te comparto la información sobre las geodas y las restricciones mineras en Eme Ranchito.
> 
> * **Sobre las geodas:** En Eme Ranchito, tenemos una política muy clara con las geodas. No las vendemos cerradas, ya que son como un tesoro escondido. Todas las geodas que recuperamos en nuestras expediciones mineras son llevadas al herrero local para que las abra de forma técnica. Esto tiene un costo fijo de 25 monedas de oro por unidad, pero nos permite descubrir y capturar el valor total de los minerales que contienen, ¡que pueden llegar hasta las 750 monedas de oro por pieza! Una vez abiertas, los minerales arqueológicos únicos sin registro previo se donan al museo local para fortalecer nuestras relaciones comunitarias. Los duplicados y las gemas de alta pureza, como diamantes, esmeraldas y cuarzos refinados, se venden en el mercado minorista para inyectar liquidez a la granja.
> * **Sobre las restricciones en la minería los días de mala suerte:** ¡Claro que sí! La seguridad es primordial en nuestras operaciones mineras. Si el reporte diario de fortuna o el canal meteorológico local predice un día de "espíritus perturbados" o "mala suerte", está estrictamente prohibido descender más allá de los niveles de seguridad controlados (Nivel 40, 80 y 120). Esta medida es crucial para prevenir la pérdida catastrófica de herramientas e inventario valioso, así como para evitar desmayos o ataques de la fauna hostil que habita en las profundidades.
> 
> Espero que esta información te sea de gran utilidad. ¡Estamos para servirte!

### ❓ Pregunta 4: ¿Cuál es la postura de la granja frente a la Corporación Joja y la privacidad de datos?
> **Eme-Bot:** ¡Hola! Con gusto te comparto la postura de Granja Eme Ranchito sobre la Corporación Joja y la privacidad de datos, que son temas muy importantes para nosotros aquí en el rancho.
> 
> **Respecto a la Corporación Joja:**
> Granja Eme Ranchito considera a la Corporación Joja como una amenaza directa para el bienestar socioeconómico, la ecología y la tradición artesanal de nuestra región. Sus prácticas comerciales agresivas, que buscan monopolizar recursos, devaluar precios artificialmente y dañar el suelo agrícola, van en contra de nuestros principios.
> Por esta razón, tenemos una prohibición absoluta e irrevocable de compartir cualquier tipo de información (financiera, logística o de clientes) con la Corporación Joja o sus agentes. Consideramos que esto sería una violación de nuestros estatutos más profundos y un intento de espionaje comercial. Mantener un bloqueo total de información es una medida de seguridad vital para la supervivencia y prosperidad de nuestra granja, ya que estamos comprometidos con un modelo de producción descentralizada, artesanal y de ciclo cerrado.
> 
> **En cuanto a la privacidad de datos:**
> En Eme Ranchito nos tomamos muy en serio la privacidad de nuestros clientes y proveedores. Te aseguro que:
> * **Confidencialidad absoluta:** Protegemos la identidad, los datos comerciales y los registros de consumo de toda nuestra red. Todas las transacciones se gestionan bajo un estricto principio de anonimato y reserva.
> * **Registros físicos:** Los registros contables de ventas y despachos se asientan exclusivamente en libros físicos, estructurados por los socios fundadores. No empleamos sistemas de seguimiento digital ni compartimos historiales comerciales con instituciones de control o terceras personas. Tus hábitos de compra se mantienen bajo el más estricto secreto comercial e industrial.
> * **Secretos industriales:** La información más valiosa, como la ubicación exacta de las vetas de minerales raros, los mapas de exploración minera y las fórmulas biológicas para optimizar cultivos, se clasifica como "Secretos Industriales de Nivel Crítico" o "Alta Seguridad". Estos datos no se almacenan en formatos digitales vulnerables y se prohíbe terminantemente su discusión pública, manteniéndose en la memoria operativa de los socios fundadores y en bitácoras físicas bajo estrictas medidas de seguridad.
> 
> Así que, vecino, puedes estar tranquilo de que tu información y nuestros secretos de producción están bien resguardados aquí en Eme Ranchito.
---
## 🖥️ Demostración

¡Puedes probar el agente en vivo haciendo clic en el siguiente enlace!

👉 **[Probar Eme-Bot en Streamlit Community Cloud](https://granja-eme-ranchito.streamlit.app/)**

---

### 📸 Vista Previa de la Interfaz

A continuación puedes ver cómo luce el panel de control y el flujo de conversación de Eme-Bot:

#### 1. Panel Principal y Documentación
Aquí se gestionan los manuales y políticas de la granja desde la barra lateral.
<img width="1854" height="881" alt="image" src="https://github.com/user-attachments/assets/617cd29c-139b-4537-b77d-52deb54f149b" />

#### 2. Flujo de Chat con el Agente
Demostración de una consulta en tiempo real utilizando la paleta rústica y minimalista.
<img width="1851" height="882" alt="image" src="https://github.com/user-attachments/assets/01e54f2e-7882-45d8-b516-f1a684093edb" />
