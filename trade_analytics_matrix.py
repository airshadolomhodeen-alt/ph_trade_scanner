import pandas as pd

class TradeAnalyticsMatrix:
    def __init__(self):
        # Top 20 Philippine Export Destinations (PSA & WITS baseline)
        self.top_export_partners = [
            {"Rank": 1, "Market": "United States (USA)", "Share": "~16.0%", "Primary Sectors": "Electronics, Machineries, Agro-products"},
            {"Rank": 2, "Market": "Japan (JPN)", "Share": "~14.0%", "Primary Sectors": "Semiconductors, Ignition Wiring, Bananas"},
            {"Rank": 3, "Market": "Mainland China (CHN)", "Share": "~13.0%", "Primary Sectors": "Ores, Copper, Electrical Equipment"},
            {"Rank": 4, "Market": "Hong Kong (HKG)", "Share": "~12.0%", "Primary Sectors": "Integrated Circuits, Transistors"},
            {"Rank": 5, "Market": "Singapore (SGP)", "Share": "~5.8%", "Primary Sectors": "Refined Petroleum, Electronics"},
            {"Rank": 6, "Market": "Thailand (THA)", "Share": "~4.0%", "Primary Sectors": "Automotive Components, Integrated Circuits"},
            {"Rank": 7, "Market": "Germany (DEU)", "Share": "~3.8%", "Primary Sectors": "Electrical Machinery, Medical Instruments"},
            {"Rank": 8, "Market": "South Korea (KOR)", "Share": "~3.6%", "Primary Sectors": "Copper Concentrates, Electronic Parts"},
            {"Rank": 9, "Market": "Netherlands (NLD)", "Share": "~3.1%", "Primary Sectors": "Processors, Office Machine Parts"},
            {"Rank": 10, "Market": "Malaysia (MYS)", "Share": "~2.6%", "Primary Sectors": "Semiconductors, Petroleum Oils"},
            {"Rank": 11, "Market": "Taiwan (TWN)", "Share": "~2.4%", "Primary Sectors": "Integrated Microcircuits, Diodes"},
            {"Rank": 12, "Market": "Vietnam (VNM)", "Share": "~2.1%", "Primary Sectors": "Electronic Components, Cereals"},
            {"Rank": 13, "Market": "Australia (AUS)", "Share": "~1.4%", "Primary Sectors": "Gold, Machinery, Prepared Foods"},
            {"Rank": 14, "Market": "United Kingdom (GBR)", "Share": "~1.1%", "Primary Sectors": "Machinery, Electrical Equipment"},
            {"Rank": 15, "Market": "France (FRA)", "Share": "~0.9%", "Primary Sectors": "Aerospace Components, Electronics"},
            {"Rank": 16, "Market": "Canada (CAN)", "Share": "~0.7%", "Primary Sectors": "Insulated Wire, Electronic Parts"},
            {"Rank": 17, "Market": "Italy (ITA)", "Share": "~0.6%", "Primary Sectors": "Apparel, Machinery, Footwear"},
            {"Rank": 18, "Market": "Switzerland (CHE)", "Share": "~0.5%", "Primary Sectors": "Watches, Precision Instruments, Gold"},
            {"Rank": 19, "Market": "India (IND)", "Share": "~0.5%", "Primary Sectors": "Chemicals, Electronics, Copper"},
            {"Rank": 20, "Market": "Indonesia (IDN)", "Share": "~0.4%", "Primary Sectors": "Tobacco, Animal Feeds, Machinery"}
        ]
        
        # Top 20 Philippine Import Origins (PSA & WITS baseline)
        self.top_import_partners = [
            {"Rank": 1, "Market": "Mainland China (CHN)", "Share": "~23.0%", "Primary Sectors": "Industrial Machinery, Electronics, Iron/Steel"},
            {"Rank": 2, "Market": "Japan (JPN)", "Share": "~11.5%", "Primary Sectors": "Specialized Machinery, Transport Parts, Steel"},
            {"Rank": 3, "Market": "South Korea (KOR)", "Share": "~8.5%", "Primary Sectors": "Refined Petroleum, Semiconductors, Parts"},
            {"Rank": 4, "Market": "Indonesia (IDN)", "Share": "~8.0%", "Primary Sectors": "Coal, Mineral Fuels, Automotive, Palm Oil"},
            {"Rank": 5, "Market": "United States (USA)", "Share": "~7.3%", "Primary Sectors": "Cereals, Electronic Components, Aircraft"},
            {"Rank": 6, "Market": "Thailand (THA)", "Share": "~6.8%", "Primary Sectors": "Motor Vehicles, Plastic Materials, Rice"},
            {"Rank": 7, "Market": "Singapore (SGP)", "Share": "~6.0%", "Primary Sectors": "Petroleum Products, Electronic Integrated Circuits"},
            {"Rank": 8, "Market": "Malaysia (MYS)", "Share": "~5.2%", "Primary Sectors": "Electrical Equipment, Mineral Fuels, Plastics"},
            {"Rank": 9, "Market": "Vietnam (VNM)", "Share": "~4.1%", "Primary Sectors": "Cereals (Rice), Iron and Steel, Electronics"},
            {"Rank": 10, "Market": "Taiwan (TWN)", "Share": "~3.8%", "Primary Sectors": "Integrated Circuits, Machinery, Plastics"},
            {"Rank": 11, "Market": "Saudi Arabia (SAU)", "Share": "~2.5%", "Primary Sectors": "Crude Petroleum Oils"},
            {"Rank": 12, "Market": "United Arab Emirates (ARE)", "Share": "~2.0%", "Primary Sectors": "Petroleum Oils, Gold, Unwrought Metals"},
            {"Rank": 13, "Market": "Germany (DEU)", "Share": "~1.8%", "Primary Sectors": "Motor Vehicles, Pharmaceuticals, Machinery"},
            {"Rank": 14, "Market": "Australia (AUS)", "Share": "~1.5%", "Primary Sectors": "Meat, Wheat, Ores, Metal Scrap"},
            {"Rank": 15, "Market": "Switzerland (CHE)", "Share": "~1.2%", "Primary Sectors": "Jewelry, Pharmaceuticals, Clocks/Watches"},
            {"Rank": 16, "Market": "India (IND)", "Share": "~1.1%", "Primary Sectors": "Pharmaceuticals, Bovine Meat, Organic Chemicals"},
            {"Rank": 17, "Market": "Hong Kong (HKG)", "Share": "~1.0%", "Primary Sectors": "Electrical Machinery, Integrated Circuits"},
            {"Rank": 18, "Market": "Italy (ITA)", "Share": "~0.8%", "Primary Sectors": "Specialized Machinery, Industrial Components"},
            {"Rank": 19, "Market": "France (FRA)", "Share": "~0.7%", "Primary Sectors": "Pharmaceutical Products, Aerospace Parts"},
            {"Rank": 20, "Market": "United Kingdom (GBR)", "Share": "~0.6%", "Primary Sectors": "Power-generating Machinery, Medicaments"}
        ]

    def get_export_df(self):
        return pd.DataFrame(self.top_export_partners)

    def get_import_df(self):
        return pd.DataFrame(self.top_import_partners)
