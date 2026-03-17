---
name: browser-automation
description: Advanced browser automation skill combining Patchright (stealth, anti-detection, full API) and Agent Browser (fast CLI, lightweight). Optimized for scraping, testing, screenshots, and resilient automation workflows.
---

# 🌐🧠 Browser Automation  
### Patchright × Agent Browser

<p align="center">
  <b>Adaptive automation for modern web environments</b><br>
  <sub>Stealth-aware • Fast execution • Agent-optimized</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Skill-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Patchright-Stealth-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/AgentBrowser-CLI-green?style=for-the-badge">
</p>

---

## 🧠 Overview

This skill provides a **dual-engine browser automation system** designed for OpenClaw agents operating across varying levels of complexity and detection sensitivity.

It introduces an **adaptive execution model**, allowing agents to dynamically switch between:

- 🛡️ **Patchright** → deep control, stealth, anti-detection  
- ⚡ **Agent Browser** → speed, simplicity, low overhead  

---

## ⚡ Decision Matrix

| Scenario                              | Engine           |
|--------------------------------------|------------------|
| Protected / anti-bot environments    | 🛡️ Patchright     |
| Dynamic or JS-heavy applications     | 🛡️ Patchright     |
| Network inspection required          | 🛡️ Patchright     |
| Simple navigation / quick tasks      | ⚡ Agent Browser  |
| CLI-driven workflows                | ⚡ Agent Browser  |
| Low-latency execution               | ⚡ Agent Browser  |

---

## 🛡️ Patchright — Stealth Execution Core

> High-control engine for complex and protected targets

### 🔑 Capabilities

- Anti-bot detection mitigation  
- Playwright-compatible API  
- Multi-browser support (Chromium, Firefox, WebKit)  
- Network interception & request manipulation  
- PDF generation & full-page rendering  
- Video recording and tracing  

### 🧠 Operational Role

- Handles **high-risk environments**
- Maintains **behavioral realism**
- Enables **deep automation control**

---

## ⚡ Agent Browser — Rapid Execution Layer

> Lightweight CLI engine optimized for speed and simplicity

### 🔑 Capabilities

- Fast browser control via CLI  
- Element-based interaction system (`@e1`, `@e2`, …)  
- Instant startup and execution  
- Minimal resource consumption  
- Efficient for short-lived automation tasks  

### 🧠 Operational Role

- Handles **low-complexity workflows**
- Maximizes **execution speed**
- Supports **agent scripting pipelines**

---

## 🏗️ Architecture
browser-automation/
│
├── patchright/ # Stealth + full API engine
├── agent-browser/ # CLI-based execution engine
│
├── strategies/ # Decision routing logic
│ ├── selector.py
│ └── scoring.py
│
├── workflows/ # Reusable automation patterns
│ ├── scraping/
│ ├── navigation/
│ └── forms/
│
├── detection/ # Anti-bot heuristics
├── utils/ # Shared utilities
│
└── README.md


---

## 🔄 Execution Model

This skill follows a **dynamic routing strategy**:


analyze(task):
if requires_stealth or is_protected:
return Patchright
else:
return AgentBrowser


### 🧠 Routing Factors

- Detection sensitivity  
- Page complexity  
- Execution time constraints  
- Resource availability  
- Interaction depth  

---

## 📊 Performance Profile

| Capability            | Patchright        | Agent Browser     |
|----------------------|------------------|------------------|
| Anti-detection       | 🛡️ High          | ❌ None          |
| Speed                | ⚠️ Moderate      | ⚡ High          |
| Flexibility          | 🧠 Full API      | ⚙️ Structured    |
| Resource Usage       | ⚠️ Higher        | ✅ Low           |
| Startup Time         | ⚠️ Medium        | ⚡ Instant       |
| Best Use Case        | Protected flows  | Quick tasks      |

---

## 🧠 Design Principles

- 🛡️ **Stealth-first execution**  
- ⚡ **Speed where possible**  
- 🧠 **Adaptive decision-making**  
- 🔄 **Composable workflows**  

---

## 🔐 Operational Guidelines

- Prefer Patchright for **protected or monitored targets**  
- Prefer Agent Browser for **stateless or repetitive tasks**  
- Combine both engines for **hybrid workflows**  
- Avoid unnecessary overhead by selecting the correct engine early  

---

## 🧩 Integration Role

Within an OpenClaw agent pipeline, this skill acts as:

> ⚙️ A **core execution layer** responsible for all browser-based interactions

It enhances:

- Reliability  
- Task success rate  
- Execution efficiency  
- Environmental adaptability  

---

## ⚠️ Disclaimer

> 🚨 Authorized and ethical use only

This skill is intended for:

- Development  
- Testing  
- Research  

Do **not** use it to:

- Bypass protections without permission  
- Abuse or overload services  
- Violate platform policies or laws  

---

## 🤝 Contributing

Focus areas:

- Smarter routing logic  
- Detection avoidance improvements  
- Performance tuning  
- New automation strategies  

---

## 🧬 Final Thought

> “Effective automation is not just fast — it’s adaptive.”
