# 🌱 BLOM – Signal Intelligence Assistant

**“From digital pulse to planted vision.”**  
BLOM is a modular, Streamlit-based signal intelligence assistant designed to **scout, seed, and scale** meaningful insights from global data signals. Whether you're a curious learner, a transformation strategist, or a builder of tomorrow's ideas, BLOM empowers you to explore public trends, surface emergent patterns, and translate signals into actionable opportunities.

---

## 🌐 Overview

BLOM (**B**ehavioral **L**ogic for **O**pportunity **M**apping) serves as a **personal radar for global signals**. It pulls from open public APIs, trends, and feeds to:

- Discover **emerging trends** and topics
- Generate **insight prompts** for learning or ideation
- Enable **structured outputs** (YAML, Markdown, CSV)
- Build a portfolio of **opportunity briefs and pathways**

> 🎯 BLOM is **exploratory, non-commercial**, and built to scale from personal use to educational and community tools.

---

## ✨ Features

- ✅ **Streamlit Dashboard UI** – Lightweight, intuitive control tower interface
- ✅ **Modular Signal Scouts** – Easily add new data source connectors
- ✅ **Multi-format Output** – Export insights to Markdown, CSV, PNG, and YAML
- ✅ **Privacy-First** – Only uses non-authenticated, public APIs for MVP
- ✅ **No Cloud Dependency** – Runs locally with optional GitHub-hosted visibility

---

## 🧱 Tech Stack

| Layer              | Tools / Notes                                               |
|-------------------|-------------------------------------------------------------|
| 🖥️ UI              | Streamlit                                                   |
| 🧠 Logic           | Python scripts (modular logic per signal type)              |
| 🔗 Data Sources     | Google Trends, RSS, News APIs, data.gov.my, BNM            |
| 📦 Output Format    | Markdown, CSV, YAML, PNG                                   |
| 🚀 Deployment       | GitHub local runner (with optional Streamlit Cloud push)   |

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/hadzwanihasni/blom.git
cd blom
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

> ℹ️ No API keys or credentials are required for MVP sources. All data used is public and non-authenticated.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🔭 Roadmap

| Phase | Milestone                                    | Status     |
| ----- | -------------------------------------------- | ---------- |
| P0    | Scaffold BLOM Streamlit app                  | ✅ Complete |
| P1    | Add `pytrends`, RSS, and NewsCatcher sources | ⏳ In Dev   |
| P2    | Enable YAML + Markdown exports               | ⏳ In Dev   |
| P3    | Add Insight Prompt Generator Module          | 🔲 Planned |
| P4    | Package as GitHub Portfolio Piece            | 🔲 Planned |
| P5    | Optional: GPT Action integration             | 🔲 Backlog |

---

## 🌱 Motto & Intent

> “Nurturing signals to movements.”

BLOM is an open learning and ideation project — it is **not a commercial tool**, and it respects signal integrity, source attribution, and public access principles.

---

📍 Maintained by [@hadzwanihasni](https://github.com/hadzwanihasni) | Built for learning, scaling for possibility.
