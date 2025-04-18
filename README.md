# agronomix-oss 🌱🐄  

**Open-Source Animal Feeding & Livestock Management Software**  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Build Status](https://img.shields.io/github/actions/workflow/status/dvozicnivod/agronomix-oss/python-app.yml)](https://github.com/dvozicnivod/agronomix-oss/actions)  

<img src="docs/screenshots/demo.png" width="600" alt="agronomix-oss Screenshot">  

## **Purpose**  
Empower small-scale farmers with free, modular tools to:  
- 🥛 **Optimize feed rations** (minimize cost, meet nutritional needs).  
- 🥚 **Track production** (milk, eggs, weight gain).  
- 📊 **Generate actionable reports** for better decision-making.  

**Long-Term Vision**: Core modules remain open-source, while advanced features (e.g., AI predictions, IoT integration) can be commercialized.  

---

## **Features**  
### Phase 1: MVP (Stable Release)  
- **Feed Calculator**: Balance rations using local ingredient prices/nutrients.  
- **Production Tracker**: Log milk/egg yields with CSV exports.  
- **Basic GUI**: PySimpleGUI interface for input/output.  

### Phase 2: Expansion  
- Health Alerts (e.g., vaccination reminders).  
- Feed Inventory Management (stock tracking).  

### Phase 3: Automation  
- Mobile app (Kivy) and IoT sensor integration.  

---

## **Installation**  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/dvozicnivod/agronomix-oss/.git
2. Install dependencies:  
   ```bash 
   pip install -r requirements.txt  
3. Run the GUI:  
   ```bash 
   python src/gui.py   

---

## **Contribution Guidelines**
* **Report Bugs**: Use [GitHub Issues](https://github.com/dvozicnivod/agronomix-oss/issues).
* **Request Features**: Tag issues with `enhancement`.
* **Code Standards**: Follow PEP8 and document functions with docstrings.

---

## **License**
This project is licensed under the **MIT License** - see [LICENSE](./LICENSE) for details.

---
