# 👨‍⚕️ Data Surgeon — Agentic AI Insight Bot

A **Streamlit web app** that performs "surgery" on your CSV data — you ask questions in plain English (like *"show me the top 5 performers"* or *"create a histogram of the score"*), and an **AI Agent** (LangChain + Groq Llama 3.3) writes Python/Pandas code on its own in the background to answer that question — both as text and, if you ask for a chart, as a graph too.

---

##  How It Works (Architecture)

1. The user uploads a CSV file → Pandas creates a `DataFrame`.
2. `create_pandas_dataframe_agent` (LangChain Experimental) sets up an **Agentic AI** that:
   - Understands the user's question
   - Writes Pandas code on its own based on the question
   - **Executes** that code (in a sandbox)
   - Explains the result back in natural language
3. The **Groq API** (Llama 3.3 70B) is used for the LLM — it's **free and very fast**.
4. If the query includes a keyword like "plot/chart/graph/hist/bar," a Matplotlib-generated graph is also shown in the Streamlit UI.

---

## 📁 Project Structure

```
data-surgeon-agentic-ai/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example         # Sample env variable file (add your API key here)
├── .gitignore
├── .vscode/
│   └── settings.json
└── README.md
```

---

## ✅ Requirements

- **Python 3.10 – 3.13**
- **VS Code** (with Python extension installed)
- A **free Groq API key** — get it from https://console.groq.com/keys (sign-up is free)

---

## 🚀 Setup & How to Run in VS Code

### Step 1 — Open the Project in VS Code
1. Open VS Code.
2. `File → Open Folder` → select the `data-surgeon-agentic-ai` folder.
3. If the Python extension isn't installed, open Extensions (`Ctrl+Shift+X`), search for "**Python**," and install it (by Microsoft).

### Step 2 — Open the Terminal
Inside VS Code: `Terminal → New Terminal` (or shortcut ``Ctrl+` ``)

### Step 3 — Create a Virtual Environment (recommended)
```bash
python -m venv .venv
```

Activate it:
- **Windows (PowerShell):**
  ```bash
  .venv\Scripts\activate
  ```
- **Mac / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Once activated, you'll see `(.venv)` at the start of the terminal prompt.

> 💡 VS Code will also prompt "Select python interpreter" in the bottom-right corner — choose the `.venv` interpreter there.

### Step 4 — Install Dependencies
```bash
pip install -r requirements.txt
```
(This will take a bit of time since it downloads libraries like langchain, faiss, etc.)

### Step 5 — Set Up Your API Key
1. Copy the `.env.example` file and rename it to `.env` (or create a new `.env` file).
2. Add your Groq key in it:
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
   ```
3. Get a free key here → https://console.groq.com/keys

> ⚠️ Never push the `.env` file to GitHub — it's already added to `.gitignore`, so it's safe.

### Step 6 — Run the App
In the terminal:
```bash
streamlit run app.py
```

As soon as this command runs, the app will automatically open in your browser at `http://localhost:8501`.

### Step 7 — Use the App
1. Upload a CSV file.
2. Type your question in the "Surgeon's Console," for example:
   - `Who is the top performer in MidTerm_Score?`
   - `Show me a bar chart of average scores by subject`
   - `What is the average age of students?`
3. Press Enter — the agent will write and execute the code on its own and show you the answer + (if requested) a chart.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `GROQ_API_KEY not found` error | Check the `.env` file; the key should be in the correct `GROQ_API_KEY=...` format with no spaces |
| `ModuleNotFoundError` | Check whether the virtual environment is activated, then run `pip install -r requirements.txt` again |
| App is slow/showing an error | You may have hit Groq's free tier rate limit — wait a bit and try again |
| Chart isn't showing | Include a keyword like "plot," "chart," "graph," "hist," or "bar" in your query |

---

## ⚠️ Security Note

`app.py` has `allow_dangerous_code=True` set — this means the agent **directly executes** AI-generated Python code. This is fine only for **learning/personal sandbox** use. Before using this app in production or giving access to any untrusted user, proper sandboxing (like Docker isolation) should be added.

---

## 📦 Tech Stack

- **Streamlit** — UI
- **LangChain + LangChain Experimental** — Agentic AI framework
- **Groq (Llama 3.3 70B)** — LLM (free & fast inference)
- **Pandas, Matplotlib, Seaborn** — Data handling & visualization
- **python-dotenv** — Environment variable management