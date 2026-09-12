with tab2:
    st.header("AHTN-2022 Product & Tariff Finder (PTF / FTAOMS Style)")
    st.markdown("Search across the complete global WITS/HS product nomenclature database (8,244+ records).")
    
    search_query = st.text_input("Enter HS Code or Keyword (e.g., 'Live horses', 'Coconut', or '8542')", "Live horses")
    search_results = search_ahtn_database(search_query)
    
    if search_results:
        df_results = pd.DataFrame(search_results)
        st.dataframe(df_results, use_container_width=True, hide_index=True)
    else:
        st.warning(f"⚠️ No matching product found for '{search_query}'. Try a broader keyword like 'Horse', 'Meat', or 'Fish'.")
