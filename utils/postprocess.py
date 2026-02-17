DEPTH_MAP = {
    0: "Enamel (Early-stage decay)",
    1: "Dentin (Moderate decay)",
    2: "Deep Caries",
    3: "Pulp Exposure"
}

def interpret_dental(cavity, depth_stage, risk):
    if risk < 20:
        action = "Maintain oral hygiene and routine check-up"
    elif risk < 40:
        action = "Preventive dental care recommended"
    elif risk < 60:
        action = "Dental consultation advised within 2-4 weeks"
    elif risk < 80:
        action = "Urgent dental visit recommended"
    else:
        action = "Immediate dental intervention required"

    return {
        "cavity_percent": cavity,
        "depth": DEPTH_MAP[depth_stage],
        "risk": risk,
        "recommendation": action
    }
