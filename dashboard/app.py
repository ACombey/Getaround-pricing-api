import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Getaround Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Getaround - Analyse du délai minimum entre locations")
st.markdown("---")

st.sidebar.header("⚙️ Paramètres")
threshold = st.sidebar.slider(
    "Délai minimum (minutes)",
    min_value=0,
    max_value=720,
    value=120,
    step=30
)

scope = st.sidebar.radio(
    "Scope d'application",
    ["Toutes les voitures", "Uniquement Connect", "Uniquement Mobile"]
)

st.info("⚠️ Dashboard de démo - Remplace par tes vraies données issues de l'EDA")

n_rentals = 1000
demo_data = pd.DataFrame({
    'rental_id': range(n_rentals),
    'delay_minutes': np.random.exponential(60, n_rentals),
    'checkin_type': np.random.choice(['connect', 'mobile'], n_rentals),
    'revenue': np.random.normal(100, 30, n_rentals),
    'is_late': np.random.choice([True, False], n_rentals, p=[0.3, 0.7])
})

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total locations", f"{len(demo_data):,}")

with col2:
    affected = len(demo_data[demo_data['delay_minutes'] < threshold])
    pct = (affected / len(demo_data)) * 100
    st.metric("Locations affectées", f"{affected:,}", delta=f"{pct:.1f}%")

with col3:
    late_rentals = demo_data['is_late'].sum()
    st.metric("Retards de checkout", f"{late_rentals:,}")

with col4:
    potential_loss = demo_data[demo_data['delay_minutes'] < threshold]['revenue'].sum()
    st.metric("Revenu potentiel affecté", f"{potential_loss:,.0f}€")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribution des délais entre locations")
    fig1 = px.histogram(demo_data, x='delay_minutes', nbins=50)
    fig1.add_vline(x=threshold, line_dash="dash", line_color="red")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🔌 Répartition par type de checkin")
    checkin_counts = demo_data['checkin_type'].value_counts()
    fig2 = px.pie(values=checkin_counts.values, names=checkin_counts.index)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.caption("Dashboard créé avec Streamlit")
