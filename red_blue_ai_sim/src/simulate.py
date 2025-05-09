import sys
import os

# Adjust import path
current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
sys.path.insert(0, current_dir)

from environment import SimulationEnvironment
from red_team_ai import RedTeamAI
from blue_team_ai import BlueTeamAI

# Ask user for Red Team IP
ip_address = input("Enter Red Team IP address (default: 192.168.1.100): ").strip()
if not ip_address:
    ip_address = "192.168.1.100"

env = SimulationEnvironment(red_team_ip=ip_address)
red_ai = RedTeamAI()
blue_ai = BlueTeamAI()

for step in range(5):
    print(f"\n--- Simulation Step {step + 1} ---")
    red_action = red_ai.choose_action(env)
    log = env.simulate_step(red_action, blue_ai.detect_intrusion)
    print("RedTeam Log:", log)
    for alert in env.blue_alerts:
        print("BlueTeam Response:", alert)
