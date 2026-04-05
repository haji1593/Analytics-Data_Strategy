"""
Enterprise Data Strategy Dashboard
Predicting and Reducing First-Year Student Dropout
Private Higher-Education Institution | OMIS 407
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# ────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# ────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Enterprise Data Strategy | Student Retention Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ────────────────────────────────────────────────────────────────────
# PROFESSIONAL COLOR PALETTE
# ────────────────────────────────────────────────────────────────────
# Light theme - board-room ready
BG_MAIN    = "#ffffff"
BG_LIGHT   = "#f8fafb"
BG_CARD    = "#ffffff"
BORDER     = "#e0e6ed"
BORDER_LT  = "#f0f3f7"

# Professional corporate colors
PRIMARY    = "#1e5a9e"      # Deep professional blue
PRIMARY_LT = "#2874c5"
ACCENT     = "#e8994f"      # Warm professional orange
SUCCESS    = "#2d8b4a"      # Professional green
DANGER     = "#c84c3c"      # Professional red
WARNING    = "#d9943a"      # Professional amber
INFO       = "#5b8ac5"      # Professional info blue
NEUTRAL    = "#6b778c"      # Professional gray

TEXT_DARK  = "#0d0d0d"      # Almost black
TEXT_MID   = "#2a2a2a"
TEXT_LIGHT = "#4a5568"
TEXT_FAINT = "#5a6b7d"

SHADOW     = "0 2px 8px rgba(0, 0, 0, 0.06)"
SHADOW_MD  = "0 4px 12px rgba(0, 0, 0, 0.08)"

PL_BG      = "rgba(255,255,255,0)"
GRID       = "#e8ecf1"

# ────────────────────────────────────────────────────────────────────
# GLOBAL CSS
# ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

  * {{ box-sizing: border-box; }}

  html, body, .stApp {{
    background-color: {BG_MAIN};
    color: {TEXT_DARK};
    font-family: 'Inter', 'Segoe UI', -apple-system, sans-serif;
  }}

  /* ── Sidebar ── */
  [data-testid="stSidebar"] {{
    background-color: {BG_LIGHT};
    border-right: 1px solid {BORDER};
  }}
  [data-testid="stSidebar"] * {{ color: {TEXT_DARK}; }}

  /* ── Main content ── */
  div[data-testid="stAppViewContainer"] {{
    background-color: {BG_MAIN};
  }}

  /* ── Divider ── */
  hr {{ border-color: {BORDER}; margin: 24px 0; }}

  /* ── Page Title ── */
  .page-title {{
    font-size: 2.2rem; font-weight: 800;
    color: {TEXT_DARK}; margin-bottom: 8px; letter-spacing: -0.015em;
    line-height: 1.1;
    margin-top: 0;
  }}
  .page-sub {{
    font-size: 0.95rem; color: {TEXT_LIGHT}; margin-bottom: 28px;
    font-weight: 400;
    opacity: 1;
    line-height: 1.4;
    margin-top: 0;
  }}

  /* ── Section Header ── */
  .sec-head {{
    font-size: 0.77rem; font-weight: 700; color: {PRIMARY};
    text-transform: uppercase; letter-spacing: 0.15em;
    border-bottom: 2px solid {PRIMARY};
    padding-bottom: 12px; margin: 40px 0 28px 0;
    display: block;
    opacity: 1;
    clear: both;
  }}

  /* ── KPI Card ── */
  .kpi-card {{
    background: linear-gradient(135deg, {BG_CARD} 0%, {BG_LIGHT} 100%);
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: 32px 24px;
    height: 100%;
    box-shadow: {SHADOW};
    transition: all 0.3s ease;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .kpi-card:hover {{
    box-shadow: {SHADOW_MD};
    border-color: {PRIMARY_LT};
  }}
  .kpi-card .val {{
    font-size: 2.4rem; font-weight: 800; color: {PRIMARY};
    line-height: 1.1; letter-spacing: -0.01em;
    margin-bottom: 8px;
  }}
  .kpi-card .label {{
    font-size: 0.75rem; color: {TEXT_LIGHT}; text-transform: uppercase;
    letter-spacing: 0.12em; margin-bottom: 10px; font-weight: 600;
  }}
  .kpi-card .delta {{
    font-size: 0.86rem; margin-top: 10px; font-weight: 500;
  }}
  .kpi-card .up    {{ color: {SUCCESS}; }}
  .kpi-card .dn    {{ color: {DANGER}; }}
  .kpi-card .nt    {{ color: {INFO}; }}

  /* ── Info Box ── */
  .info-box {{
    background: {BG_LIGHT};
    border-left: 4px solid {ACCENT};
    border-radius: 8px;
    padding: 20px 20px;
    margin: 18px 0;
    box-shadow: {SHADOW};
  }}
  .info-box .hd {{
    font-size: 0.77rem; font-weight: 700; color: {PRIMARY};
    text-transform: uppercase; letter-spacing: 0.1em;
    margin-bottom: 10px;
    opacity: 1;
  }}
  .info-box .bd {{
    font-size: 0.9rem; color: {TEXT_MID}; line-height: 1.7;
    opacity: 1;
  }}

  /* ── Pillar/Component Card ── */
  .component-card {{
    background: {BG_CARD};
    border: 1px solid {BORDER};
    border-top: 3px solid {PRIMARY};
    border-radius: 10px;
    padding: 24px;
    height: 100%;
    box-shadow: {SHADOW};
  }}
  .component-card .title {{
    font-size: 0.97rem; font-weight: 700; color: {TEXT_DARK};
    margin-bottom: 12px;
    line-height: 1.3;
  }}
  .component-card .body {{
    font-size: 0.85rem; color: {TEXT_MID}; line-height: 1.7;
    margin-bottom: 14px;
  }}
  .component-card .tech {{
    font-size: 0.8rem; color: {ACCENT}; font-weight: 600;
  }}

  /* ── Progress Bar ── */
  .prog-row {{
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 12px;
  }}
  .prog-label {{
    font-size: 0.85rem; color: {TEXT_MID}; min-width: 240px;
    font-weight: 500;
  }}
  .prog-wrap {{
    flex: 1; background: {BORDER_LT}; border-radius: 6px;
    height: 8px; overflow: hidden;
  }}
  .prog-fill {{
    height: 100%; border-radius: 6px;
  }}
  .prog-pct {{
    font-size: 0.82rem; color: {PRIMARY}; min-width: 42px;
    text-align: right; font-weight: 600;
  }}

  /* ── Table ── */
  .data-table {{
    width: 100%; border-collapse: collapse;
    font-size: 0.87rem; background: {BG_CARD};
    border: 1px solid {BORDER}; border-radius: 8px;
    overflow: hidden;
  }}
  .data-table th {{
    background: {BG_LIGHT}; color: {PRIMARY};
    font-size: 0.75rem; text-transform: uppercase;
    letter-spacing: 0.1em; padding: 12px 14px;
    border-bottom: 2px solid {BORDER};
    text-align: left; font-weight: 700;
  }}
  .data-table td {{
    padding: 11px 14px; border-bottom: 1px solid {BORDER};
    color: {TEXT_MID};
  }}
  .data-table tr:last-child td {{
    border-bottom: none;
  }}
  .data-table tr:hover td {{
    background: {BG_LIGHT};
  }}

  /* ── Badge ── */
  .badge {{
    display: inline-block; padding: 5px 12px;
    border-radius: 20px; font-size: 0.73rem;
    font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.08em;
  }}
  .b-active  {{ background: #e8f5e9; color: {SUCCESS}; border: 1px solid {SUCCESS}; }}
  .b-planned {{ background: #fff3e0; color: {WARNING}; border: 1px solid {WARNING}; }}
  .b-future  {{ background: #e3f2fd; color: {INFO}; border: 1px solid {INFO}; }}
  .b-risk    {{ background: #ffebee; color: {DANGER}; border: 1px solid {DANGER}; }}

  /* ── Phase Card ── */
  .phase-card {{
    background: {BG_CARD}; border: 1px solid {BORDER};
    border-left: 4px solid {PRIMARY};
    border-radius: 10px; padding: 24px;
    height: 100%; box-shadow: {SHADOW};
  }}
  .phase-card .ph-num {{
    font-size: 0.72rem; font-weight: 700; color: {TEXT_LIGHT};
    text-transform: uppercase; letter-spacing: 0.12em;
    margin-bottom: 4px;
  }}
  .phase-card .ph-name {{
    font-size: 1.08rem; font-weight: 700; color: {TEXT_DARK};
    margin: 0 0 10px 0;
    line-height: 1.2;
  }}
  .phase-card .ph-dur {{
    font-size: 0.85rem; color: {ACCENT}; margin-bottom: 12px;
    font-weight: 600;
  }}
  .phase-card ul {{
    margin: 14px 0 0 18px; padding: 0;
    list-style: none;
  }}
  .phase-card li {{
    font-size: 0.85rem; color: {TEXT_MID};
    margin-bottom: 7px; line-height: 1.5;
    position: relative; padding-left: 18px;
  }}
  .phase-card li:before {{
    content: "→"; position: absolute;
    left: 0; color: {PRIMARY}; font-weight: 700;
  }}

  /* ── Metric Box ── */
  .metric-box {{
    background: {BG_LIGHT}; border: 1px solid {BORDER};
    border-radius: 8px; padding: 18px 16px;
    text-align: center;
    min-height: 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }}
  .metric-box .metric-val {{
    font-size: 1.8rem; font-weight: 800;
    color: {PRIMARY}; line-height: 1;
    margin-bottom: 8px;
  }}
  .metric-box .metric-label {{
    font-size: 0.78rem; color: {TEXT_LIGHT};
    text-transform: uppercase; letter-spacing: 0.1em;
    font-weight: 600;
  }}

  /* ── Hide default chrome ── */
  footer, header {{ visibility: hidden; }}
  div[data-testid="stDecoration"] {{ display: none; }}

  /* ── Radio buttons styling ── */
  [role="radiogroup"] label {{
    font-weight: 500 !important;
    color: {TEXT_MID} !important;
  }}

  /* ── Selectbox styling ── */
  [data-testid="stSelectbox"] {{
    border: 1px solid {BORDER} !important;
    border-radius: 8px !important;
  }}

  /* ── Slider styling ── */
  [data-testid="stSlider"] div {{
    color: {TEXT_MID} !important;
  }}

  /* ── Column separator ── */
  .col-divider {{
    border-left: 1px solid {BORDER};
    padding-left: 24px;
  }}
</style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────
# UTILITY FUNCTIONS
# ────────────────────────────────────────────────────────────────────

def kpi_card(val, label, delta="", dtype="nt"):
    dt = f'<div class="delta {dtype}">{delta}</div>' if delta else ""
    return f'<div class="kpi-card"><div class="val">{val}</div><div class="label">{label}</div>{dt}</div>'

def info_box(heading, body):
    return f'<div class="info-box"><div class="hd">{heading}</div><div class="bd">{body}</div></div>'

def sec(txt):
    return f'<div class="sec-head">{txt}</div>'

def badge(txt, kind="active"):
    return f'<span class="badge b-{kind}">{txt}</span>'

def metric_box(val, label):
    return f'<div class="metric-box"><div class="metric-val">{val}</div><div class="metric-label">{label}</div></div>'

def pl(fig, h=None):
    """Apply consistent Plotly theme."""
    fig.update_layout(
        paper_bgcolor=PL_BG, plot_bgcolor=PL_BG,
        font=dict(color=TEXT_MID, family="Inter, Segoe UI, sans-serif", size=12),
        margin=dict(l=80, r=60, t=60, b=100),
        height=h,
        legend=dict(bgcolor="rgba(255,255,255,0.95)", bordercolor=BORDER, borderwidth=1, x=0, y=1.18),
        hovermode="x unified",
    )
    fig.update_xaxes(
        gridcolor=GRID, zerolinecolor=BORDER, color=TEXT_LIGHT,
        linecolor=BORDER, showgrid=True, gridwidth=1,
        tickfont=dict(size=12, color=TEXT_LIGHT),
        title_font=dict(size=13, color=TEXT_DARK),
    )
    fig.update_yaxes(
        gridcolor=GRID, zerolinecolor=BORDER, color=TEXT_LIGHT,
        linecolor=BORDER, showgrid=True, gridwidth=1,
        tickfont=dict(size=12, color=TEXT_LIGHT),
        title_font=dict(size=13, color=TEXT_DARK),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding: 12px 0 24px 0; border-bottom: 1px solid {BORDER}; margin-bottom: 20px;">
      <div style="font-size: 0.7rem; color: {TEXT_LIGHT}; text-transform: uppercase;
                  letter-spacing: 0.14em; margin-bottom: 4px; font-weight: 700;">Enterprise Strategy</div>
      <div style="font-size: 1.2rem; font-weight: 800; color: {PRIMARY}; line-height: 1.1;">
        Student Retention Analytics</div>
      <div style="font-size: 0.82rem; color: {ACCENT}; margin-top: 4px; font-weight: 600;">
        Data-Driven Early Warning System</div>
    </div>
    """, unsafe_allow_html=True)

    pages = {
        "Executive Overview":        "Overview",
        "Student Risk Intelligence":  "Risk Analytics",
        "Data Architecture":          "Architecture",
        "Analytics Maturity":         "Maturity Model",
        "Implementation Roadmap":     "Roadmap",
        "KPI Tracker":               "KPI Metrics",
        "ROI Calculator":            "ROI Analysis",
    }

    page = st.radio(
        "Navigate",
        list(pages.keys()),
        format_func=lambda x: pages[x],
        label_visibility="collapsed",
    )

    st.markdown(f"""
    <div style="margin-top: 32px; padding: 14px 16px; background: {BG_LIGHT};
                border-radius: 8px; border: 1px solid {BORDER};">
      <div style="font-size: 0.7rem; color: {TEXT_LIGHT}; margin-bottom: 6px;
                  text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700;">Programme Status</div>
      <div style="font-size: 0.88rem; color: {TEXT_DARK}; font-weight: 600; margin-bottom: 4px;">Phase 1 — Foundation</div>
      <div style="font-size: 0.8rem; color: {SUCCESS};">Active — Month 4</div>
    </div>
    <div style="position: fixed; bottom: 20px; left: 20px; right: 20px;
                font-size: 0.7rem; color: {TEXT_LIGHT}; line-height: 1.7;">
      <div style="font-weight: 600; margin-bottom: 4px;">OMIS 407</div>
      Analytics Planning & Strategy<br>
      Classification: <span style="color: {WARNING}; font-weight: 700;">CONFIDENTIAL</span><br>
      February 2026
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# PAGE 1 — EXECUTIVE OVERVIEW
# ════════════════════════════════════════════════════════════════════
if page == "Executive Overview":
    st.markdown('<div class="page-title">Executive Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Strategic assessment and programme impact projection for governance approval</div>', unsafe_allow_html=True)

    # KPI Row
    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        st.markdown(kpi_card("27.5%", "Current Dropout Rate", "Historical baseline 25–30%", "dn"), unsafe_allow_html=True)
    with c2:
        st.markdown(kpi_card("17.5%", "Target Dropout Rate", "36% reduction by Month 18", "up"), unsafe_allow_html=True)
    with c3:
        st.markdown(kpi_card("500+", "Students Retained", "Per annual cohort at target", "up"), unsafe_allow_html=True)
    with c4:
        st.markdown(kpi_card("L4", "Analytics Maturity Target", "From Level 1 (Ad-Hoc) to Predictive", "nt"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown(sec("Dropout Rate Reduction Pathway"), unsafe_allow_html=True)

        # Simple bar chart showing phase progression
        phases = ["Current\n(2025)", "After\nPhase 1", "After\nPhase 2", "Target\n(Month 18)"]
        dropout_rates = [27.5, 26.0, 23.0, 17.5]
        colors_chart = [DANGER, WARNING, ACCENT, SUCCESS]

        fig = go.Figure(go.Bar(
            x=phases,
            y=dropout_rates,
            marker=dict(color=colors_chart, opacity=0.85, line=dict(width=2, color=BG_MAIN)),
            text=[f"{v:.1f}%" for v in dropout_rates],
            textposition="outside",
            textfont=dict(color=TEXT_DARK, size=12),
            hovertemplate="<b>%{x}</b><br>Dropout Rate: %{y:.1f}%<extra></extra>",
        ))
        fig.update_layout(
            margin=dict(l=70, r=60, t=60, b=100),
            showlegend=False,
            yaxis_title="Dropout Rate (%)",
            xaxis_title="Programme Phase",
        )
        fig.update_yaxes(range=[10, 32])
        pl(fig, 360)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown(sec("Student Cohort — Current State"), unsafe_allow_html=True)

        # Simple stacked bar chart for cohort composition
        categories = ["Current\nCohort"]
        retained = [3625]
        at_risk = [1375]

        fig2 = go.Figure(data=[
            go.Bar(y=categories, x=retained, name="Retained (73%)", orientation="h",
                   marker=dict(color=SUCCESS, opacity=0.85),
                   text=["3,625 students"], textposition="inside", textfont=dict(color="#ffffff", size=11)),
            go.Bar(y=categories, x=at_risk, name="At-Risk (27%)", orientation="h",
                   marker=dict(color=WARNING, opacity=0.85),
                   text=["1,375 students"], textposition="inside", textfont=dict(color="#ffffff", size=11)),
        ])
        fig2.update_layout(
            barmode="stack",
            margin=dict(l=40, r=60, t=60, b=40),
            legend=dict(orientation="v", y=0.95, x=0.6),
            showlegend=True,
            xaxis_title="Number of Students",
        )
        fig2.update_xaxes(range=[0, 5500])
        pl(fig2, 360)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(info_box(
            "Impact Projection",
            "Targeting 36% dropout reduction (27.5% → 17.5%) saves ~500 students per cohort. At 3+ years tuition per student, lifetime ROI exceeds £2.5M per cohort."
        ), unsafe_allow_html=True)

    # Strategic Pillars
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(sec("Strategic Intervention Pillars"), unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4, gap="medium")
    pillars = [
        ("Data Lakehouse", "Modern architecture integrating all five operational systems via governed ETL/ELT pipelines with ACID transaction guarantees and ML-ready analytics.",
         "Delta Lake + Apache Iceberg"),
        ("Predictive Model", "Machine learning system generating at-risk scores by Week 3–5 (vs current Weeks 10–12), enabling timely advisor intervention.",
         "Multi-factor ML algorithm"),
        ("Governance Framework", "Federated data governance with RBAC, metadata lineage, business glossary, and full GDPR/FERPA compliance.",
         "Data Governance Committee"),
        ("Analytics Advancement", "Maturity progression from Level 1 (Ad-Hoc) to Level 3–4 (Predictive) through phased infrastructure investment.",
         "Capability progression"),
    ]
    for col, (title, body, tech) in zip([p1, p2, p3, p4], pillars):
        with col:
            st.markdown(
                f'<div class="component-card">'
                f'<div class="title">{title}</div>'
                f'<div class="body">{body}</div>'
                f'<div class="tech">{tech}</div>'
                f'</div>',
                unsafe_allow_html=True
            )


# ════════════════════════════════════════════════════════════════════
# PAGE 2 — STUDENT RISK INTELLIGENCE
# ════════════════════════════════════════════════════════════════════
elif page == "Student Risk Intelligence":
    st.markdown('<div class="page-title">Student Risk Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Predictive model architecture, signal analysis, and early-warning system performance</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 2], gap="large")

    with col_left:
        st.markdown(sec("Risk Score Distribution — Current Cohort Simulation"), unsafe_allow_html=True)
        np.random.seed(42)
        low_risk   = np.random.beta(2, 7, 3200) * 100
        medium     = np.random.beta(5, 5, 1000) * 100
        high_risk  = np.random.beta(7, 2,  800) * 100

        fig3 = go.Figure()
        for scores, name, color in [
            (low_risk,  "Low Risk (0–40)",      SUCCESS),
            (medium,    "Moderate Risk (40–65)", ACCENT),
            (high_risk, "High Risk (65–100)",    DANGER),
        ]:
            fig3.add_trace(go.Histogram(
                x=scores, name=name, nbinsx=30,
                marker_color=color, opacity=0.75,
                hovertemplate=f"<b>{name}</b><br>Score: %{{x:.0f}}<br>Students: %{{y}}<extra></extra>",
            ))
        fig3.add_vline(x=65, line=dict(color=DANGER, dash="dash", width=2),
                       annotation_text="High-Risk Threshold", annotation_font_color=DANGER)
        fig3.add_vline(x=40, line=dict(color=ACCENT, dash="dash", width=2),
                       annotation_text="Moderate Threshold", annotation_font_color=ACCENT)
        fig3.update_layout(
            barmode="overlay",
            xaxis_title="Risk Score (0–100)",
            yaxis_title="Number of Students",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        )
        pl(fig3, 340)
        st.plotly_chart(fig3, use_container_width=True)

    with col_right:
        st.markdown(sec("Intervention Funnel"), unsafe_allow_html=True)
        funnel_labels = ["Total Cohort", "At-Risk\nIdentified", "Advisor\nContacted", "Intervention\nAccepted", "Dropout\nPrevented"]
        funnel_vals   = [5000, 875, 750, 560, 490]

        fig4 = go.Figure(go.Funnel(
            y=funnel_labels, x=funnel_vals,
            textposition="inside",
            texttemplate="%{label}<br><b>%{value}</b>",
            marker=dict(color=[PRIMARY, ACCENT, INFO, SUCCESS, SUCCESS]),
            connector=dict(line=dict(color=BORDER, width=1)),
        ))
        pl(fig4, 340)
        st.plotly_chart(fig4, use_container_width=True)

    # Early warning timeline
    st.markdown(sec("Early-Warning Detection Timeline — Current vs Proposed"), unsafe_allow_html=True)
    t_col1, t_col2 = st.columns([2, 2], gap="large")

    with t_col1:
        weeks = list(range(1, 13))
        current_system   = [0]*9 + [0.3, 0.6, 1.0]
        proposed_system  = [0]*2 + [0.2, 0.5, 0.75, 0.9, 1.0]*2

        fig5 = go.Figure()
        fig5.add_trace(go.Scatter(
            x=weeks, y=[v*100 for v in current_system],
            name="Current System", fill="tozeroy",
            line=dict(color=DANGER, width=2.5),
            fillcolor=f"rgba(200, 76, 60, 0.08)",
        ))
        fig5.add_trace(go.Scatter(
            x=weeks, y=[v*100 for v in proposed_system],
            name="Proposed ML Model", fill="tozeroy",
            line=dict(color=SUCCESS, width=2.5),
            fillcolor=f"rgba(45, 139, 74, 0.08)",
        ))
        fig5.add_vrect(x0=3, x1=5, fillcolor=SUCCESS, opacity=0.05, line_width=0)
        fig5.add_vrect(x0=10, x1=12, fillcolor=DANGER, opacity=0.05, line_width=0)
        fig5.update_layout(
            xaxis_title="Semester Week",
            yaxis_title="Detection Coverage (%)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        )
        pl(fig5, 320)
        st.plotly_chart(fig5, use_container_width=True)

    with t_col2:
        st.markdown(sec("Data Sources — Predictive Weight"), unsafe_allow_html=True)
        sources = ["LMS Engagement", "Academic Records", "Finance Data", "Welfare Signals", "Demographics"]
        weights = [92, 88, 74, 65, 48]

        fig6 = go.Figure(go.Bar(
            y=sources,
            x=weights,
            orientation="h",
            marker=dict(
                color=weights,
                colorscale=[[0, INFO], [1, SUCCESS]],
                showscale=False,
            ),
            text=[f"{v}%" for v in weights],
            textposition="outside",
            textfont=dict(color=TEXT_DARK, size=11),
            hovertemplate="<b>%{y}</b><br>Weight: %{x}%<extra></extra>",
        ))
        fig6.update_layout(
            xaxis=dict(range=[0, 110], title="Predictive Power (%)"),
        )
        pl(fig6, 320)
        st.plotly_chart(fig6, use_container_width=True)

    # Risk composition radar
    st.markdown(sec("Risk Factor Impact Matrix"), unsafe_allow_html=True)

    # Simplified heatmap
    risk_factors = ["LMS Engagement", "Academic Trajectory", "Financial Stress", "Attendance", "Welfare Flags"]
    student_segments = ["Low Risk", "Moderate", "High Risk", "Intervention", "Retained"]

    # Impact matrix (simplified to 5x5 for readability)
    impact_scores = [
        [15, 45, 92, 88, 20],
        [20, 60, 88, 85, 25],
        [10, 35, 74, 68, 15],
        [8, 28, 65, 60, 12],
        [5, 15, 48, 45, 8],
    ]

    fig_heat = go.Figure(data=go.Heatmap(
        z=impact_scores,
        x=student_segments,
        y=risk_factors,
        colorscale=[[0, "#e8f5e9"], [0.5, "#ffd54f"], [1, "#c84c3c"]],
        hovertemplate="<b>%{y}</b><br>%{x}<br>Impact: %{z}%<extra></extra>",
        colorbar=dict(title="Impact %", thickness=15, len=0.7),
    ))

    fig_heat.update_layout(
        yaxis_title="Risk Factors",
        xaxis_title="Student Segment",
        margin=dict(l=130, r=80, t=60, b=100),
        height=320,
    )
    pl(fig_heat, None)
    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Key insights boxes
    col_left, col_right = st.columns(2, gap="large")
    with col_left:
        st.markdown(info_box(
            "Critical Insight",
            "LMS Engagement and Academic Trajectory are the strongest predictors of at-risk status (88–92% impact). These early signals appear by Week 3–5, explaining the model's early detection capability."
        ), unsafe_allow_html=True)
    with col_right:
        st.markdown(info_box(
            "Intervention Focus",
            "For high-risk students: prioritize LMS re-engagement and academic recovery. Financial stress and welfare flags are secondary but compound risk. Retention interventions addressing these factors show 60–70% effectiveness."
        ), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# PAGE 3 — DATA ARCHITECTURE
# ════════════════════════════════════════════════════════════════════
elif page == "Data Architecture":
    st.markdown('<div class="page-title">Data Architecture</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Enterprise Data Lakehouse design specification and component integration</div>', unsafe_allow_html=True)

    st.markdown(sec("Integrated Data Flow Architecture"), unsafe_allow_html=True)

    node_labels = [
        "Admissions System", "Learning Management\nSystem", "Student Finance", "Academic Records", "Student Affairs",
        "ETL Pipeline\n(Structured)", "API Layer\n(Real-Time)",
        "Landing Zone\n(Raw Data)", "Silver Layer\n(Curated)", "Gold Layer\n(Analytics)",
        "Metadata\nGovernance",
        "Analytics\nSandbox",
        "Executive Dashboard", "Advisor Portal", "Analyst Workbench", "API Output Layer",
    ]
    node_colors = [
        PRIMARY, PRIMARY, PRIMARY, PRIMARY, PRIMARY,
        ACCENT, ACCENT,
        "#f5f5f5", ACCENT, SUCCESS,
        INFO,
        SUCCESS,
        SUCCESS, SUCCESS, INFO, PRIMARY,
    ]
    source = [0,1,2,3,4, 0,1,2,  5,6, 7,  8,8,8,  9,9,9,9, 9]
    target = [5,6,5,5,6, 6,5,6,  8,8, 9, 10,11,9, 12,13,14,15, 10]
    value  = [3,4,3,3,2, 2,4,2,  8,6, 14,  2,2,10, 3,3,3,3, 2]
    link_colors = [
        f"rgba(30, 90, 158, 0.2)"]*9 + [f"rgba(232, 153, 79, 0.2)"]*3 + [f"rgba(45, 139, 74, 0.2)"]*7

    fig_arch = go.Figure(go.Sankey(
        node=dict(
            pad=20, thickness=24, line=dict(color=BORDER, width=1),
            label=node_labels, color=node_colors,
            hovertemplate="%{label}<extra></extra>",
            x=[0]*5 + [0.15]*2 + [0.35]*3 + [0.55] + [0.65] + [0.85]*4,
            y=[0, 0.15, 0.3, 0.45, 0.6, 0.2, 0.4, 0.2, 0.4, 0.6, 0.5, 0.75, 0.1, 0.35, 0.55, 0.8],
        ),
        link=dict(
            source=source, target=target, value=value, color=link_colors,
        ),
    ))
    pl(fig_arch, 420)
    st.plotly_chart(fig_arch, use_container_width=True)

    # Component specifications
    st.markdown(sec("Component Specifications"), unsafe_allow_html=True)

    components = [
        ("ETL / ELT Engine",
         "Structured data (Admissions, Finance, Academic Records) uses traditional ETL. Semi-structured data (LMS logs, student affairs) uses ELT with dbt for in-lake transformation.",
         "Apache Airflow + dbt", "Active"),
        ("API Ingestion Layer",
         "Near-real-time event streams from LMS webhooks and Finance payment APIs. Sub-24-hour signal generation for early warning.",
         "REST APIs + Kafka", "Active"),
        ("Data Lakehouse",
         "Three-layer architecture (Raw Landing / Silver Curated / Gold Analytics-Ready) with ACID guarantees, schema enforcement, and historical data preservation.",
         "Delta Lake / Iceberg", "Active"),
        ("Metadata Management",
         "Data lineage tracking, business glossary management, data quality scoring, and audit trail. Every risk score is fully traceable.",
         "Apache Atlas / Unity Catalog", "Planned"),
        ("Analytics Sandbox",
         "Isolated environment for ML model development using pseudonymised historical data. Separate RBAC. Weekly/monthly refresh cycles.",
         "Databricks / Jupyter", "Planned"),
        ("Consumption Layer",
         "Four access tiers: Executive Dashboard (KPIs), Advisor Portal (risk scores), Analyst Workbench (SQL/BI), API Output (third-party integration).",
         "Power BI / Tableau / REST API", "Planned"),
    ]

    cols = st.columns(2, gap="medium")
    for i, (name, desc, tech, status) in enumerate(components):
        col = cols[i % 2]
        with col:
            badge_type = "active" if status == "Active" else "planned"
            st.markdown(f"""
            <div style="background: {BG_LIGHT}; border: 1px solid {BORDER}; border-top: 3px solid {PRIMARY};
                        border-radius: 8px; padding: 18px; margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <div style="font-size: 0.95rem; font-weight: 700; color: {TEXT_DARK};">{name}</div>
                <span class="badge b-{badge_type}">{status}</span>
              </div>
              <div style="font-size: 0.87rem; color: {TEXT_MID}; line-height: 1.6; margin-bottom: 10px;">{desc}</div>
              <div style="font-size: 0.8rem; color: {ACCENT}; font-weight: 600;">Technology: {tech}</div>
            </div>""", unsafe_allow_html=True)

    # Architecture comparison
    st.markdown(sec("Warehouse Type Analysis — Architecture Selection Rationale"), unsafe_allow_html=True)

    arch_data = {
        "Capability": [
            "Structured Data Handling",
            "Semi-Structured Data (JSON)",
            "Historical Depth",
            "Governance & Lineage",
            "ACID Transactions",
            "GDPR / Data Protection",
            "Real-Time Ingestion",
            "ML Model Training",
            "Cost Efficiency at Scale",
            "Governance Maturity Required",
        ],
        "Traditional Warehouse": ["✓ Excellent","✗ Poor","✓ Good","✓ Strong","✓ Native","✓ Strong","⚠ Limited","⚠ Limited","✗ Expensive","✓ Moderate"],
        "Data Lake": ["✓ Good","✓ Excellent","✓ Excellent","✗ Weak","✗ None","⚠ Complex","✓ Excellent","✓ Excellent","✓ Low","✗ High"],
        "Lakehouse Selected": ["✓ Excellent","✓ Excellent","✓ Excellent","✓ Strong","✓ Native","✓ Strong","✓ Good","✓ Excellent","✓ Low","⚠ Moderate"],
    }
    df_arch = pd.DataFrame(arch_data)

    table_html = '<table class="data-table"><thead><tr>'
    for col in df_arch.columns:
        highlight = f' style="background: {BORDER_LT}; color: {SUCCESS};"' if "Selected" in col else ""
        table_html += f'<th{highlight}>{col}</th>'
    table_html += '</tr></thead><tbody>'
    for _, row in df_arch.iterrows():
        table_html += '<tr>'
        for j, val in enumerate(row):
            cell_style = f' style="background: {BORDER_LT}; color: {SUCCESS}; font-weight: 700;"' if j == 3 else ""
            table_html += f'<td{cell_style}>{val}</td>'
        table_html += '</tr>'
    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# PAGE 4 — ANALYTICS MATURITY
# ════════════════════════════════════════════════════════════════════
elif page == "Analytics Maturity":
    st.markdown('<div class="page-title">Analytics Maturity Framework</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Five-level progression model and capability advancement roadmap</div>', unsafe_allow_html=True)

    m_left, m_right = st.columns([2, 3], gap="large")

    with m_left:
        st.markdown(sec("Maturity Level Progression"), unsafe_allow_html=True)
        levels = ["Ad-Hoc\nLevel 1", "Descriptive\nLevel 2", "Diagnostic\nLevel 3", "Predictive\nLevel 4", "Prescriptive\nLevel 5"]
        current = [100, 25, 5, 0, 0]
        target12 = [100, 90, 80, 70, 5]
        target18 = [100, 100, 90, 85, 30]

        fig_mat = go.Figure()
        fig_mat.add_trace(go.Bar(
            name="Current State", x=levels, y=current,
            marker_color=DANGER, opacity=0.75, text=[f"{v}%" for v in current],
            textposition="outside", textfont=dict(color=TEXT_DARK, size=10),
        ))
        fig_mat.add_trace(go.Bar(
            name="Month 12 Target", x=levels, y=target12,
            marker_color=ACCENT, opacity=0.75, text=[f"{v}%" for v in target12],
            textposition="outside", textfont=dict(color=TEXT_DARK, size=10),
        ))
        fig_mat.add_trace(go.Bar(
            name="Month 18+ Vision", x=levels, y=target18,
            marker_color=SUCCESS, opacity=0.75, text=[f"{v}%" for v in target18],
            textposition="outside", textfont=dict(color=TEXT_DARK, size=10),
        ))
        fig_mat.update_layout(
            barmode="group",
            yaxis_title="Capability Score (%)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        )
        pl(fig_mat, 380)
        st.plotly_chart(fig_mat, use_container_width=True)

    with m_right:
        st.markdown(sec("Level Definitions"), unsafe_allow_html=True)
        maturity_levels = [
            ("Level 1", "Ad-Hoc", DANGER,
             "Manual, inconsistent reporting produced on demand by individual staff. No shared data infrastructure or governance.",
             "Current State", "b-risk"),
            ("Level 2", "Descriptive", ACCENT,
             "Standardised dashboards showing business results. Consistent KPI definitions and automated ETL pipelines.",
             "Phase 1 Exit", "b-planned"),
            ("Level 3", "Diagnostic", INFO,
             "Understanding patterns and root causes. Cross-system analysis enabling faculty to explore contributing factors.",
             "Phase 2 Target", "b-planned"),
            ("Level 4", "Predictive", SUCCESS,
             "Forward-looking risk scores updated weekly. Machine learning identifies at-risk students. Proactive interventions enabled.",
             "Month 12 Target", "b-future"),
            ("Level 5", "Prescriptive", PRIMARY,
             "System recommends optimal interventions per student profile. Automated personalised support pathways.",
             "Future Vision", "b-future"),
        ]
        for lvl, name, color, desc, phase, btype in maturity_levels:
            st.markdown(f"""
            <div style="display: flex; gap: 12px; margin-bottom: 12px; background: {BG_LIGHT};
                        border: 1px solid {BORDER}; border-left: 4px solid {color}; border-radius: 8px; padding: 12px 14px;">
              <div style="min-width: 56px; text-align: center;">
                <div style="font-size: 0.7rem; color: {TEXT_LIGHT}; text-transform: uppercase; font-weight: 600;">{lvl}</div>
                <div style="font-size: 0.92rem; font-weight: 800; color: {color};">{name}</div>
              </div>
              <div style="flex: 1;">
                <div style="font-size: 0.85rem; color: {TEXT_MID}; line-height: 1.5; margin-bottom: 6px;">{desc}</div>
                <span class="badge b-{btype}">{phase}</span>
              </div>
            </div>""", unsafe_allow_html=True)

    # Capability dimensions
    st.markdown(sec("Capability Assessment — Current vs Month 12 Target"), unsafe_allow_html=True)
    r_left, r_right = st.columns([1, 1], gap="large")

    with r_left:
        categories_mat = [
            "Data Integration", "Reporting\nAutomation", "Data Quality",
            "Predictive\nCapability", "Self-Service\nAnalytics", "Governance"
        ]
        current_scores = [15, 20, 25, 5, 20, 10]
        target_scores  = [90, 85, 88, 80, 75, 85]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=current_scores + [current_scores[0]],
            theta=categories_mat + [categories_mat[0]],
            fill="toself", name="Current (Level 1)",
            line=dict(color=DANGER, width=2.5),
            fillcolor=f"rgba(200, 76, 60, 0.1)",
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=target_scores + [target_scores[0]],
            theta=categories_mat + [categories_mat[0]],
            fill="toself", name="Target (Level 3–4)",
            line=dict(color=SUCCESS, width=2.5),
            fillcolor=f"rgba(45, 139, 74, 0.1)",
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], gridcolor=GRID),
                angularaxis=dict(color=TEXT_MID),
                bgcolor=PL_BG,
            ),
            legend=dict(orientation="h", y=-0.12),
        )
        pl(fig_radar, 380)
        st.plotly_chart(fig_radar, use_container_width=True)

    with r_right:
        st.markdown(sec("Capability Gap Analysis"), unsafe_allow_html=True)
        caps = list(zip(categories_mat, current_scores, target_scores))
        for cap, curr, tgt in caps:
            gap = tgt - curr
            cap_clean = cap.replace("\n", " ")
            st.markdown(f"""
            <div style="margin-bottom: 14px;">
              <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                <span style="font-size: 0.87rem; color: {TEXT_MID}; font-weight: 500;">{cap_clean}</span>
                <span style="font-size: 0.82rem; color: {TEXT_LIGHT};">{curr}% → <span style="color: {SUCCESS}; font-weight: 700;">{tgt}%</span></span>
              </div>
              <div style="background: {BORDER_LT}; border-radius: 6px; height: 10px; overflow: hidden; position: relative;">
                <div style="position: absolute; width: {tgt}%; height: 100%; background: rgba(45, 139, 74, 0.25); border-radius: 6px;"></div>
                <div style="position: absolute; width: {curr}%; height: 100%; background: {DANGER}; border-radius: 6px;"></div>
              </div>
              <div style="font-size: 0.77rem; color: {ACCENT}; margin-top: 3px; font-weight: 600;">Gap to close: +{gap} points</div>
            </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# PAGE 5 — IMPLEMENTATION ROADMAP
# ════════════════════════════════════════════════════════════════════
elif page == "Implementation Roadmap":
    st.markdown('<div class="page-title">Implementation Roadmap</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Three-phase architecture activation spanning 18 months</div>', unsafe_allow_html=True)

    # Phase cards
    ph1, ph2, ph3 = st.columns(3, gap="medium")
    phases = [
        ("Phase 1", "Foundation", "Months 1–4",
         ACCENT, "b-active",
         ["Data audit across five OLTP systems",
          "KPI standardisation and business glossary",
          "Data Governance Committee establishment",
          "RBAC and security framework",
          "Structured source warehouse",
          "Executive Dashboard MVP"]),
        ("Phase 2", "Architecture Build", "Months 5–8",
         PRIMARY, "b-planned",
         ["Full Lakehouse deployment",
          "ETL/ELT pipelines for all sources",
          "API layer integration",
          "Metadata lineage implementation",
          "Analytics sandbox provisioning",
          "Faculty Advisor Portal launch",
          "Analytics Maturity: L2–L3"]),
        ("Phase 3", "Model Activation", "Months 9–18",
         SUCCESS, "b-future",
         ["ML model development and training",
          "Demographic fairness audit",
          "Week 3–5 early warning go-live",
          "Stakeholder rollout to advisors",
          "Third-party API layer launch",
          "Continuous model retraining",
          "Analytics Maturity: L3–L4"]),
    ]
    for col, (ph, name, dur, col_c, btype, items) in zip([ph1, ph2, ph3], phases):
        with col:
            items_html = "".join(f'<li style="color: {TEXT_MID}; margin-bottom: 5px; font-size: 0.85rem;">{i}</li>' for i in items)
            st.markdown(f"""
            <div class="phase-card" style="border-left-color: {col_c};">
              <div class="ph-num">Phase {ph[-1]}</div>
              <div class="ph-name">{name}</div>
              <div class="ph-dur">{dur}</div>
              <span class="badge b-{btype}">{'In Progress' if btype=='b-active' else ('Planned' if btype=='b-planned' else 'Future')}</span>
              <ul style="margin: 14px 0 0 18px; padding: 0;">{items_html}</ul>
            </div>""", unsafe_allow_html=True)

    # Gantt chart
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(sec("Detailed Project Timeline"), unsafe_allow_html=True)

    gantt_tasks = [
        ("Data Audit & Inventory",                1,  2, "Phase 1"),
        ("KPI Standardisation",                   1,  3, "Phase 1"),
        ("Data Governance Committee",             2,  4, "Phase 1"),
        ("RBAC Framework",                        2,  4, "Phase 1"),
        ("Structured Source Warehouse",           3,  5, "Phase 1"),
        ("Executive Dashboard",                   4,  5, "Phase 1"),
        ("Lakehouse Deployment",                  5,  7, "Phase 2"),
        ("ETL/ELT Pipelines",                     5,  8, "Phase 2"),
        ("API Layer Integration",                 6,  8, "Phase 2"),
        ("Metadata Management",                   6,  9, "Phase 2"),
        ("Analytics Sandbox",                     7,  9, "Phase 2"),
        ("Advisor Portal",                        8,  9, "Phase 2"),
        ("ML Model Development",                  9, 13, "Phase 3"),
        ("Fairness Audit",                       12, 14, "Phase 3"),
        ("Early Warning Go-Live",                14, 15, "Phase 3"),
        ("Stakeholder Rollout",                  14, 17, "Phase 3"),
        ("Continuous Retraining",                16, 18, "Phase 3"),
    ]

    fig_gantt = go.Figure()
    phase_colors_map = {"Phase 1": ACCENT, "Phase 2": PRIMARY, "Phase 3": SUCCESS}

    for i, (task, start, end, phase) in enumerate(gantt_tasks):
        fig_gantt.add_trace(go.Bar(
            x=[end - start],
            y=[task],
            base=[start],
            orientation="h",
            name=phase,
            marker=dict(color=phase_colors_map[phase], opacity=0.85),
            showlegend=(task == gantt_tasks[[t[3] for t in gantt_tasks].index(phase)][0]),
            hovertemplate=f"<b>{task}</b><br>Month {start} – {end}<extra></extra>",
        ))

    fig_gantt.update_layout(
        barmode="overlay",
        xaxis_title="Month",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
    )
    pl(fig_gantt, 560)
    st.plotly_chart(fig_gantt, use_container_width=True)

    # Phase gates
    st.markdown(sec("Phase Gate Criteria"), unsafe_allow_html=True)
    g1, g2 = st.columns(2, gap="large")
    with g1:
        st.markdown(info_box(
            "Phase 1 → Phase 2 Gate",
            "Data Governance Committee formally established with data owners from all departments. Business glossary approved. Structured warehouse operational. RBAC framework approved by Information Security."
        ), unsafe_allow_html=True)
    with g2:
        st.markdown(info_box(
            "Phase 2 → Phase 3 Gate",
            "All five systems integrated via ETL/ELT pipelines. Metadata lineage operational. Analytics sandbox provisioned with 5+ years pseudonymised data. Faculty Advisor Portal piloting with one faculty."
        ), unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# PAGE 6 — KPI TRACKER
# ════════════════════════════════════════════════════════════════════
elif page == "KPI Tracker":
    st.markdown('<div class="page-title">KPI Framework</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Four measurement domains with baseline, Phase 2, and Phase 3 targets</div>', unsafe_allow_html=True)

    # Domain selector
    domain = st.selectbox(
        "Select KPI Domain",
        ["Domain 1 — Student Retention Outcomes",
         "Domain 2 — Data Infrastructure Performance",
         "Domain 3 — Analytics Capability Maturity",
         "Domain 4 — Governance and Compliance"],
        label_visibility="collapsed",
    )

    kpis = {
        "Domain 1 — Student Retention Outcomes": [
            ("First-Year Dropout Rate",            "27.5%", "24.5%",   "17.5%",   72),
            ("At-Risk Detection Week",             "Wk 10–12", "Wk 6–8", "Wk 3–5",  60),
            ("Advisor Intervention Rate",          "N/A",     "60%",     "80%",    50),
            ("Cohort Retention Improvement",       "0%",      "+12%",    "+36%",   45),
            ("Student Satisfaction Score",         "62%",     "70%",     "80%",    38),
        ],
        "Domain 2 — Data Infrastructure Performance": [
            ("Source Systems Integrated",          "0/5",   "3/5",   "5/5",     100),
            ("Pipeline Uptime",                    "N/A",   "95%",   "99.5%",   85),
            ("Data Quality Score",                 "~45%",  "75%",   "92%",     78),
            ("Metadata Lineage Coverage",          "0%",    "70%",   "100%",    65),
            ("Average Data Latency",               ">24h",  "4h",    "<1h",     70),
        ],
        "Domain 3 — Analytics Capability Maturity": [
            ("Analytics Maturity Level",           "L1",    "L2–3",  "L3–4",    75),
            ("ML Model AUC",                       "N/A",   "In Dev", "≥0.82",   55),
            ("Self-Service Analytics Rate",        "20%",   "60%",   "85%",     60),
            ("Dashboard Weekly Active Users",      "5",     "50+",   "150+",    45),
            ("Risk Score Update Cadence",          "Manual", "Weekly", "Daily",  65),
        ],
        "Domain 4 — Governance and Compliance": [
            ("RBAC Policies Implemented",          "0%",    "70%",   "100%",    70),
            ("DGC Meeting Frequency",              "None",  "Monthly", "Bi-weekly", 60),
            ("Privacy Compliance Audit",           "None",  "Partial", "Complete", 50),
            ("Data Lineage Traceability",          "0%",    "60%",   "100%",    55),
            ("Business Glossary Terms",            "0",     "40+",   "100+",    65),
        ],
    }

    domain_kpis = kpis[domain]

    # Summary stats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(metric_box(str(len(domain_kpis)), "KPIs in Domain"), unsafe_allow_html=True)
    with c2:
        avg_prog = int(np.mean([k[4] for k in domain_kpis]))
        st.markdown(metric_box(f"{avg_prog}%", "Avg Progress"), unsafe_allow_html=True)
    with c3:
        st.markdown(metric_box("18 Mo", "Target Horizon"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI Performance Table with progress bars
    st.markdown(sec("KPI Performance — Progress to Phase 3 Target"), unsafe_allow_html=True)

    # Create simple table with progress bars
    for kpi_name, baseline, p2_target, p3_target, prog in domain_kpis:
        col1, col2, col3 = st.columns([2, 3, 1], gap="medium")

        with col1:
            st.markdown(f"""
            <div style="padding: 10px 0; font-weight: 600; color: {TEXT_DARK};">
            {kpi_name}
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="padding: 8px 0;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="flex: 1; background: {BORDER_LT}; border-radius: 8px; height: 24px; overflow: hidden;">
                  <div style="width: {prog}%; height: 100%; background: linear-gradient(90deg, {PRIMARY}dd, {SUCCESS}dd); border-radius: 8px;"></div>
                </div>
                <span style="font-size: 0.85rem; font-weight: 700; color: {PRIMARY}; min-width: 40px;">{prog}%</span>
              </div>
              <div style="font-size: 0.75rem; color: {TEXT_LIGHT}; margin-top: 4px; text-align: right;">
              Baseline: {baseline} → Target: {p3_target}
              </div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            status_badge = "b-active" if prog >= 70 else ("b-planned" if prog >= 40 else "b-risk")
            st.markdown(f'<span class="badge {status_badge}">{"On Track" if prog >= 70 else ("In Progress" if prog >= 40 else "At Risk")}</span>', unsafe_allow_html=True)

        st.markdown(f"<div style='border-bottom: 1px solid {BORDER}; margin: 12px 0;'></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Domain overview
    st.markdown(sec("Cross-Domain Performance Snapshot"), unsafe_allow_html=True)
    domain_names = ["Student\nRetention", "Data\nInfrastructure", "Analytics\nCapability", "Governance"]
    current_domain = [18, 12, 15, 8]
    target_domain  = [85, 92, 82, 90]

    fig_d = go.Figure()
    fig_d.add_trace(go.Scatterpolar(
        r=current_domain + [current_domain[0]],
        theta=domain_names + [domain_names[0]],
        fill="toself", name="Current State",
        line=dict(color=DANGER, width=2.5),
        fillcolor=f"rgba(200, 76, 60, 0.1)",
    ))
    fig_d.add_trace(go.Scatterpolar(
        r=target_domain + [target_domain[0]],
        theta=domain_names + [domain_names[0]],
        fill="toself", name="Phase 3 Target",
        line=dict(color=SUCCESS, width=2.5),
        fillcolor=f"rgba(45, 139, 74, 0.1)",
    ))
    fig_d.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor=GRID),
            angularaxis=dict(color=TEXT_MID),
            bgcolor=PL_BG,
        ),
        legend=dict(orientation="h", y=-0.15),
    )
    pl(fig_d, 400)
    st.plotly_chart(fig_d, use_container_width=True)


# ════════════════════════════════════════════════════════════════════
# PAGE 7 — ROI CALCULATOR
# ════════════════════════════════════════════════════════════════════
elif page == "ROI Calculator":
    st.markdown('<div class="page-title">ROI and Financial Impact Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Interactive financial model — adjust parameters to project programme outcomes</div>', unsafe_allow_html=True)

    ctrl_col, analysis_col = st.columns([1, 2.2], gap="large")

    with ctrl_col:
        st.markdown(sec("Financial Model Parameters"), unsafe_allow_html=True)

        cohort_size    = st.slider("First-Year Cohort Size", 1000, 10000, 5000, 250)
        current_rate   = st.slider("Baseline Dropout Rate (%)", 10, 45, 28, 1)
        tuition_annual = st.slider("Annual Tuition (GBP 000s)", 5, 50, 15, 1)
        reduction_pct  = st.slider("Expected Dropout Reduction (%)", 5, 50, 36, 1)
        programme_yrs  = st.slider("Programme Duration (Years)", 2, 6, 4, 1)
        invest_cost    = st.slider("Total Investment (GBP M)", 0.5, 10.0, 2.5, 0.25)

        target_rate    = current_rate * (1 - reduction_pct / 100)
        students_saved = int(cohort_size * (current_rate - target_rate) / 100)
        revenue_per    = tuition_annual * 1000 * (programme_yrs - 1)
        total_revenue  = students_saved * revenue_per
        roi_pct        = ((total_revenue - invest_cost * 1_000_000) / (invest_cost * 1_000_000)) * 100 if invest_cost > 0 else 0
        payback        = (invest_cost * 1_000_000) / (total_revenue / 18) if total_revenue > 0 else 0

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(sec("Key Outcomes"), unsafe_allow_html=True)

        st.markdown(kpi_card(
            f"{target_rate:.1f}%", "Target Dropout Rate",
            f"Reduction from {current_rate}%", "up"
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(kpi_card(
            f"{students_saved:,}", "Students Retained",
            "Per cohort over programme duration", "up"
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(kpi_card(
            f"£{total_revenue/1_000_000:.1f}M", "Additional Revenue",
            f"Lifetime value at {programme_yrs}-year programme", "up"
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(kpi_card(
            f"{roi_pct:.0f}%", "Return on Investment",
            f"On £{invest_cost}M investment", "nt" if roi_pct < 200 else "up"
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(kpi_card(
            f"{payback:.1f} mo", "Months to Breakeven",
            "18-month programme horizon", "nt"
        ), unsafe_allow_html=True)

    with analysis_col:
        st.markdown(sec("Financial Scenario Analysis"), unsafe_allow_html=True)

        reductions   = list(range(5, 51, 5))
        rev_scenarios = []
        roi_scenarios = []
        for r in reductions:
            tr = current_rate * (1 - r / 100)
            ss = int(cohort_size * (current_rate - tr) / 100)
            rv = ss * revenue_per
            rev_scenarios.append(rv / 1_000_000)
            roi_scenarios.append(((rv - invest_cost * 1_000_000) / (invest_cost * 1_000_000)) * 100)

        # Revenue scenario chart
        fig_rev = go.Figure(go.Bar(
            x=[f"{r}%" for r in reductions],
            y=rev_scenarios,
            marker=dict(
                color=rev_scenarios,
                colorscale=[[0, INFO], [0.5, ACCENT], [1, SUCCESS]],
                showscale=False,
                line=dict(width=0),
            ),
            text=[f"£{v:.1f}M" for v in rev_scenarios],
            textposition="outside",
            textfont=dict(color=TEXT_DARK, size=10),
            hovertemplate="Reduction: %{x}<br>Revenue: £%{y:.2f}M<extra></extra>",
            name="Additional Revenue",
        ))
        fig_rev.update_layout(
            title="Additional Revenue by Dropout Reduction",
            xaxis_title="Dropout Reduction (%)",
            yaxis_title="Revenue (£M)",
            margin=dict(l=70, r=50, t=60, b=80),
        )
        pl(fig_rev, 320)
        st.plotly_chart(fig_rev, use_container_width=True)

        # ROI scenario chart
        fig_roi_scenario = go.Figure(go.Bar(
            x=[f"{r}%" for r in reductions],
            y=roi_scenarios,
            marker=dict(
                color=roi_scenarios,
                colorscale=[[0, DANGER], [0.25, WARNING], [0.5, ACCENT], [1, SUCCESS]],
                showscale=False,
                line=dict(width=0),
            ),
            text=[f"{int(v)}%" for v in roi_scenarios],
            textposition="outside",
            textfont=dict(color=TEXT_DARK, size=10),
            hovertemplate="Reduction: %{x}<br>ROI: %{y:.0f}%<extra></extra>",
            name="ROI",
        ))
        fig_roi_scenario.update_layout(
            title="ROI Return by Dropout Reduction",
            xaxis_title="Dropout Reduction (%)",
            yaxis_title="ROI (%)",
            margin=dict(l=70, r=50, t=60, b=80),
        )
        pl(fig_roi_scenario, 320)
        st.plotly_chart(fig_roi_scenario, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Cumulative revenue over 18 months
        st.markdown(sec("Cumulative Revenue Build — 18-Month Horizon"), unsafe_allow_html=True)
        months = list(range(0, 19))

        def ramp(m):
            if m < 5: return 0
            if m < 9: return 0.3 * (m - 4) / 4
            if m < 14: return 0.3 + 0.5 * (m - 8) / 6
            return 0.8 + 0.2 * (m - 13) / 5

        cumulative = [total_revenue / 1_000_000 * ramp(m) for m in months]
        invest_line = [invest_cost] * len(months)

        fig_cum = go.Figure()
        fig_cum.add_trace(go.Scatter(
            x=months, y=cumulative, name="Cumulative Revenue",
            line=dict(color=SUCCESS, width=3.5),
            fill="tozeroy",
            fillcolor=f"rgba(45, 139, 74, 0.1)",
            hovertemplate="Month %{x}<br>Revenue: £%{y:.2f}M<extra></extra>",
        ))
        fig_cum.add_trace(go.Scatter(
            x=months, y=invest_line, name=f"Investment Cost",
            line=dict(color=DANGER, width=2.5, dash="dash"),
            opacity=0.8,
            hovertemplate="Month %{x}<br>Cost: £%{y:.2f}M<extra></extra>",
        ))
        fig_cum.update_layout(
            xaxis_title="Month",
            yaxis_title="GBP Millions",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
            margin=dict(l=70, r=50, t=60, b=80),
            hovermode="x unified",
        )
        fig_cum.update_xaxes(tickmode="linear", tick0=0, dtick=2)
        pl(fig_cum, 340)
        st.plotly_chart(fig_cum, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(info_box(
            "Economic Model Basis",
            f"Projections assume: (1) Cohort size = {cohort_size} students, (2) Dropout reduction = {reduction_pct}%, (3) Annual tuition £{tuition_annual}k, (4) Investment £{invest_cost}M. Payback period is typically 12–15 months post-deployment."
        ), unsafe_allow_html=True)
