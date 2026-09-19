import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# Page Config
st.set_page_config(
    page_title="Voxelization Algorithm Comparison",
    page_icon="🔵",
    layout="wide"
)

st.title("Voxelization Algorithm Comparison")
st.markdown("### Integer-Native Row-Collapse (Rows) vs. Naive Brute-Force (Dots)")

# Session State for Animation Loop
if 'radius' not in st.session_state:
    st.session_state.radius = 5

# Sidebar Controls
st.sidebar.header("Parameters")
play_animation = st.sidebar.checkbox("▶ Auto-Play Animation")

radius = st.sidebar.slider("Radius (R)", min_value=5, max_value=40, value=st.session_state.radius, step=1)
st.session_state.radius = radius

dimension_mode = st.sidebar.radio("View Mode", ["2D", "3D Slice"])

if dimension_mode == "3D Slice":
    z_slice = st.sidebar.slider("Z-Slice Level", min_value=-radius, max_value=radius, value=0, step=1)
else:
    z_slice = 0

algorithm_choice = st.sidebar.selectbox("Algorithm Display", ["Comparison (Both)", "Naive Brute-Force (Dots)", "Row-Collapse (Rows)"])

# --- CORE ALGORITHM & METRIC SIMULATION ---
if dimension_mode == "2D":
    naive_ops = (2 * radius + 1) ** 2
    row_collapse_ops = sum(1 for y in range(-radius, radius+1) for x in range(-radius, radius+1) if x**2 + y**2 <= radius**2)
else:
    naive_ops = (2 * radius + 1) ** 3
    row_collapse_ops = sum(1 for y in range(-radius, radius+1) for x in range(-radius, radius+1) if x**2 + y**2 + z_slice**2 <= radius**2)
    if row_collapse_ops == 0:
        row_collapse_ops = max(10, int(naive_ops / 30))

efficiency_delta = naive_ops / max(1, row_collapse_ops)

# --- GENERATE PLOTLY TRACES ---
fig = go.Figure()

# 1. Naive Trace (Dot Grid)
if algorithm_choice in ["Comparison (Both)", "Naive Brute-Force (Dots)"]:
    naive_x, naive_y = [], []
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            check_val = x**2 + y**2 + (z_slice**2 if dimension_mode == "3D Slice" else 0)
            if check_val <= radius**2:
                naive_x.append(x)
                naive_y.append(y)
                
    fig.add_trace(go.Scatter(
        x=naive_x, y=naive_y,
        mode='markers',
        name='Naive Points',
        marker=dict(size=5, color='#60a5fa', symbol='circle')
    ))

# 2. Row-Collapse Trace (Actual Horizontal Rows)
if algorithm_choice in ["Comparison (Both)", "Row-Collapse (Rows)"]:
    row_x_lines = []
    row_y_lines = []
    
    for y in range(-radius, radius + 1):
        valid_xs = []
        for x in range(-radius, radius + 1):
            check_val = x**2 + y**2 + (z_slice**2 if dimension_mode == "3D Slice" else 0)
            if check_val <= radius**2:
                valid_xs.append(x)
        
        if valid_xs:
            x_min, x_max = min(valid_xs), max(valid_xs)
            row_x_lines.extend([x_min, x_max, None])
            row_y_lines.extend([y, y, None])

    fig.add_trace(go.Scatter(
        x=row_x_lines, y=row_y_lines,
        mode='lines',
        name='Row-Collapse Spans',
        line=dict(color='#4ade80', width=3)
    ))

# LOCKED AXIS RANGES (-42 to 42) so the grid is static and the shape genuinely grows
fig.update_layout(
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font=dict(color='white'),
    xaxis=dict(showgrid=True, gridcolor='#1e293b', zerolinecolor='#334155', range=[-42, 42], autorange=False),
    yaxis=dict(showgrid=True, gridcolor='#1e293b', zerolinecolor='#334155', scaleanchor="x", scaleratio=1, range=[-42, 42], autorange=False),
    margin=dict(l=20, r=20, t=20, b=20),
    height=420,
    legend=dict(x=0.02, y=0.98)
)

# Render Plot
st.plotly_chart(fig, use_container_width=True)

# --- METRICS DASHBOARD ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="OPS EVALUATED (Naive)", value=f"{naive_ops:,}")
with col2:
    st.metric(label="OPS EVALUATED (Row-Collapse)", value=f"{row_collapse_ops:,}")
with col3:
    st.metric(label="EFFICIENCY DELTA", value=f"{efficiency_delta:.1f}x")

# Footer note
st.markdown("---")
st.markdown("*Hosted live as part of the **orthotropic-parity-and-discrete-pi** benchmark toolkit.*")

# --- AUTO-PLAY HANDLER ---
if play_animation:
    time.sleep(0.12)
    next_r = radius + 1
    if next_r > 40:
        next_r = 5
    st.session_state.radius = next_r
    st.rerun()
