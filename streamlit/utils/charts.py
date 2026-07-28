import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Professional Corporate Palette - High Contrast
COLOR_RETAINED = "#059669"   # Emerald Green
COLOR_CHURNED = "#DC2626"    # Crimson Red
COLOR_PRIMARY = "#4F46E5"    # Indigo
COLOR_AMBER = "#D97706"      # Amber
COLOR_SLATE = "#475569"      # Slate

def apply_corporate_theme(fig: go.Figure):
    """
    Applies unified corporate layout and styling to Plotly figures with generous spacing
    to prevent title and legend overlap.
    """
    fig.update_layout(
        font=dict(family="Inter, sans-serif", size=12, color="#0F172A"),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#F8FAFC",
        margin=dict(l=40, r=40, t=65, b=70),
        xaxis=dict(
            gridcolor="#E2E8F0",
            zerolinecolor="#CBD5E1",
            showline=True,
            linecolor="#CBD5E1",
            tickfont=dict(size=11, color="#334155")
        ),
        yaxis=dict(
            gridcolor="#E2E8F0",
            zerolinecolor="#CBD5E1",
            showline=True,
            linecolor="#CBD5E1",
            tickfont=dict(size=11, color="#334155")
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="center",
            x=0.5,
            title_text="",  # Remove redundant field title in legend
            font=dict(size=11, color="#1E293B")
        ),
        title=dict(
            font=dict(size=15, color="#0F172A", family="Inter"),
            y=0.96,
            x=0.01,
            xanchor="left"
        )
    )
    return fig

def create_gauge_chart(probability: float) -> go.Figure:
    """
    Creates a clean Plotly Gauge chart displaying churn probability percentage.
    """
    score = probability * 100

    if score < 35:
        bar_color = COLOR_RETAINED
    elif score < 65:
        bar_color = COLOR_AMBER
    else:
        bar_color = COLOR_CHURNED

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': "%", 'font': {'size': 34, 'color': bar_color, 'family': 'Inter'}},
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Predicted Churn Probability", 'font': {'size': 15, 'color': "#0F172A", 'family': 'Inter'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#64748B"},
            'bar': {'color': bar_color, 'thickness': 0.28},
            'bgcolor': "#F8FAFC",
            'borderwidth': 1,
            'bordercolor': "#CBD5E1",
            'steps': [
                {'range': [0, 35], 'color': "rgba(16, 185, 129, 0.15)"},
                {'range': [35, 65], 'color': "rgba(245, 158, 11, 0.15)"},
                {'range': [65, 100], 'color': "rgba(220, 38, 38, 0.15)"}
            ],
            'threshold': {
                'line': {'color': COLOR_CHURNED, 'width': 3},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))

    fig.update_layout(
        height=280,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font=dict(family="Inter, sans-serif")
    )
    return fig

def create_churn_pie_chart(df: pd.DataFrame) -> go.Figure:
    """
    Creates a clean donut pie chart showing churned vs retained customer distribution.
    """
    churn_counts = df['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn_Status', 'Count']
    churn_counts['Label'] = churn_counts['Churn_Status'].map({0: 'Retained', 1: 'Churned'})

    fig = px.pie(
        churn_counts,
        names='Label',
        values='Count',
        color='Label',
        color_discrete_map={'Retained': COLOR_RETAINED, 'Churned': COLOR_CHURNED},
        hole=0.48,
        title="Customer Retention Breakdown"
    )

    fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#FFFFFF', width=2)))
    fig = apply_corporate_theme(fig)
    fig.update_layout(height=380)
    return fig

def create_complaint_churn_chart(df: pd.DataFrame) -> go.Figure:
    """
    Bar chart showing churn rate by complaint status.
    """
    temp_df = df.copy()
    temp_df['Complaint_Status'] = temp_df['Complains'].map({0: 'No Complaint Logged', 1: 'Complaint Logged'})
    temp_df['Churn_Label'] = temp_df['Churn'].map({0: 'Retained', 1: 'Churned'})

    grouped = temp_df.groupby(['Complaint_Status', 'Churn_Label']).size().reset_index(name='Count')

    fig = px.bar(
        grouped,
        x='Complaint_Status',
        y='Count',
        color='Churn_Label',
        barmode='group',
        color_discrete_map={'Retained': COLOR_RETAINED, 'Churned': COLOR_CHURNED},
        title="Customer Churn by Complaint History",
        labels={'Complaint_Status': 'Complaint Status', 'Count': 'Customer Count', 'Churn_Label': 'Status'}
    )
    fig = apply_corporate_theme(fig)
    fig.update_layout(height=380)
    return fig

