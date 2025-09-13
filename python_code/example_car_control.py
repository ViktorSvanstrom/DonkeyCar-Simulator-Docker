#!/usr/bin/env python3
"""
Exempel på hur du styr en DonkeyCar i simulatorn med Python
Detta är en minimal implementation som visar grunderna
"""

import gym
import gym_donkeycar
import numpy as np
import time
import os

def main():
    print("Ansluter till DonkeyCar simulator...")
    
    # Skapa miljön för DonkeyCar simulatorn med korrekt konfiguration
    # gym-donkeycar använder conf-parametrar för att konfigurera anslutningen
    conf = {
        "host": "donkey-sim",
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
    
    try:
        env = gym.make("donkey-generated-track-v0", conf=conf)
        print("Miljö skapad framgångsrikt!")
    except Exception as e:
        print(f"Fel vid skapande av miljö: {e}")
        print("Försöker med alternativ miljö...")
        try:
            env = gym.make("donkey-generated-roads-v0", conf=conf)
            print("Alternativ miljö skapad!")
        except Exception as e2:
            print(f"Kunde inte skapa miljö: {e2}")
            print("Försöker med warehouse miljö...")
            try:
                env = gym.make("donkey-warehouse-v0", conf=conf)
                print("Warehouse miljö skapad!")
            except Exception as e3:
                print(f"Kunde inte skapa någon miljö: {e3}")
                return
    
    # Återställ miljön
    try:
        obs = env.reset()
        print("Simulator ansluten! Börjar köra...")
        print(f"Observation shape: {obs.shape if hasattr(obs, 'shape') else type(obs)}")
    except Exception as e:
        print(f"Fel vid återställning av miljö: {e}")
        return
    
    # Kör i 1000 steg (du kan ändra detta)
    for step in range(1000):
        try:
            # Här programmerar du din egen logik!
            
            # Exempel 1: Kör rakt fram
            steering = 0.0  # -1.0 till 1.0 (vänster till höger)
            throttle = 0.3  # -1.0 till 1.0 (bakåt till framåt)
            
            # Exempel 2: Enkel svänglogik baserat på bildens innehåll
            # Du kan analysera obs (kamerabild) här för att fatta beslut
            
            # Exempel 3: Lägg till din egen AI-logik här
            # if some_condition_based_on_obs:
            #     steering = calculate_steering(obs)
            #     throttle = calculate_throttle(obs)
            
            # Skicka kommandon till bilen
            action = [steering, throttle]
            obs, reward, done, info = env.step(action)
            
            # Visa information varje 50:e steg
            if step % 50 == 0:
                print(f"Steg {step}: Styrning={steering:.2f}, Gas={throttle:.2f}")
                print(f"Belöning: {reward:.2f}")
            
            # Om bilen kraschar eller går av banan
            if done:
                print("Episod avslutad! Återställer...")
                obs = env.reset()
            
            # Liten paus för att inte överbelasta
            time.sleep(0.05)
            
        except Exception as e:
            print(f"Fel under körning: {e}")
            break
    
    print("Klar! Stänger anslutning...")
    try:
        env.close()
    except:
        pass

if __name__ == "__main__":
    main()
