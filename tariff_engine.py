import requests

def search_ahtn_database(query: str):
    """
    Searchable AHTN-2022 product catalog matching PTF and FTAOMS frameworks.
    """
    mock_ahtn_catalog = [
        {"code": "8542.31", "description": "Electronic integrated circuits: Processors and controllers", "mfn": 3.0, "atiga": 0.0, "rcep": 0.0, "pkfta": 0.0, "pjepa": 0.0},
        {"code": "0803.90", "description": "Bananas, including plantains, fresh or dried", "mfn": 7.0, "atiga": 0.0, "rcep": 5.0, "pkfta": 3.0, "pjepa": 0.0},
        {"code": "8703.23", "description": "Motor cars and other motor vehicles principally designed for transport of persons", "mfn": 20.0, "atiga": 0.0, "rcep": 5.0, "pkfta": 5.0, "pjepa": 0.0},
        {"code": "2401.10", "description": "Tobacco, not stemmed or stripped (Unmanufactured tobacco)", "mfn": 50.0, "atiga": 0.0, "rcep": 10.0, "pkfta": 20.0, "pjepa": 10.0},
        {"code": "7108.12", "description": "Gold in non-monetary forms", "mfn": 1.0, "atiga": 0.0, "rcep": 0.0, "pkfta": 0.0, "pjepa": 0.0}
    ]
    
    query_lower = query.lower()
    results = [
        item for item in mock_ahtn_catalog 
        if query_lower in item["code"].lower() or query_lower in item["description"].lower()
    ]
    return results if results else mock_ahtn_catalog
