class OriginEngine:
    def calculate_rvc_fob(self, fob_value: float, non_originating_cif: float) -> dict:
        if fob_value <= 0:
            return {
                "rvc_percentage": 0.0,
                "passed": False,
                "error": "FOB export value must be greater than zero."
            }

        rvc = ((fob_value - non_originating_cif) / fob_value) * 100.0
        rvc = round(rvc, 2)
        passed = rvc >= 40.0

        return {
            "fob_value": fob_value,
            "non_originating_cif": non_originating_cif,
            "rvc_percentage": rvc,
            "threshold_required": 40.0,
            "passed": passed
        }


class OpportunityEngine:
    def analyze_bilateral_potential(self, reporter_iso: str, partner_iso: str, hs_code: str) -> dict:
        return {
            "reporter": reporter_iso,
            "partner": partner_iso,
            "product_code": hs_code,
            "export_potential_score": "High (Top 15% Priority Sector)",
            "tariff_advantage": "Active preferential margin available",
            "recommendation": "Proceed with commercial shipment and secure preferential Certificate of Origin."
        }
