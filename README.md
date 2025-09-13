# Minimal DonkeyCar Simulator Setup för Python-programmering

Detta är en förenklad version av DonkeyCar-simulatorn som är optimerad för att programmera din egen bil-kontroll i Python, utan AI-träning eller webbgränssnitt.

## Vad som ingår:
- **DonkeyCar Simulator** - Den grafiska 3D-simulatorn
- **gym-donkeycar** - Python-bibliotek för att kommunicera med simulatorn
- **Minimal Python-miljö** - För att skriva din egen bil-kontroll

## Vad som är borttaget:
- Webbgränssnitt (ingen port 8887)
- AI-träning och TensorFlow
- Datalagring för träningsdata
- Komplex DonkeyCar-konfiguration

## Systemkrav

### Windows:
- Docker Desktop
- X11 server (VcXsrv eller Xming) för att visa simulatorn

### macOS:
- Docker Desktop
- XQuartz för X11-stöd

### Linux:
- Docker Engine
- X11 forwarding (vanligtvis redan konfigurerat)

## Hur du kör det:

1. **Starta setupen:**
```bash
docker-compose up --build
```

2. **Vänta tills båda containrarna är igång** (du bör se meddelandet "Python client container started successfully")

3. **Kör ditt Python-program i en ny terminal:**
```bash
# Öppna en terminal i Python-containern
docker-compose exec python-client bash

# Kör exempel-programmet
python3 example_car_control.py
```

4. **Alternativt, kör direkt utan att gå in i containern:**
```bash
docker-compose exec python-client python3 example_car_control.py
```

## Programmera din egen bil:

1. **Redigera filen `python_code/example_car_control.py`** eller skapa nya Python-filer i `python_code/`-mappen

2. **Grundläggande API:**
```python
import gym
import gym_donkeycar

# Anslut till simulatorn
env = gym.make("donkey-generated-track-v0", host="donkey-sim", port=9091)

# Återställ miljön
obs = env.reset()  # obs är en kamerabild (numpy array)

# Kontrollera bilen
steering = 0.0    # -1.0 (vänster) till 1.0 (höger)
throttle = 0.3    # -1.0 (bakåt) till 1.0 (framåt)
action = [steering, throttle]

# Skicka kommando och få respons
obs, reward, done, info = env.step(action)
```

3. **Kameradatan:**
   - `obs` är en numpy array med bilden från bilens kamera
   - Storlek: (120, 160, 3) - RGB-bild
   - Du kan använda OpenCV eller andra bildbehandlingsbibliotek för att analysera bilden

## Exempel på vad du kan programmera:

- **Enkel linjeföljning** - Analysera kamerabilden för att hitta vägen
- **Hinderundvikande** - Upptäck objekt och styr runt dem
- **Hastighetskontroll** - Anpassa hastigheten baserat på kurvighet
- **Egen AI-algoritm** - Implementera din egen beslutslogik

## Felsökning:

- Om simulatorn inte visas, kontrollera att X11-servern körs
- Om Python-programmet inte kan ansluta, vänta några sekunder efter att containrarna startat
- Loggar visas med: `docker-compose logs`
