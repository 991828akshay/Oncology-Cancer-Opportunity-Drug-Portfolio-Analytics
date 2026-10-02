import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Oncology Opportunity & Drug Portfolio Analytics",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

.metric-title {
    font-size: 14px;
    color: #6b7280;
}

.metric-value {
    font-size: 30px;
    font-weight: 700;
    color: #111827;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
}

.small-note {
    color: #6b7280;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

@st.cache_data
def load_csv(filename):
    """Load CSV safely."""
    path = DATA_DIR / filename

    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as e:
        st.error(f"Could not read {filename}: {e}")
        return pd.DataFrame()


def find_column(df, candidates):
    """
    Find a column using exact or partial matching.
    """
    if df.empty:
        return None

    cols = list(df.columns)

    # Exact match
    for candidate in candidates:
        if candidate in cols:
            return candidate

    # Case-insensitive match
    lower_map = {str(c).lower(): c for c in cols}

    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]

    # Partial match
    for candidate in candidates:
        candidate_lower = candidate.lower()

        for col in cols:
            if candidate_lower in str(col).lower():
                return col

    return None


def number_format(value):
    if pd.isna(value):
        return "N/A"

    if isinstance(value, (int, np.integer)):
        return f"{value:,}"

    if isinstance(value, (float, np.floating)):
        return f"{value:,.0f}"

    return str(value)


def show_download(df, filename):
    if not df.empty:
        st.download_button(
            label=f"⬇ Download {filename}",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=filename,
            mime="text/csv"
        )


# ============================================================
# LOAD DATA
# ============================================================

epidemiology = load_csv("01_epidemiology_final.csv")

cancer_decision = load_csv(
    "01_FINAL_CANCER_OPPORTUNITY_DECISION.csv"
)

top_drugs_by_cancer = load_csv(
    "02_FINAL_TOP_DRUGS_BY_CANCER.csv"
)

competitive = load_csv(
    "03_cancer_competitive_landscape.csv"
)

drug_cancer = load_csv(
    "04_drug_cancer_trial_metrics.csv"
)

drug_therapeutic = load_csv(
    "06_drug_therapeutic_dashboard.csv"
)

top20 = load_csv(
    "07_AUTHORITATIVE_STEP56_TOP20.csv"
)

robustness = load_csv(
    "07_robustness_ranking.csv"
)

top5 = load_csv(
    "08_AUTHORITATIVE_STEP56_TOP5.csv"
)

robust_top10 = load_csv(
    "09_robust_top10.csv"
)

cross_cancer = load_csv(
    "DASHBOARD_CROSS_CANCER_TOP15.csv"
)

disease_master = load_csv(
    "DASHBOARD_DISEASE_MASTER.csv"
)

drug_shortlist = load_csv(
    "DASHBOARD_DRUG_SHORTLIST.csv"
)


# ============================================================
# BASIC VALIDATION
# ============================================================

if epidemiology.empty and top20.empty:
    st.error(
        "No dashboard data could be loaded. "
        "Please check that the CSV files are inside the data folder."
    )
    st.stop()


# ============================================================
# COLUMN DETECTION
# ============================================================

# Epidemiology
epi_cancer = find_column(
    epidemiology,
    ["cancer_indication", "cancer", "indication"]
)

epi_incidence = find_column(
    epidemiology,
    ["incidence_cases", "incidence"]
)

epi_deaths = find_column(
    epidemiology,
    ["deaths", "death"]
)

epi_mortality_ratio = find_column(
    epidemiology,
    [
        "mortality_incidence_ratio",
        "mortality_rate_proxy",
        "mortality"
    ]
)


# Cancer decision
decision_cancer = find_column(
    cancer_decision,
    ["cancer_indication", "cancer", "indication"]
)

decision_rank = find_column(
    cancer_decision,
    ["final_rank", "rank"]
)


# Top 20 drugs
drug_name_col = find_column(
    top20,
    ["canonical_drug", "drug_name", "drug"]
)

drug_cancers_col = find_column(
    top20,
    ["n_target_cancers", "cancer_breadth", "target_cancers"]
)

drug_trials_col = find_column(
    top20,
    ["total_target_trials", "total_trials", "trials"]
)

drug_active_col = find_column(
    top20,
    ["active_target_trials", "active_trials"]
)

drug_completed_col = find_column(
    top20,
    ["completed_target_trials", "completed_trials"]
)

drug_sponsors_col = find_column(
    top20,
    [
        "total_unique_sponsors",
        "total_target_sponsors",
        "sponsors"
    ]
)

drug_score_col = find_column(
    top20,
    [
        "drug_opportunity_score",
        "opportunity_score",
        "score"
    ]
)

drug_rank_col = find_column(
    top20,
    ["final_drug_rank", "rank"]
)


