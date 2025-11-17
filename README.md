# 🏭 ResearchForge AI – Autonomous Literature Review Intelligence System

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)]()
[![Google ADK](https://img.shields.io/badge/Google_ADK-0.1.0-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

> **An advanced multi‑agent AI system that automates research discovery, paper analysis, and literature review generation end‑to‑end.**

**ResearchForge AI** is a fully autonomous research‑automation engine powered by **Google’s Agent Development Kit (ADK)**. Using a coordinated set of specialized agents, it finds academic papers, analyzes them, extracts citations, synthesizes knowledge, and iteratively refines a complete literature review within minutes.

---

## 🎯 Problem Overview

Researchers, students, and professionals spend a massive amount of time on literature reviews:

* 20–30 hours searching and filtering papers
* 30–40 hours reading + taking notes
* 20–30 hours writing and structuring the review
* 10–20 hours polishing and cross‑checking

Total ≈ **80–120 hours per review**.

### Core Challenges

* 🔍 Time‑consuming manual search
* 📚 Hard to keep track of all relevant papers
* ✍️ Maintaining good structure and writing consistency
* 📑 Citation formatting takes too long
* 🧠 Requires domain expertise

---

## 💡 ResearchForge AI – The Solution

ResearchForge compresses **weeks of effort** into **3–5 minutes**.

### 🔧 Workflow Breakdown

```
User Topic → Paper Discovery → PDF Processing → Content Analysis
           → Synthesis → Iterative Refinement → Final Review
```

The system automatically:

* Finds the most relevant academic papers
* Downloads PDFs and extracts important content
* Summarizes major contributions and insights
* Identifies themes, patterns, and research gaps
* Writes a polished, structured literature review (1500–2000 words)
* Refines it using a multi‑iteration scoring loop

---

## 🤖 Multi‑Agent Architecture

ResearchForge uses a network of coordinated agents:

```
┌──────────────────────────────┐
│  MasterCoordinator (Root)     │
│  - Controls end‑to‑end flow   │
└──────────────────────────────┘
                 ↓
      ┌──────────────────────┐  
      │ Discovery Agent      │ → Performs online paper search
      └──────────────────────┘
                 ↓
      ┌──────────────────────┐
      │ Analysis Agent        │ → Extracts text, citations, summaries
      └──────────────────────┘
                 ↓
      ┌──────────────────────┐
      │ Synthesis Agent       │ → Writes structured literature review
      └──────────────────────┘
                 ↓
      ┌──────────────────────┐
      │ Refinement Loop       │ → Iteratively improves quality (score ≥ 8)
      └──────────────────────┘
```

---

## 🧠 ADK Concepts Demonstrated

This project showcases more than **5 high‑value ADK capabilities**:

### ⭐ Multi‑Agent Orchestration

* Sequential workflow pipeline
* Loop‑based refinement using quality scoring
* Extendable design for parallel processing

### ⭐ Custom Tools

* PDF fetching & text extraction
* APA/BibTeX citation generator
* Quality evaluator for draft scoring

### ⭐ Built‑in Integrations

* Google Search Tool for academic queries

### ⭐ Session Memory

* Maintains context throughout the multi‑stage workflow

### ⭐ Logging & Observability

* Detailed logs for debugging and performance analysis

---

## 🧰 Tech Stack

| Component   | Technology       |
| ----------- | ---------------- |
| Framework   | Google ADK       |
| AI Model    | Gemini 2.0 Flash |
| Language    | Python 3.12+     |
| PDF Tools   | PyMuPDF, PyPDF2  |
| Environment | python‑dotenv    |
| Testing     | pytest           |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/jatin009v/Capstone-Project-for-the-5-Day-AI-Agents.git
cd Capstone-Project-for-the-5-Day-AI-Agents
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/MacOS
.venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Copy `.env.example` → `.env`, then add:

```
GOOGLE_API_KEY=your_key_here
```
# Optional: Deployment Settings
# PROJECT_ID=your-gcp-project-id
# REGION=us-central1git add .env.example
---

## 🚀 Usage

### Interactive Mode

```bash
python src/agent.py
```

### Direct Topic

```bash
python src/agent.py "machine learning in healthcare"
```

### Quick Demo

```bash
python src/agent.py --test
```

---

## 📂 Project Structure

```
project_root/
│   README.md
│   requirements.txt
│   .env.example
│   researchforge.log
│
├── src/
│   ├── agent.py
│   ├── config/prompts.py
│   └── tools/
│       ├── pdf_tools.py
│       ├── citation_tools.py
│       └── evaluation_tools.py
│
└── data/
    └── generated_reviews/
```

---

## 📊 Evaluation Criteria

| Criterion | Weight |
| --------- | ------ |
| Structure | 2      |
| Length    | 2      |
| Citations | 2      |
| Coverage  | 2      |
| Clarity   | 2      |

Minimum score to finalize output: **8/10**.

---

## 🐛 Troubleshooting

### API key missing

Add your key to `.env`.

### PDF fails to download

Likely due to restricted or broken links.

### Rate Limit

Wait 1 minute or try again.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---


### 🏭 **ResearchForge AI**

**Automating Knowledge. Accelerating Discovery.**

