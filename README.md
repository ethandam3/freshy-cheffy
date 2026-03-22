# 🐻 Freshy Cheffy

**BeachHacks 9.0 — Sustainability Track**

> Connecting Long Beach communities with affordable, rescued "ugly" produce — powered by machine learning.

---

## 🌊 The Problem

Every year, billions of pounds of perfectly good food are wasted because they look "wrong." At the same time, rising tariffs and inflation are making fresh produce unaffordable for everyday families. Local farmers are forced to throw out misfit vegetables while people in Long Beach struggle to eat healthy on a budget.

**Freshy Cheffy** fixes this — one ugly box at a time.

---

## 🤖 The ML Model

This is not just a website. Freshy Cheffy uses a **real machine learning price predictor** built with concepts from DSC 40A and COGS 108 at UCSD.

- **Algorithm**: SGD Regressor (Stochastic Gradient Descent) with MSE loss function
- **Features**: Produce item, season, and ugly produce flag
- **Training R²**: 0.931 (93.1% accuracy)
- **Framework**: scikit-learn + Flask REST API

The model predicts fair market prices for produce in the Long Beach area, then compares them against local farmer deals to show users exactly how much they're saving.

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Frontend | HTML, Tailwind CSS, JavaScript |
| Backend | Python, Flask |
| ML Model | scikit-learn, NumPy, pandas |
| Design | Figma, Stitch |
| Version Control | Git, GitHub |

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/ethandam3/freshy-cheffy.git
cd freshy-cheffy
```

**2. Install dependencies**
```bash
pip install flask flask-cors scikit-learn pandas numpy
```

**3. Train the model**
```bash
python model.py
```

**4. Start the Flask server**
```bash
python app.py
```

**5. Open in browser**
```
http://127.0.0.1:5000
```

---

## 📄 Pages

- **Home** — Latest innovations and community testimonials
- **About** — The Freshy Cheffy story and mission
- **Recipes** — The Daily Catch — community recipe feed
- **Deals** — Coastal Harvest Deals with ML price predictor + live map
- **Impact** — Tides of Change — community environmental stats
- **Community** — The Modern Mariner's Table — recipe sharing platform

---

## 💡 Key Features

- **ML Price Predictor** — Enter any produce item and season, get a real gradient descent price prediction
- **Ugly Produce Toggle** — See how much cheaper imperfect produce is vs regular retail
- **Local Farm Map** — Interactive Long Beach map showing nearby ugly produce deals
- **Impact Dashboard** — Real stats on CO2 diverted, meals shared, and community savings
- **Consistent Design** — Beach-themed UI with custom bear mascot, built in Figma + Stitch

---

## 👤 Team

**Ethan Dam** — Data Science, UC San Diego  
**Lauren Tran** — Marketing, CSU Long Beach  
BeachHacks 9.0 — Long Beach, CA

---

*"Every meal you save ripples across the Long Beach shoreline."* 🌊
