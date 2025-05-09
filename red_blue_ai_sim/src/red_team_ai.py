import random

class RedTeamAI:
    def choose_action(self, env):
        target_index = random.randint(0, len(env.hosts) - 1)
        service = random.choice(env.hosts[target_index].services)
        return {"target": target_index, "service": service}
