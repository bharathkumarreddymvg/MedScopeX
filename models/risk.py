import random

class RiskModel:
    def __call__(self, cavity_percent, depth_stage):
        score = cavity_percent * 0.4 + depth_stage * 10 + random.uniform(-2, 2)
        return round(min(max(score, 0), 100), 2)
