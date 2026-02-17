def compute_risk(cavity_pct, depth_stage, gum_score):
    return min(100, cavity_pct * 0.4 + depth_stage * 20 + gum_score * 0.2)
