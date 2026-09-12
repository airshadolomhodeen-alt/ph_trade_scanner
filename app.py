with tab4:
    st.subheader("Philippine Regional Resource & Industry Cluster Mapping")
    st.markdown("Align your export product lines with regional raw material strengths, Halal trade potential, and investment promotion agencies (PEZA, BOI, BEZA-BARMM).")
    
    region_choice = st.selectbox("Select Philippine Region / Economic Hub", [
        "BARMM (Bangsamoro Autonomous Region) - Halal Agribusiness, Fisheries, Seaweeds & Corn",
        "CALABARZON (Region IV-A) - Electronics, Automotive & Heavy Industries",
        "Davao Region (Region XI) - Agribusiness (Bananas, Coconuts, Cacao, Fruit)",
        "Central Visayas (Region VII / Mactan PEZA) - Aerospace MRO, Electronics & Furniture",
        "Northern Mindanao (Region X) - Coconuts, Steel, Agro-Industrial & Logistics",
        "National Capital Region (NCR) - Global Services, Logistics & Trading HQs",
        "Ilocos Region (Region I) - Mangoes, Tobacco, Renewable Energy & IT-BPM",
        "Cagayan Valley (Region II) - Corn, Legumes, Coffee & High-Value Crops",
        "Central Luzon (Region III / Clark-Subic) - Aviation, Logistics, Electronics & Agribusiness",
        "Western Visayas (Region VI) - Sugar, Renewable Energy, Aqua-marine & Tourism Tech",
        "Eastern Visayas (Region VIII) - Geothermal Energy, Coconut Products & Minerals",
        "Zamboanga Peninsula (Region IX) - Sardines, Rubber, Coconut & Halal Trade",
        "SOCCSKSARGEN (Region XII) - Tuna Capital, Pineapple, Coffee & Palm Oil",
        "Caraga (Region XIII) - Timber, Mining, Aqua-culture & Nickel Processing"
    ])
    
    if "BARMM" in region_choice:
        st.success("""**Key Sectors & Resources:** 
* Halal-certified processed foods, agricultural produce, and ingredients
* High-grade carrageenan (seaweed farming - major global exporter)
* Yellow corn, Robusta coffee, and tropical fruits
* Artisanal fisheries, aquaculture, and cold-chain logistics

**Investment & Trade Agencies:** 
* **Bangsamoro Economic Zone Authority (BEZA-BARMM)** – Establishes and regulates special economic zones, offering fiscal and non-fiscal incentives similar to PEZA.
* **Bangsamoro Board of Investments (BBOI)** and **Ministry of Trade, Investments and Tourism (MTIT-BARMM)**.

**Export Advantages & Markets:** Strategic participation in the **BIMP-EAGA (Brunei-Indonesia-Malaysia-Philippines East ASEAN Growth Area)** and expanding Halal-compliant trade channels across the Middle East, North Africa (MENA), and Southeast Asia.""")
    elif "CALABARZON" in region_choice:
        st.success("**Key Sectors:** Semiconductor assembly, automotive wiring, electrical machinery.\n\n**Investment Agencies:** PEZA, BOI\n\n**Major Economic Zones:** Laguna Technopark, Gateway Business Park, Lima Technology Center.")
    elif "Davao" in region_choice:
        st.success("**Key Sectors:** Cavendish bananas, fresh pineapples, coconut products, cacao.\n\n**Investment Agencies:** MinDA, BOI, DTI-XI\n\n**Export Destinations:** Japan, China, Middle East, South Korea.")
    elif "Visayas" in region_choice:
        st.success("**Key Sectors:** MRO aerospace parts, electronics manufacturing, furniture, tourism tech.\n\n**Investment Agencies:** Mactan Export Processing Zone (MEPZ), Cebu CFI.\n\n**Export Destinations:** USA, EU, Japan.")
    elif "Mindanao" in region_choice:
        st.success("**Key Sectors:** Crude coconut oil, copra cake, steel manufacturing, processed fruit.\n\n**Investment Agencies:** PHividec Industrial Estate, BOI.\n\n**Export Destinations:** Europe, USA, ASEAN neighbors.")
    elif "SOCCSKSARGEN" in region_choice:
        st.success("**Key Sectors:** Tuna processing (General Santos City is the Tuna Capital), canned goods, pineapples, Cavendish bananas, palm oil.\n\n**Investment Agencies:** BOI, DTI-XII, General Santos City Investment Promotion Center.\n\n**Export Destinations:** USA, Europe, Japan, Middle East.")
    elif "Zamboanga" in region_choice:
        st.success("**Key Sectors:** Sardine manufacturing (Zamboanga City is the sardine capital), rubber production, seaweeds, coconut.\n\n**Investment Agencies:** DTI-IX, Zamboanga Economic Zone (ZAMECOZONE).\n\n**Export Destinations:** ASEAN, USA, Middle East.")
    else:
        st.success(f"**Selected Hub:** {region_choice}\n\n**Strategic Focus:** Regional commodity integration, domestic distribution, and value-chain processing for international export compliance.")
