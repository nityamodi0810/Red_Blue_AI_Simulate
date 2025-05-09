def log_event(message):
    with open("simulation_log.txt", "a") as f:
        f.write(message + "\n")

def print_metrics(env):
    compromised = [h.name for h in env.hosts if h.is_compromised]
    print("\nCompromised Hosts:", compromised if compromised else "None")
    print("Total Blue Team Alerts:", len(env.blue_alerts))
