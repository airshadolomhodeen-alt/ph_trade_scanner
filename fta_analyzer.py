def check_roo_eligibility(fta: str, rvc: int, ctc_changed: bool):
    thresholds = {"RCEP": 40, "ATIGA": 40, "PH-Korea (PKFTA)": 45}
    req_rvc = thresholds.get(fta, 40)
    
    if rvc >= req_rvc or ctc_changed:
        return True, f"RVC threshold of {req_rvc}% met (Actual: {rvc}%) and/or CTC fulfilled."
    else:
        return False, f"RVC of {rvc}% is below the required {req_rvc}% threshold without CTC satisfaction."