def create_usage_scatter_chart(df: pd.DataFrame) -> go.Figure:
    """
    Scatter chart comparing Seconds of Use vs Customer Value colored by Churn status.
    """
    temp_df = df.copy()
    temp_df['Status_Label'] = temp_df['Churn'].map({0: 'Retained', 1: 'Churned'})

    fig = px.scatter(
        temp_df,
        x='Seconds of Use',
        y='Customer Value',
        color='Status_Label',
        color_discrete_map={'Retained': COLOR_RETAINED, 'Churned': COLOR_CHURNED},
        opacity=0.75,
        title="Customer Usage Duration vs Revenue Value",
        labels={'Status_Label': 'Churn Status', 'Seconds of Use': 'Total Seconds of Use', 'Customer Value': 'Customer Value Score'}
    )
    fig = apply_corporate_theme(fig)
    fig.update_layout(height=390)
    return fig

def create_tenure_cohort_chart(df: pd.DataFrame) -> go.Figure:
    """
    Bar chart showing Churn Rate across Subscription Tenure brackets.
    """
    temp_df = df.copy()
    bins = [0, 12, 24, 36, 48, 60]
    labels = ['0-12 M', '13-24 M', '25-36 M', '37-48 M', '49-60 M']
    temp_df['Tenure_Bracket'] = pd.cut(temp_df['Subscription Length'], bins=bins, labels=labels)
    
    cohort = temp_df.groupby('Tenure_Bracket')['Churn'].agg(['count', 'mean']).reset_index()
    cohort['Churn_Rate'] = cohort['mean'] * 100

    fig = px.bar(
        cohort,
        x='Tenure_Bracket',
        y='Churn_Rate',
        text=cohort['Churn_Rate'].apply(lambda x: f"{x:.1f}%"),
        title="Churn Rate by Subscription Tenure Cohort",
        labels={'Tenure_Bracket': 'Subscription Tenure', 'Churn_Rate': 'Churn Rate (%)'},
        color='Churn_Rate',
        color_continuous_scale='Reds'
    )
    fig.update_traces(textposition='outside')
    fig = apply_corporate_theme(fig)
    fig.update_layout(height=380, coloraxis_showscale=False)
    return fig

def create_feature_importance_chart(df_feat: pd.DataFrame, importance_col: str = None) -> go.Figure:
    """
    Bar chart showing Top Feature Importance.
    """
    if importance_col and importance_col in df_feat.columns:
        col_to_use = importance_col
    elif 'Importance' in df_feat.columns:
        col_to_use = 'Importance'
    elif 'Importance_XGBoost' in df_feat.columns:
        col_to_use = 'Importance_XGBoost'
    else:
        numeric_cols = df_feat.select_dtypes(include=['number']).columns
        col_to_use = numeric_cols[0] if len(numeric_cols) > 0 else df_feat.columns[1]

    df_sorted = df_feat.sort_values(by=col_to_use, ascending=True)

    fig = px.bar(
        df_sorted,
        x=col_to_use,
        y='Feature',
        orientation='h',
        title=f"Feature Importance ({col_to_use.replace('_', ' ')})",
        color=col_to_use,
        color_continuous_scale='Cividis',
        labels={col_to_use: 'Importance Score'}
    )
    fig = apply_corporate_theme(fig)
    fig.update_layout(height=400, coloraxis_showscale=False)
    return fig

def create_feature_contribution_chart(df_contrib: pd.DataFrame) -> go.Figure:
    """
    Creates a bar chart showing relative feature risk weights for a single customer.
    """
    fig = px.bar(
        df_contrib,
        x='Importance_Weight',
        y='Feature',
        orientation='h',
        title="Feature Influence Breakdown on Churn Model Score",
        color='Importance_Weight',
        color_continuous_scale='Blues',
        labels={'Importance_Weight': 'Model Feature Weight'}
    )
    fig = apply_corporate_theme(fig)
    fig.update_layout(height=360, coloraxis_showscale=False)
    return fig
