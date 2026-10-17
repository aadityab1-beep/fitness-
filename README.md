# fitness- | Athletic Conditioning & Performance Analytics Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://www.python.org/)

An open-source, local-first analytics engine and tracking tool engineered for performance athletes, strength coaches, and independent trainees. Designed to eliminate proprietary black-box algorithms and cloud-based subscription barriers in fitness tracking.

---

## Key Features

- **Progressive Overload Tracking:** Automatic computation of total volume load (Sets × Reps × Load), muscle group tonnage, and intensity distribution over time.
- **Adaptive Macronutrient & Caloric Engine:** Mathematical modeling for basal metabolic rate (BMR), total daily energy expenditure (TDEE), and automated macro periodization across hypertrophy, deficit, and maintenance phases.
- **Local-First & Extensible Data Architecture:** Lightweight JSON and CSV data stores with zero third-party cloud lock-in or telemetry.
- **Modular Architecture:** Structured for easy integration into custom coaching scripts, CLI utilities, or web-based dashboards.

---

## Project Structure

```text
fitness-/
├── README.md
├── requirements.txt
├── tracker.py
└── data/
    └── session_logs.json
