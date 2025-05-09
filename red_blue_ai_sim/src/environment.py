class Host:
    def __init__(self, name):
        self.name = name
        self.is_compromised = False
        self.services = ["ssh", "http", "ftp"]
        self.logs = []

    def receive_attack(self, service, attacker_ip):
        log_entry = f"Attack on {service} from {attacker_ip}"
        self.logs.append(log_entry)
        if service == "ssh":
            self.is_compromised = True
        return log_entry

    def clear_logs(self):
        self.logs = []

class SimulationEnvironment:
    def __init__(self, red_team_ip="192.168.1.100"):
        self.hosts = [Host("WebServer"), Host("DBServer"), Host("MailServer")]
        self.red_team_ip = red_team_ip
        self.blue_alerts = []

    def simulate_step(self, red_action, blue_action):
        host = self.hosts[red_action['target']]
        attack_log = host.receive_attack(red_action['service'], self.red_team_ip)
        self.blue_alerts.append(blue_action(host))
        return attack_log
