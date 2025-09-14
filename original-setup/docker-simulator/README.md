# DonkeyCar Simulator - Hybrid Setup

Detta är en **hybrid-lösning** där DonkeyCar-simulatorn körs i Docker men Python-utvecklingsmiljön körs lokalt på din dator. Detta ger dig det bästa av båda världar:

- ✅ **Snabb Python-utveckling** - Ingen container overhead
- ✅ **Enkel debugging** - Använd din vanliga IDE och debugger
- ✅ **Isolerad simulator** - Simulatorn körs säkert i Docker
- ✅ **Enkel installation** - Minimal setup krävs

## 🚀 Snabbstart

### 1. Förutsättningar

#### Windows:
- Docker Desktop
- Python 3.9+ installerat lokalt
- X11 server (VcXsrv eller Xming) för att visa simulatorn

#### macOS:
- Docker Desktop
- Python 3.9+ installerat lokalt
- XQuartz för X11-stöd

#### Linux:
- Docker Engine
- Python 3.9+ installerat lokalt
- X11 forwarding (vanligtvis redan konfigurerat)

### 2. Installation

#### Steg 1: Navigera till mappen
```bash
cd docker-simulator
```

#### Steg 2: Installera lokala Python-beroenden
```bash
# Skapa virtuell miljö
python -m venv venv

# Aktivera virtuell miljö (VIKTIGT: använd forward slashes i Git Bash)
source venv/Scripts/activate  # Git Bash
# eller: venv\Scripts\activate  # Command Prompt

# Installera grundläggande verktyg (löser distutils-problem i Python 3.13+)
pip install setuptools wheel

# Installera beroenden
pip install -r requirements.txt

# Installera gym-donkeycar (använd den lokala kopian)
cd gym-donkeycar
pip install -e .
cd ..
```

#### Steg 3: Starta simulatorn i Docker
```bash
# Bygg och starta simulator-containern
docker-compose up --build
```

#### Steg 4: Kör Python-koden lokalt (i ny terminal)
```bash
# Aktivera virtuell miljö (VIKTIGT: forward slashes i Git Bash)
source venv/Scripts/activate  # Git Bash

# Kör exempel-programmet
python python_code/example_car_control.py
```

## 🎮 Användning

### Grundläggande körning:
1. **Terminal 1**: `docker-compose up` (håll igång)
2. **Terminal 2**: `python python_code/example_car_control.py`

### Utveckling:
- Redigera filer i `python_code/` mappen med din vanliga editor/IDE
- Kör Python-koden direkt utan att bygga om containers
- Simulatorn behöver bara startas om vid Docker-ändringar

## 💻 Programmering

### API-referens:
```python
import gym
import gym_donkeycar

# Anslut till simulatorn (körs i Docker på localhost:9091)
conf = {
    "host": "localhost",  # VIKTIGT: localhost, inte "donkey-sim"
    "port": 9091,
    "start_delay": 5.0,
    "max_cte": 8.0,
    "frame_skip": 1,
    "cam_resolution": (120, 160, 3),
    "log_level": 20,
    "steer_limit": 1.0,
    "throttle_min": 0.0,
    "throttle_max": 1.0
}

env = gym.make("donkey-generated-track-v0", conf=conf)

# Återställ miljön
obs = env.reset()  # obs är en kamerabild (numpy array)

# Kontrollera bilen
steering = 0.0    # -1.0 (vänster) till 1.0 (höger)
throttle = 0.3    # -1.0 (bakåt) till 1.0 (framåt)
action = [steering, throttle]

# Skicka kommando och få respons
obs, reward, done, info = env.step(action)
```

### Kameradatan:
- `obs` är en numpy array med bilden från bilens kamera
- Storlek: (120, 160, 3) - RGB-bild
- Använd OpenCV eller andra bildbehandlingsbibliotek för analys

### Exempel på AI-logik:
```python
# Enkel linjeföljning baserat på kamerabild
def calculate_steering(obs):
    # Konvertera till gråskala
    gray = cv2.cvtColor(obs, cv2.COLOR_RGB2GRAY)
    
    # Hitta vägen (enkel implementation)
    # ... din logik här ...
    
    return steering_value

# I huvudloopen:
steering = calculate_steering(obs)
throttle = 0.3
action = [steering, throttle]
```

## 🔧 Felsökning

### Problem: Python kan inte ansluta till simulatorn
**Lösning:**
1. Kontrollera att Docker-containern körs: `docker-compose ps`
2. Vänta 5-10 sekunder efter att containern startat
3. Kontrollera att port 9091 är tillgänglig: `netstat -an | grep 9091`

### Problem: Simulatorn visas inte
**Lösning:**
1. **Windows**: Starta VcXsrv eller Xming
2. **macOS**: Starta XQuartz
3. **Linux**: Kontrollera X11 forwarding

### Problem: Python-beroenden fungerar inte
**Lösning:**
```bash
# Använd kompatibel pip-version
pip install --upgrade "pip<24.1"

# Installera beroenden i rätt ordning
pip install "numpy<2.0"
pip install opencv-python-headless==4.5.3.56
pip install pillow==8.3.2
pip install gym==0.25.2
pip install websocket-client==1.2.1
pip install msgpack==1.0.2
```

### Problem: gym-donkeycar installation misslyckas
**Lösning:**
```bash
# Installera systempaket (Ubuntu/Debian)
sudo apt-get install git build-essential cmake swig

# Eller på macOS
brew install cmake swig

# Sedan installera gym-donkeycar (använd den lokala kopian)
cd gym-donkeycar
pip install -e .
cd ..
```

## 📋 Docker-kommandon

```bash
# Starta simulator
docker-compose up --build

# Starta i bakgrunden
docker-compose up --build -d

# Stoppa simulator
docker-compose down

# Se loggar
docker-compose logs

# Följ loggar live
docker-compose logs -f

# Kontrollera status
docker-compose ps

# Bygga om efter ändringar
docker-compose up --build --force-recreate
```

## 🎯 Projektstruktur

```
docker-simulator/
├── docker-compose.yml          # Docker konfiguration
├── Dockerfile                  # Simulator container
├── requirements.txt            # Lokala Python-beroenden
├── README.md                   # Denna fil
└── python_code/               # Din Python-kod (körs lokalt)
    └── example_car_control.py  # Exempel-program
```

## ✅ Fördelar med Hybrid Setup

- **Snabbare utveckling**: Ingen container overhead för Python-kod
- **Bättre debugging**: Använd din vanliga IDE och debugger
- **Enklare installation**: Färre Docker-containers att hantera
- **Flexibilitet**: Lätt att byta mellan olika Python-versioner
- **IDE-integration**: Full support för code completion, linting, etc.

## 🔄 Jämförelse med andra setups

| Setup | Simulator | Python | Fördelar | Nackdelar |
|-------|-----------|--------|----------|-----------|
| **Hybrid** (denna) | Docker | Lokalt | Snabb utveckling, enkel debugging | Kräver lokal Python-installation |
| **Full Docker** | Docker | Docker | Helt isolerat, konsistent miljö | Långsammare, svårare debugging |
| **Lokal** | Lokalt | Lokalt | Snabbast | Komplicerad installation, miljöproblem |

## 📚 Resurser

- **gym-donkeycar GitHub**: [https://github.com/tawnkramer/gym-donkeycar](https://github.com/tawnkramer/gym-donkeycar)
- **DonkeyCar Documentation**: [https://docs.donkeycar.com/](https://docs.donkeycar.com/)
- **Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)

## 🤝 Bidrag

Har du förbättringar eller hittat buggar? Skapa gärna en issue eller pull request!