# Drug-cancer metrics
dc_drug = find_column(
    drug_cancer,
    ["canonical_drug", "drug_name", "drug"]
)

dc_cancer = find_column(
    drug_cancer,
    ["cancer_indication", "cancer", "indication"]
)

dc_trials = find_column(
    drug_cancer,
    ["total_trials", "total_target_trials", "trials"]
)

dc_active = find_column(
    drug_cancer,
    ["active_trials", "active_target_trials"]
)

dc_completed = find_column(
    drug_cancer,
    ["completed_trials", "completed_target_trials"]
)

dc_sponsors = find_column(
    drug_cancer,
    ["unique_sponsors", "sponsors", "total_unique_sponsors"]
)


# Competitive landscape
comp_cancer = find_column(
    competitive,
    ["cancer_indication", "cancer", "indication"]
)

comp_trials = find_column(
    competitive,
    ["total_trials", "trial_count", "trials"]
)

comp_sponsors = find_column(
    competitive,
    ["total_unique_sponsors", "unique_sponsors", "sponsors"]
)


# Robustness
robust_cancer = find_column(
    robustness,
    ["cancer_indication", "cancer", "indication"]
)

robust_mean = find_column(
    robustness,
    ["mean_rank", "average_rank", "mean"]
)

robust_min = find_column(
    robustness,
    ["min_rank", "best_rank", "minimum_rank"]
)

robust_max = find_column(
    robustness,
    ["max_rank", "worst_rank", "maximum_rank"]
)

