# 🚀 Snabbstart - DonkeyCar Simulator Hybrid

**Kom igång på 5 minuter!**

## 🎮 Installation

### 1. Installera Python-miljö
```bash
# Navigera till mappen
cd docker-simulator

# Skapa virtuell miljö
python -m venv venv

# Aktivera virtuell miljö (VIKTIGT: forward slashes i Git Bash)
source venv/Scripts/activate  # Git Bash
# eller: venv\Scripts\activate  # Command Prompt

# Installera grundläggande verktyg (löser distutils-problem)
pip install setuptools wheel

# Installera beroenden
pip install -r requirements.txt

# Installera gym-donkeycar (använd den lokala kopian)
cd gym-donkeycar
pip install -e .
cd ..
```

### 2. Starta simulatorn
```bash
docker-compose up 
```

### 3. Kör Python-kod (ny terminal)
```bash
# Aktivera virtuell miljö
source venv/Scripts/activate  # eller venv\Scripts\activate på Windows

# Kör exempel
python python_code/example_car_control.py
```

## ✅ Verifiering

Du bör se:
1. **Docker**: Simulator startar och visar 3D-miljö
2. **Python**: "Ansluter till DonkeyCar simulator..." följt av "Simulator ansluten!"

## 🔧 Vanliga problem

### Python kan inte ansluta
- Vänta 10 sekunder efter Docker-start
- Kontrollera: `docker-compose ps`

### Simulator visas inte
- **Windows**: Starta VcXsrv/Xming
- **macOS**: Starta XQuartz
- **Linux**: Kontrollera X11

### Beroenden misslyckas
```bash
pip install --upgrade "pip<24.1"
pip install -r requirements.txt
```

## 📖 Mer information

Se `README.md` för fullständig dokumentation!
