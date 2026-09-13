from providers.comtrade_provider import ComtradeProvider

class OpportunityEngine:
    def __init__(self):
        self.comtrade = ComtradeProvider()

    def calculate_opportunity_score(self, tariff_margin: float, market_size: float):
        score = min(100.0, (tariff_margin * 3.5) + (market_size / 1000000.0 * 0.1))
        return round(score, 2)

class OriginEngine:
    def __init__(self):
        pass

    def calculate_rvc_fob(self, fob_value: float, non_originating_value: float):
        if fob_value <= 0:
            return {"rvc_percentage": 0.0, "threshold": 40.0, "passed": False, "status": "INVALID FOB"}
        
        rvc = ((fob_value - non_originating_value) / fob_value) * 100.0
        rvc_round = round(rvc, 2)
        threshold = 40.0
        
        return {
            "rvc_percentage": rvc_round,
            "threshold": threshold,
            "passed": rvc_round >= threshold,
            "status": "QUALIFIED" if rvc_round >= threshold else "UNQUALIFIED"
        }