robust_sd = find_column(
    robustness,
    ["rank_sd", "sd_rank", "std_rank", "sd"]
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧬 Oncology Analytics")

st.sidebar.markdown(
    """
**Clinical-development opportunity screening**

This dashboard combines:

- Cancer burden
- Clinical-trial activity
- Active trials
- Sponsor breadth
- Cross-cancer drug presence
- Robustness analysis
"""
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "Cancer Landscape",
        "Drug Landscape",
        "Drug × Cancer",
        "Robustness Analysis"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Clinical-development opportunity screen. "
    "Not a financial-return forecast or investment recommendation."
)


# ============================================================
# HEADER
# ============================================================

st.title("Oncology Cancer Opportunity & Drug Portfolio Analytics")

st.markdown(
    """
A data-driven framework for screening cancer indications and
oncology drugs using epidemiology, clinical-development activity,
competitive breadth and robustness analysis.
"""
)

st.markdown("---")


# ============================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    st.header("Executive Overview")

    # KPI calculations

    if decision_cancer is not None and not cancer_decision.empty:
        cancer_count = len(cancer_decision)
    else:
        cancer_count = 0

    if not top20.empty and drug_name_col:
        drug_count = len(top20)
    elif not drug_shortlist.empty:
        drug_count = len(drug_shortlist)
    else:
        drug_count = 0

    if not drug_cancer.empty:
        pair_count = len(drug_cancer)
    else:
        pair_count = 0

    if not top20.empty and drug_trials_col:
        total_trials = pd.to_numeric(
            top20[drug_trials_col],
            errors="coerce"
        ).sum()
    else:
        total_trials = 0

    # KPI cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Tier-1 Cancer Indications",
            number_format(cancer_count)
        )

    with c2:
        st.metric(
            "Authoritative Drugs",
            number_format(drug_count)
        )

    with c3:
        st.metric(
            "Drug–Cancer Pairs",
            number_format(pair_count)
        )

    with c4:
        st.metric(
            "Trials — Top Drug Set",
            number_format(total_trials)
        )

    st.markdown("---")

    # Top drugs
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Top Cross-Cancer Drugs")

        if not top20.empty and drug_name_col:

            plot_df = top20.copy()

            if drug_rank_col:
                plot_df[drug_rank_col] = pd.to_numeric(
                    plot_df[drug_rank_col],
                    errors="coerce"
                )
                plot_df = plot_df.sort_values(
                    drug_rank_col
                )

            plot_df = plot_df.head(5)

            if drug_trials_col:
                plot_df[drug_trials_col] = pd.to_numeric(
                    plot_df[drug_trials_col],
                    errors="coerce"
                )

                fig = px.bar(
                    plot_df,
                    x=drug_trials_col,
                    y=drug_name_col,
                    orientation="h",
                    title="Top 5 Drugs by Trial Activity",
                    labels={
                        drug_trials_col: "Target Trials",
                        drug_name_col: "Drug"
                    },
                    text_auto=True
                )

                fig.update_layout(
                    yaxis={"categoryorder": "total ascending"}
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

    with col2:

        st.subheader("Tier-1 Cancer Opportunities")

        if not cancer_decision.empty:

            display_df = cancer_decision.copy()

            if decision_rank:
                display_df[decision_rank] = pd.to_numeric(
                    display_df[decision_rank],
                    errors="coerce"
                )
                display_df = display_df.sort_values(
                    decision_rank
                )

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

    # Epidemiology chart

    st.subheader("Cancer Burden")

    if not epidemiology.empty and epi_cancer:

        burden_df = epidemiology.copy()

        if epi_incidence:
            burden_df[epi_incidence] = pd.to_numeric(
                burden_df[epi_incidence],
                errors="coerce"
            )

        if epi_deaths:
            burden_df[epi_deaths] = pd.to_numeric(
                burden_df[epi_deaths],
                errors="coerce"
            )

        if epi_incidence and epi_deaths:

            fig = px.scatter(
                burden_df,
                x=epi_incidence,
                y=epi_deaths,
                size=epi_incidence,
                hover_name=epi_cancer,
                title="Cancer Incidence vs Deaths",
                labels={
                    epi_incidence: "Incidence Cases",
                    epi_deaths: "Deaths"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.info(
        "Interpretation: the dashboard identifies clinical-development "
        "signals. Trial activity should not be interpreted as equivalent "
        "to market demand, revenue or investment return."
    )


# ============================================================
# PAGE 2 — CANCER LANDSCAPE
# ============================================================

elif page == "Cancer Landscape":

    st.header("Cancer Landscape")

    if not epidemiology.empty and epi_cancer:

        st.subheader("Cancer Burden")

        burden = epidemiology.copy()

        if epi_incidence:
            burden[epi_incidence] = pd.to_numeric(
                burden[epi_incidence],
                errors="coerce"
            )

        if epi_deaths:
            burden[epi_deaths] = pd.to_numeric(
                burden[epi_deaths],
                errors="coerce"
            )

        if epi_incidence:

            fig = px.bar(
                burden.sort_values(
                    epi_incidence,
                    ascending=False
                ),
                x=epi_cancer,
                y=epi_incidence,
                title="Cancer Incidence",
                labels={
                    epi_cancer: "Cancer",
                    epi_incidence: "Incidence Cases"
                }
            )

            fig.update_layout(
                xaxis_tickangle=-45
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.subheader("Clinical Competition")

    if not competitive.empty and comp_cancer:

        comp = competitive.copy()

        if comp_trials:
            comp[comp_trials] = pd.to_numeric(
                comp[comp_trials],
                errors="coerce"
            )

        if comp_sponsors:
            comp[comp_sponsors] = pd.to_numeric(
                comp[comp_sponsors],
                errors="coerce"
            )

        if comp_trials and comp_sponsors:

            fig = px.scatter(
                comp,
                x=comp_trials,
                y=comp_sponsors,
                size=comp_trials,
                hover_name=comp_cancer,
                title="Trial Activity vs Sponsor Breadth",
                labels={
                    comp_trials: "Clinical Trials",
                    comp_sponsors: "Sponsors"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.subheader("Competitive Landscape Table")

        st.dataframe(
            competitive,
            use_container_width=True,
            hide_index=True
        )

        show_download(
            competitive,
            "cancer_competitive_landscape.csv"
        )


# ============================================================
# PAGE 3 — DRUG LANDSCAPE
# ============================================================

elif page == "Drug Landscape":

    st.header("Drug Opportunity Landscape")

    if top20.empty:

        st.warning("Top-20 drug dataset could not be loaded.")

    else:

        # Filters
        if drug_rank_col:
            rank_values = pd.to_numeric(
                top20[drug_rank_col],
                errors="coerce"
            )

            max_rank = int(
                rank_values.dropna().max()
            )

            selected_rank = st.slider(
                "Show top N drugs",
                min_value=5,
                max_value=max_rank,
                value=min(20, max_rank)
            )

            drug_view = top20[
                rank_values <= selected_rank
            ].copy()

        else:
            drug_view = top20.copy()

        # Chart
        if drug_name_col and drug_score_col:

            drug_view[drug_score_col] = pd.to_numeric(
                drug_view[drug_score_col],
                errors="coerce"
            )

            fig = px.bar(
                drug_view.sort_values(
                    drug_score_col
                ),
                x=drug_score_col,
                y=drug_name_col,
                orientation="h",
                title="Authoritative Drug Opportunity Ranking",
                labels={
                    drug_score_col: "Opportunity Score",
                    drug_name_col: "Drug"
                },
                text_auto=".2f"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.subheader("Drug Metrics")

        columns_to_show = [
            c for c in [
                drug_rank_col,
                drug_name_col,
                drug_cancers_col,
                drug_trials_col,
                drug_active_col,
                drug_completed_col,
                drug_sponsors_col,
                drug_score_col
            ]
            if c is not None
        ]

        st.dataframe(
            drug_view[columns_to_show],
            use_container_width=True,
            hide_index=True
        )

        show_download(
            drug_view,
            "filtered_drug_opportunity.csv"
        )


# ============================================================
# PAGE 4 — DRUG × CANCER
# ============================================================

elif page == "Drug × Cancer":

    st.header("Drug × Cancer Analysis")

    if drug_cancer.empty:

        st.warning(
            "Drug-cancer trial metrics could not be loaded."
        )

    else:

        dc_view = drug_cancer.copy()

        # Cancer selector
        if dc_cancer:

            cancer_values = sorted(
                dc_view[dc_cancer]
                .dropna()
                .astype(str)
                .unique()
            )

            selected_cancer = st.selectbox(
                "Select cancer indication",
                ["All"] + cancer_values
            )

            if selected_cancer != "All":

                dc_view = dc_view[
                    dc_view[dc_cancer].astype(str)
                    == selected_cancer
                ]

        # Drug selector
        if dc_drug and not dc_view.empty:

            drug_values = sorted(
                dc_view[dc_drug]
                .dropna()
                .astype(str)
                .unique()
            )

            selected_drug = st.selectbox(
                "Select drug",
                ["All"] + drug_values
            )

            if selected_drug != "All":

                dc_view = dc_view[
                    dc_view[dc_drug].astype(str)
                    == selected_drug
                ]

        st.subheader("Filtered Drug–Cancer Relationships")

        st.dataframe(
            dc_view,
            use_container_width=True,
            hide_index=True
        )

        # Trial chart
        if (
            dc_drug
            and dc_trials
            and not dc_view.empty
        ):

            chart_df = dc_view.copy()

            chart_df[dc_trials] = pd.to_numeric(
                chart_df[dc_trials],
                errors="coerce"
            )

            chart_df = chart_df.sort_values(
                dc_trials,
                ascending=False
            ).head(20)

            fig = px.bar(
                chart_df,
                x=dc_trials,
                y=dc_drug,
                orientation="h",
                title="Top Drug–Cancer Trial Activity",
                labels={
                    dc_trials: "Trials",
                    dc_drug: "Drug"
                }
            )

            fig.update_layout(
                yaxis={"categoryorder": "total ascending"}
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        show_download(
            dc_view,
            "filtered_drug_cancer_metrics.csv"
        )


# ============================================================
# PAGE 5 — ROBUSTNESS
# ============================================================

elif page == "Robustness Analysis":

    st.header("Robustness & Sensitivity Analysis")

    st.markdown(
        """
        Robustness analysis examines whether cancer rankings remain
        relatively stable under different analytical scenarios.
        """
    )

    if robustness.empty:

        st.warning(
            "Robustness ranking data could not be loaded."
        )

    else:

        robust_view = robustness.copy()

        # Mean rank chart
        if robust_cancer and robust_mean:

            robust_view[robust_mean] = pd.to_numeric(
                robust_view[robust_mean],
                errors="coerce"
            )

            chart_df = robust_view.sort_values(
                robust_mean
            ).head(15)

            fig = px.bar(
                chart_df.sort_values(
                    robust_mean,
                    ascending=False
                ),
                x=robust_mean,
                y=robust_cancer,
                orientation="h",
                title="Mean Scenario Rank",
                labels={
                    robust_mean: "Mean Rank",
                    robust_cancer: "Cancer"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # Stability chart
        if (
            robust_cancer
            and robust_min
            and robust_max
        ):

            for col in [
                robust_min,
                robust_max
            ]:
                robust_view[col] = pd.to_numeric(
                    robust_view[col],
                    errors="coerce"
                )

            range_df = robust_view.sort_values(
                robust_min
            ).head(15)

            fig = go.Figure()

            for _, row in range_df.iterrows():

                cancer = row[robust_cancer]
                min_rank = row[robust_min]
                max_rank = row[robust_max]

                fig.add_trace(
                    go.Scatter(
                        x=[min_rank, max_rank],
                        y=[cancer, cancer],
                        mode="lines+markers",
                        name=str(cancer),
                        showlegend=False
                    )
                )

            fig.update_layout(
                title="Best-to-Worst Scenario Rank Range",
                xaxis_title="Rank",
                yaxis_title="Cancer"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.subheader("Robustness Ranking Table")

        st.dataframe(
            robust_view,
            use_container_width=True,
            hide_index=True
        )

        show_download(
            robust_view,
            "robustness_analysis.csv"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Oncology Cancer Opportunity & Drug Portfolio Analytics | "
    "Clinical-development opportunity screening"
)

st.caption(
    "This dashboard does not establish commercial ROI, "
    "clinical efficacy, or investment returns."
)