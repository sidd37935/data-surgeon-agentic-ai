# 👨‍⚕️ Data Surgeon — Agentic AI Insight Bot

Ek **Streamlit web app** jo aapke CSV data pe "surgery" karta hai — aap plain English/Hindi mein sawal poochte ho (jaise *"top 5 performers dikhao"* ya *"score ka histogram banao"*), aur ek **AI Agent** (LangChain + Groq Llama 3.3) background mein khud Python/Pandas code likh kar us sawal ka jawab deta hai — text mein bhi, aur agar chart mangoge to graph bana kar bhi.

---

## 🧠 Ye kaise kaam karta hai (Architecture)

1. User CSV file upload karta hai → Pandas se `DataFrame` bana.
2. `create_pandas_dataframe_agent` (LangChain Experimental) ek **Agentic AI** setup karta hai jo:
   - User ke question ko samajhta hai
   - Uske hisaab se khud Pandas code **likhta** hai
   - Us code ko **execute** karta hai (sandbox mein)
   - Result ko wapas natural language mein explain karta hai
3. LLM ke liye **Groq API** (Llama 3.3 70B) use hota hai — ye **free & bahut fast** hai.
4. Agar query mein "plot/chart/graph/hist/bar" jaisa keyword ho, to Matplotlib se bana graph bhi Streamlit UI mein dikha diya jata hai.

---

## 📁 Project Structure

```
data-surgeon-agentic-ai/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example         # Env variable ka sample (apni API key yahan daalni hai)
├── .gitignore
├── .vscode/
│   └── settings.json
└── README.md
```

---

## ✅ Requirements

- **Python 3.10 – 3.13**
- **VS Code** (with Python extension installed)
- Ek **free Groq API key** — https://console.groq.com/keys se milegi (sign up free hai)

---

## 🚀 Setup & VS Code me chalane ka pura tareeka

### Step 1 — Project VS Code me kholo
1. VS Code open karo.
2. `File → Open Folder` → `data-surgeon-agentic-ai` folder select karo.
3. Agar Python extension installed nahi hai, to Extensions (`Ctrl+Shift+X`) mein "**Python**" search karke install kar lo (by Microsoft).

### Step 2 — Terminal kholo
VS Code ke andar: `Terminal → New Terminal` (ya shortcut ``Ctrl+` ``)

### Step 3 — Virtual environment banao (recommended)
```bash
python -m venv .venv
```

Activate karo:
- **Windows (PowerShell):**
  ```bash
  .venv\Scripts\activate
  ```
- **Mac / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Activate hone ke baad terminal ke start mein `(.venv)` dikhega.

> 💡 VS Code niche-right corner mein bhi puchega "Select python interpreter" — usme `.venv` wala interpreter choose kar lena.

### Step 4 — Dependencies install karo
```bash
pip install -r requirements.txt
```
(Isme thoda time lagega kyunki langchain, faiss jaisi libraries download hongi.)

### Step 5 — API Key set karo
1. `.env.example` file ko copy karke naam `.env` rakho (ya naya `.env` file banao).
2. Usme apni Groq key daalo:
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
   ```
3. Key free milti hai yahan se → https://console.groq.com/keys

> ⚠️ `.env` file kabhi GitHub pe push mat karna — ye already `.gitignore` mein add hai isliye safe hai.

### Step 6 — App run karo
Terminal mein:
```bash
streamlit run app.py
```

Ye command chalte hi automatically browser mein `http://localhost:8501` open ho jayega jahan app chal rahi hogi.

### Step 7 — App use karo
1. Ek CSV file upload karo.
2. "Surgeon's Console" mein apna question type karo, jaise:
   - `Who is the top performer in MidTerm_Score?`
   - `Show me a bar chart of average scores by subject`
   - `What is the average age of students?`
3. Enter dabao — agent khud code likh kar execute karega aur jawab + (agar mangoge to) chart dikhayega.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `GROQ_API_KEY nahi mili` error | `.env` file check karo, key sahi se `GROQ_API_KEY=...` format mein honi chahiye, spaces na ho |
| `ModuleNotFoundError` | Virtual environment activate hai ya nahi check karo, phir dobara `pip install -r requirements.txt` chalao |
| App slow/error de rahi hai | Groq free tier ki rate limit lag sakti hai — thodi der ruk kar dobara try karo |
| Chart nahi dikh raha | Query mein "plot", "chart", "graph", "hist", "bar" jaisa keyword include karo |

---

## ⚠️ Security Note

`app.py` mein `allow_dangerous_code=True` set hai — iska matlab agent AI-generated Python code ko **directly execute** karta hai. Ye sirf **learning/personal sandbox** ke liye theek hai. Production ya kisi untrusted user ko is app tak access dene se pehle proper sandboxing (jaise Docker isolation) add karna chahiye.

---

## 📦 Tech Stack

- **Streamlit** — UI
- **LangChain + LangChain Experimental** — Agentic AI framework
- **Groq (Llama 3.3 70B)** — LLM (free & fast inference)
- **Pandas, Matplotlib, Seaborn** — Data handling & visualization
- **python-dotenv** — Environment variable management
