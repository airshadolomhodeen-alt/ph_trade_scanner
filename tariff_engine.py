def search_ahtn_database(query):
    """Searches the AHTN-2022 product nomenclature and tariff database."""
    database = [
        {"HS Code": "8542.31", "Description": "Monolithic integrated circuits as processors and controllers", "MFN Rate (%)": "0%", "FTA Preferential Rate (%)": "0% (ATIGA / ACFTA / AJCEP)", "Export Potential": "Very High"},
        {"HS Code": "8544.30", "Description": "Ignition wiring sets and other wiring sets for vehicles, aircraft or ships", "MFN Rate (%)": "1%", "FTA Preferential Rate (%)": "0% (PJEPA / AKFTA)", "Export Potential": "High"},
        {"HS Code": "1513.11", "Description": "Crude coconut (copra) oil and its fractions", "MFN Rate (%)": "7%", "FTA Preferential Rate (%)": "0% (ASEAN / Japan / Korea)", "Export Potential": "Dominant Global Share"},
        {"HS Code": "0803.90", "Description": "Fresh or dried bananas including plantains", "MFN Rate (%)": "15%", "FTA Preferential Rate (%)": "5% or 0% under AJCEP/AKFTA", "Export Potential": "High Regional Demand"},
        {"HS Code": "1604.14", "Description": "Prepared or preserved tunas, skipjack and bonito (whole or in pieces)", "MFN Rate (%)": "5%", "FTA Preferential Rate (%)": "0% (GSP+ / Bilateral FTAs)", "Export Potential": "Stable Growth"},
        {"HS Code": "8471.30", "Description": "Portable automatic data processing machines (laptops and tablets)", "MFN Rate (%)": "0%", "FTA Preferential Rate (%)": "0% (ITA / ATIGA)", "Export Potential": "Expanding Tech Assembly"}
    ]
    q = query.lower()
    return [item for item in database if q in item["HS Code"].lower() or q in item["Description"].lower()]
