import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server
app.title = "ENG Schools"

# App parameters
topn = 10  # Show highest n values
chart_h = 500  # height of charts
datatable_rows = 100
textcol = "steelblue"  # text colour
bgcol = "black"  # background colour of charts, table etc.
fontsize = 16

col_1 = "royalblue"
col_2 = "slategrey"
col_3 = "blueviolet"
col_4 = "cornflowerblue"
col_5 = "darkmagenta"
col_6 = "slateblue"

tabs_styles = {
    "height": "40px"
}
tab_style = {
    "color": "grey",
    "fontWeight": "bold"
}

tab_selected_style = {
    "color": "white",
    "backgroundColor": "royalblue",
    "fontWeight": "bold"
}

df = pd.read_csv("england_ks2final.csv")
df_pri = df[df["RECTYPE"].isin(["1", "2"])]  # mainstream & special schools

df = pd.read_csv("england_ks4final.csv")
df_sec = df[df["RECTYPE"].isin(["1", "2"])]  # mainstream & special schools

df = pd.read_csv("england_ks5final.csv", )
df_p16 = df[df["RECTYPE"].isin(["1", "2"])]  # mainstream & special schools

df_eng_avg = pd.read_csv("england_gcse_alevel_averages.csv")

school_list1 = sorted([str(d) for d in df_pri["SCHNAME"].unique()])
school_list2 = sorted([str(d) for d in df_sec["SCHNAME"].unique()])
school_list3 = sorted([str(d) for d in df_p16["SCHNAME"].unique()])
school_list = []
for i in school_list1:
    school_list.append(i)
for i in school_list2:
    if i not in school_list:
        school_list.append(i)
for i in school_list3:
    if i not in school_list:
        school_list.append(i)
school_list.sort()

town_list = sorted([str(d) for d in df_pri["TOWN"].unique()])
postcode_list = sorted([str(d) for d in df_pri["PCODE2"].unique()])

# Rename columns
df_pri = df_pri.rename(columns=
{
    "SCHNAME": "School",
    "TOWN": "Town",
    "PCODE": "Post Code",
    "READPROG": "Reading Score",
    "READPROG_DESCR": "Reading",
    "WRITPROG": "Writing Score",
    "WRITPROG_DESCR": "Writing",
    "MATPROG": "Maths Score",
    "MATPROG_DESCR": "Maths",
    "OFSTEDRATING": "Ofsted",
    "INSPECTIONDT": "Last Inspection",
    "WEB": "Website"
}
)

df_sec = df_sec.rename(columns=
{
    "SCHNAME": "School",
    "TOWN": "Town",
    "PCODE": "Post Code",
    "P8MEA": "Progress 8",
    "P8_BANDING": "Prog8",
    "ATT8SCR": "Attainment 8",
    "PTL2BASICS_95": "Eng Maths Grade 5+",
    "PTEBACC_E_PTQ_EE": "Entering EBacc",
    "EBACCAPS": "EBacc Score",
    "OFSTEDRATING": "Ofsted",
    "INSPECTIONDT": "Last Inspection",
    "WEB": "Website"
}
)

df_p16 = df_p16.rename(columns=
{
    "SCHNAME": "School",
    "TOWN": "Town",
    "PCODE": "Post Code",
    "VA_INS_ALEV": "Progress Score",
    "PROGRESS_BAND_ALEV": "Prog_Band",
    "TALLPPEGRD_ALEV_1618": "Average Grade",
    "TALLPPE_ALEV_1618": "Average Points",
    "OFSTEDRATING": "Ofsted",
    "INSPECTIONDT": "Last Inspection",
    "WEB": "Website"
}
)

df_tbl_pri = df_pri.copy()
df_tbl_sec = df_sec.copy()
df_tbl_p16 = df_p16.copy()

# Layout ----------
app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H1("ENG Schools (2018/19)"), style={"text-align": "center", "font-weight": "bold"})),

        html.Br(),

        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                    id="school_drop",
                    options=[{"label": i, "value": i} for i in school_list],
                    multi=True,
                    placeholder="Select School",
                    style={"font-size": fontsize, "color": "black", "background-color": "white"}
                )
                ),

                dbc.Col(dcc.Dropdown(
                    id="town_drop",
                    options=[{"label": i, "value": i} for i in town_list],
                    multi=True,
                    placeholder="Select Town",
                    style={"font-size": fontsize, "color": "black", "background-color": "white"}
                )
                ),

                dbc.Col(dcc.Dropdown(
                    id="postcode_drop",
                    options=[{"label": i, "value": i} for i in postcode_list],
                    multi=True,
                    placeholder="Select Postcode District",
                    style={"font-size": fontsize, "color": "black", "background-color": "white"}
                )
                )
            ],
            style={"padding": "0px 20px 0px 20px"}
        ),

        html.Br(),

        dbc.Row(dbc.Col(html.P(
            "📗✏️📐👨‍🎓 Score: ⭐⭐⭐⭐⭐ Well Above Average | ⭐⭐⭐⭐ Above Average | ⭐⭐⭐ Average | ⭐⭐ Below Average | ⭐ Well Below Average"
        ), style={"text-align": "left", "font-weight": "bold", "padding": "0px 20px 0px 20px"})),

        dbc.Row(dbc.Col(html.P(
            "🏫Ofsted: 🎓🎓🎓🎓🎓 Outstanding | 🎓🎓🎓🎓 Good | 🎓🎓🎓 Satisfactory | 🎓🎓 Requires Improvement | 🎓 Inadequate"
        ), style={"text-align": "left", "font-weight": "bold", "padding": "0px 20px 0px 20px"})),

        dcc.Tabs(
            [
                dcc.Tab(
                    label="PRIMARY",
                    id="primary_tab",
                    style=tab_style, selected_style=tab_selected_style,
                    children=[
                        html.Br(),

                        html.Div(
                            [
                                dash_table.DataTable(
                                    id="datatable_pri",
                                    # columns=[{"name": i, "id": i} for i in df_tbl_pri],
                                    columns=[
                                        {
                                            "id": "Row",
                                            "name": ["Row"],
                                            "type": "numeric"
                                        },
                                        {
                                            "id": "School",
                                            "name": ["School"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Town",
                                            "name": ["Town"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Post Code",
                                            "name": ["Post Code"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Reading",
                                            "name": ["📗Reading"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Writing",
                                            "name": ["✏️Writing"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Maths",
                                            "name": ["📐Maths"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Ofsted",
                                            "name": ["🏫Ofsted Rating"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Last Inspected",
                                            "name": ["Last Inspected"],
                                            "type": "datetime"
                                        }
                                    ],
                                    merge_duplicate_headers=True,
                                    sort_action="native",  # native / none
                                    sort_mode="single",  # single / multi
                                    filter_action="none",  # native / none
                                    page_action="native",  # native / none
                                    page_current=0,  # current page number
                                    page_size=datatable_rows,  # rows per page
                                    fill_width=True,
                                    style_cell={
                                        # ensure adequate header width when text is shorter than cell's text
                                        "minWidth": 95, "maxWidth": 95, "width": 95,
                                        "backgroundColor": bgcol,
                                        "color": textcol,
                                        "font-family": "Verdana",
                                        # "fontWeight": "bold",
                                        "font_size": fontsize,
                                        "height": "30px",
                                        "maxWidth": "500px",
                                        "padding": "00px 10px 0px 10px"
                                    },
                                    style_cell_conditional=[
                                        {"if": {"column_id": "Row"},
                                         "width": "5%"},
                                    ],
                                    fixed_rows={"headers": True},
                                    style_data={  # wrap long cell content into multiple lines
                                        "whiteSpace": "normal",
                                        "height": "auto"
                                    },
                                    style_table={"overflowX": "auto", "overflowY": "auto"},  # "height": "500px",
                                    css=[{"selector": ".row", "rule": "margin: 0"}],  # fix text clipping issue
                                    style_header={"color": "white", "backgroundColor": textcol},
                                    style_as_list_view=True
                                )
                            ], style={"padding": "0px 20px 0px 20px"}
                        )
                    ]
                ),

                dcc.Tab(
                    label="SECONDARY",
                    id="secondary_tab",
                    style=tab_style, selected_style=tab_selected_style,
                    children=[
                        html.Br(),

                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.H3("GCSE Attainment 8", className="card-title"),
                                            html.H2(
                                                id="gcse_att8_avg",
                                                className="card-value",
                                                style={"font-weight": "bold"}
                                            )
                                        ],
                                        style={"color": "white",
                                               "background": col_1,
                                               "text-align": "center"
                                               }
                                    )
                                ),

                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.H3("Eng/Maths Grade5+", className="card-title"),
                                            html.H2(
                                                id="gcse_eng_maths_grade5_pct",
                                                className="card-value",
                                                style={"font-weight": "bold"}
                                            )
                                        ],
                                        style={"color": "white",
                                               "background": col_2,
                                               "text-align": "center"
                                               }
                                    )
                                ),

                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.H3("GCSE Entering EBacc", className="card-title"),
                                            html.H2(
                                                id="gcse_entering_ebacc",
                                                className="card-value",
                                                style={"font-weight": "bold"}
                                            )
                                        ],
                                        style={"color": "white",
                                               "background": col_3,
                                               "text-align": "center"
                                               }
                                    )
                                ),

                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.H3("GCSE EBacc Score", className="card-title"),
                                            html.H2(
                                                id="gcse_ebacc_score",
                                                className="card-value",
                                                style={"font-weight": "bold"}
                                            )
                                        ],
                                        style={"color": "white",
                                               "background": col_4,
                                               "text-align": "center"
                                               }
                                    )
                                )
                            ],
                            className="mb-3",
                            style={"padding": "0px 20px 0px 20px"}
                        ),

                        html.Div(
                            [
                                dash_table.DataTable(
                                    id="datatable_sec",
                                    # columns=[{"name": i, "id": i} for i in df_tbl_pri],
                                    columns=[
                                        {
                                            "id": "Row",
                                            "name": ["Row"],
                                            "type": "numeric"
                                        },
                                        {
                                            "id": "School",
                                            "name": ["School"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Town",
                                            "name": ["Town"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Post Code",
                                            "name": ["Post Code"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Prog 8 Band",
                                            "name": ["👨‍🎓Progress 8"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Attainment 8",
                                            "name": ["Attainment 8 Score"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Eng Maths Grade 5+",
                                            "name": ["Eng/Maths Grade 5+"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Entering EBacc",
                                            "name": ["Entering EBacc"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "EBacc Score",
                                            "name": ["EBacc Score"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Ofsted",
                                            "name": ["🏫Ofsted Rating"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Last Inspected",
                                            "name": ["Last Inspected"],
                                            "type": "text"
                                        }
                                    ],
                                    merge_duplicate_headers=True,
                                    sort_action="native",  # native / none
                                    sort_mode="single",  # single / multi
                                    filter_action="none",  # native / none
                                    page_action="native",  # native / none
                                    page_current=0,  # current page number
                                    page_size=datatable_rows,  # rows per page
                                    fill_width=True,
                                    style_cell={
                                        # ensure adequate header width when text is shorter than cell's text
                                        "minWidth": 95, "maxWidth": 95, "width": 95,
                                        "backgroundColor": bgcol,
                                        "color": textcol,
                                        "font-family": "Verdana",
                                        # "fontWeight": "bold",
                                        "font_size": fontsize,
                                        "height": "30px",
                                        "maxWidth": "500px",
                                        "padding": "00px 10px 0px 10px"
                                    },
                                    style_cell_conditional=[
                                        {"if": {"column_id": "Row"},
                                         "width": "5%"},
                                        {"if": {"column_id": "Attainment 8"},
                                         "color": "white",
                                         "backgroundColor": col_1},
                                        {"if": {"column_id": "Eng Maths Grade 5+"},
                                         "color": "white",
                                         "backgroundColor": col_2},
                                        {"if": {"column_id": "Entering EBacc"},
                                         "color": "white",
                                         "backgroundColor": col_3},
                                        {"if": {"column_id": "EBacc Score"},
                                         "color": "white",
                                         "backgroundColor": col_4}
                                    ],
                                    fixed_rows={"headers": True},
                                    style_data={  # wrap long cell content into multiple lines
                                        "whiteSpace": "normal",
                                        "height": "auto"
                                    },
                                    style_table={"overflowX": "auto", "overflowY": "auto"},  # "height": "500px",
                                    css=[{"selector": ".row", "rule": "margin: 0"}],  # fix text clipping issue
                                    style_header={"color": "white", "backgroundColor": textcol},
                                    style_as_list_view=True
                                )
                            ], style={"padding": "0px 20px 0px 20px"}
                        )
                    ]
                ),

                dcc.Tab(
                    label="POST 16",
                    id="post16_tab",
                    style=tab_style, selected_style=tab_selected_style,
                    children=[
                        html.Br(),

                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.H3("Average A-Level Grade", className="card-title"),
                                            html.H2(
                                                id="alevel_grade_avg",
                                                className="card-value",
                                                style={"font-weight": "bold"}
                                            )
                                        ],
                                        style={"color": "white",
                                               "background": col_5,
                                               "text-align": "center"
                                               }
                                    )
                                ),

                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.H3("Average A-Level Score", className="card-title"),
                                            html.H2(
                                                id="alevel_score_avg",
                                                className="card-value",
                                                style={"font-weight": "bold"}
                                            )
                                        ],
                                        style={"color": "white",
                                               "background": col_6,
                                               "text-align": "center"
                                               }
                                    )
                                )
                            ],
                            className="mb-3",
                            style={"padding": "0px 20px 0px 20px"}
                        ),

                        html.Div(
                            [
                                dash_table.DataTable(
                                    id="datatable_p16",
                                    # columns=[{"name": i, "id": i} for i in df_tbl_pri],
                                    columns=[
                                        {
                                            "id": "Row",
                                            "name": ["Row"],
                                            "type": "numeric"
                                        },
                                        {
                                            "id": "School",
                                            "name": ["School"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Town",
                                            "name": ["Town"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Post Code",
                                            "name": ["Post Code"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Prog Band",
                                            "name": ["👨‍🎓Progress"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Average Grade",
                                            "name": ["Average Grade"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Average Points",
                                            "name": ["Average Points"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Ofsted",
                                            "name": ["🏫Ofsted Rating"],
                                            "type": "text"
                                        },
                                        {
                                            "id": "Last Inspected",
                                            "name": ["Last Inspected"],
                                            "type": "text"
                                        }
                                    ],
                                    merge_duplicate_headers=True,
                                    sort_action="native",  # native / none
                                    sort_mode="single",  # single / multi
                                    filter_action="none",  # native / none
                                    page_action="native",  # native / none
                                    page_current=0,  # current page number
                                    page_size=datatable_rows,  # rows per page
                                    fill_width=True,
                                    style_cell={
                                        # ensure adequate header width when text is shorter than cell's text
                                        "minWidth": 95, "maxWidth": 95, "width": 95,
                                        "backgroundColor": bgcol,
                                        "color": textcol,
                                        "font-family": "Verdana",
                                        # "fontWeight": "bold",
                                        "font_size": fontsize,
                                        "height": "30px",
                                        "maxWidth": "500px",
                                        "padding": "00px 10px 0px 10px"
                                    },
                                    style_cell_conditional=[
                                        {"if": {"column_id": "Row"},
                                         "width": "5%"},
                                        {"if": {"column_id": "Average Grade"},
                                         "color": "white",
                                         "backgroundColor": col_5},
                                        {"if": {"column_id": "Average Points"},
                                         "color": "white",
                                         "backgroundColor": col_6}
                                    ],
                                    fixed_rows={"headers": True},
                                    style_data={  # wrap long cell content into multiple lines
                                        "whiteSpace": "normal",
                                        "height": "auto"
                                    },
                                    style_table={"overflowX": "auto", "overflowY": "auto"},  # "height": "500px",
                                    css=[{"selector": ".row", "rule": "margin: 0"}],  # fix text clipping issue
                                    style_header={"color": "white", "backgroundColor": textcol},
                                    style_as_list_view=True
                                )
                            ], style={"padding": "0px 20px 0px 20px"}
                        )
                    ]
                )
            ]
        ),

        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row(html.Label(["* May take several seconds for initial load"]),
                style={"font-style": "italic", "padding": "0px 0px 0px 50px"}
                ),

        dbc.Row(html.Label(["Data Source: ",
                            html.A("GovUK", href="https://www.compare-school-performance.service.gov.uk/download-data", target="_blank")]),
                style={"padding": "0px 0px 0px 50px"}
                ),

        dbc.Row(html.Label(["Code: ",
                            html.A("Github", href="https://github.com/waiky8/eng-schools", target="_blank")]),
                style={"padding": "0px 0px 0px 50px"}
                ),

        html.Div(id="dummy", children=[], style={"display": "none"})  # dummy DIV to trigger totals_timeline callback
    ]
)


# Data Table ----------
@app.callback(
    [
        Output("datatable_pri", "data"),
        Output("datatable_sec", "data"),
        Output("datatable_p16", "data")
    ],
    [
        Input("school_drop", "value"),
        Input("town_drop", "value"),
        Input("postcode_drop", "value")
    ]
)
def update_datatable(selected_school, selected_area, selected_postcode):
    # Check for school filter entered
    if (selected_school is None or selected_school == []):
        df1a = df_tbl_pri
        df2a = df_tbl_sec
        df3a = df_tbl_p16
    else:
        df1a = df_pri[df_pri["School"].isin(selected_school)]
        df2a = df_sec[df_sec["School"].isin(selected_school)]
        df3a = df_p16[df_p16["School"].isin(selected_school)]

    # Check for town filter entered
    if (selected_area is None or selected_area == []):
        df1b = df1a
        df2b = df2a
        df3b = df3a
    else:
        df1b = df1a[df1a["Town"].isin(selected_area)]
        df2b = df2a[df2a["Town"].isin(selected_area)]
        df3b = df3a[df3a["Town"].isin(selected_area)]

    # Check for postcode filter entered
    if (selected_postcode is None or selected_postcode == []):
        df1c = df1b
        df2c = df2b
        df3c = df3b
    else:
        df1c = df1b[df1b["PCODE2"].isin(selected_postcode)]
        df2c = df2b[df2b["PCODE2"].isin(selected_postcode)]
        df3c = df3b[df3b["PCODE2"].isin(selected_postcode)]

    df1_pri = df1c.copy().sort_values(by=["School"])
    # Refresh row no.
    df1_pri["Row"] = df1_pri.reset_index().index
    df1_pri["Row"] += 1
    if len(df1_pri) == 0:
        pass
    else:
        # Map reading progress to stars
        df1_pri.loc[(df1_pri.Reading == "1"), "Reading"] = "⭐⭐⭐⭐⭐"
        df1_pri.loc[(df1_pri.Reading == "2"), "Reading"] = "⭐⭐⭐⭐"
        df1_pri.loc[(df1_pri.Reading == "3"), "Reading"] = "⭐⭐⭐"
        df1_pri.loc[(df1_pri.Reading == "4"), "Reading"] = "⭐⭐"
        df1_pri.loc[(df1_pri.Reading == "5"), "Reading"] = "⭐"
        # Map writing progress to stars
        df1_pri.loc[(df1_pri.Writing == "1"), "Writing"] = "⭐⭐⭐⭐⭐"
        df1_pri.loc[(df1_pri.Writing == "2"), "Writing"] = "⭐⭐⭐⭐"
        df1_pri.loc[(df1_pri.Writing == "3"), "Writing"] = "⭐⭐⭐"
        df1_pri.loc[(df1_pri.Writing == "4"), "Writing"] = "⭐⭐"
        df1_pri.loc[(df1_pri.Writing == "5"), "Writing"] = "⭐"
        # Map maths progress to stars
        df1_pri.loc[(df1_pri.Maths == "1"), "Maths"] = "⭐⭐⭐⭐⭐"
        df1_pri.loc[(df1_pri.Maths == "2"), "Maths"] = "⭐⭐⭐⭐"
        df1_pri.loc[(df1_pri.Maths == "3"), "Maths"] = "⭐⭐⭐"
        df1_pri.loc[(df1_pri.Maths == "4"), "Maths"] = "⭐⭐"
        df1_pri.loc[(df1_pri.Maths == "5"), "Maths"] = "⭐"
        # Map ofsted rating to stars
        df1_pri.loc[(df1_pri.Ofsted == "Outstanding"), "Ofsted"] = "🎓🎓🎓🎓🎓"
        df1_pri.loc[(df1_pri.Ofsted == "Good"), "Ofsted"] = "🎓🎓🎓🎓"
        df1_pri.loc[(df1_pri.Ofsted == "Satisfactory"), "Ofsted"] = "🎓🎓🎓"
        df1_pri.loc[(df1_pri.Ofsted == "Requires Improvement"), "Ofsted"] = "🎓🎓"
        df1_pri.loc[(df1_pri.Ofsted == "Inadequate"), "Ofsted"] = "🎓"

    df2_sec = df2c.copy().sort_values(by=["School"])
    # Refresh row no.
    df2_sec["Row"] = df2_sec.reset_index().index
    df2_sec["Row"] += 1
    if len(df2_sec) == 0:
        pass
    else:
        # Map progress 8 to stars
        df2_sec.loc[(df2_sec.Prog8 == "1"), "Prog 8 Band"] = "⭐⭐⭐⭐⭐"
        df2_sec.loc[(df2_sec.Prog8 == "2"), "Prog 8 Band"] = "⭐⭐⭐⭐"
        df2_sec.loc[(df2_sec.Prog8 == "3"), "Prog 8 Band"] = "⭐⭐⭐"
        df2_sec.loc[(df2_sec.Prog8 == "4"), "Prog 8 Band"] = "⭐⭐"
        df2_sec.loc[(df2_sec.Prog8 == "5"), "Prog 8 Band"] = "⭐"
        # Map ofsted rating to stars
        df2_sec.loc[(df2_sec.Ofsted == "Outstanding"), "Ofsted"] = "🎓🎓🎓🎓🎓"
        df2_sec.loc[(df2_sec.Ofsted == "Good"), "Ofsted"] = "🎓🎓🎓🎓"
        df2_sec.loc[(df2_sec.Ofsted == "Satisfactory"), "Ofsted"] = "🎓🎓🎓"
        df2_sec.loc[(df2_sec.Ofsted == "Requires Improvement"), "Ofsted"] = "🎓🎓"
        df2_sec.loc[(df2_sec.Ofsted == "Inadequate"), "Ofsted"] = "🎓"

    df3_p16 = df3c.copy().sort_values(by=["School"])
    # Refresh row no.
    df3_p16["Row"] = df3_p16.reset_index().index
    df3_p16["Row"] += 1
    if len(df3_p16) == 0:
        pass
    else:
        # Map progress to stars
        df3_p16.loc[(df3_p16.Prog_Band == "1"), "Prog Band"] = "⭐⭐⭐⭐⭐"
        df3_p16.loc[(df3_p16.Prog_Band == "2"), "Prog Band"] = "⭐⭐⭐⭐"
        df3_p16.loc[(df3_p16.Prog_Band == "3"), "Prog Band"] = "⭐⭐⭐"
        df3_p16.loc[(df3_p16.Prog_Band == "4"), "Prog Band"] = "⭐⭐"
        df3_p16.loc[(df3_p16.Prog_Band == "5"), "Prog Band"] = "⭐"
        # Map ofsted rating to stars
        df3_p16.loc[(df3_p16.Ofsted == "Outstanding"), "Ofsted"] = "🎓🎓🎓🎓🎓"
        df3_p16.loc[(df3_p16.Ofsted == "Good"), "Ofsted"] = "🎓🎓🎓🎓"
        df3_p16.loc[(df3_p16.Ofsted == "Satisfactory"), "Ofsted"] = "🎓🎓🎓"
        df3_p16.loc[(df3_p16.Ofsted == "Requires Improvement"), "Ofsted"] = "🎓🎓"
        df3_p16.loc[(df3_p16.Ofsted == "Inadequate"), "Ofsted"] = "🎓"

    df1_pri["Last Inspected"] = pd.to_datetime(df1_pri["Last Inspection"].astype(str), format="%Y%m%d").dt.date
    df2_sec["Last Inspected"] = pd.to_datetime(df2_sec["Last Inspection"].astype(str), format="%Y%m%d").dt.date
    df3_p16["Last Inspected"] = pd.to_datetime(df3_p16["Last Inspection"].astype(str), format="%Y%m%d").dt.date

    return df1_pri.to_dict("records"), \
           df2_sec.to_dict("records"), \
           df3_p16.to_dict("records")


@app.callback(
    [
        Output("gcse_att8_avg", "children"),
        Output("gcse_eng_maths_grade5_pct", "children"),
        Output("gcse_entering_ebacc", "children"),
        Output("gcse_ebacc_score", "children"),
        Output("alevel_grade_avg", "children"),
        Output("alevel_score_avg", "children")
    ],
    Input("school_drop", "value")
)
def update_cards(selected_school):
    gcse_att8 = df_eng_avg["GCSEATT8"][0]
    gcse_eng_maths_grade5 = df_eng_avg["GCSEENGMAT5"][0]
    gcse_enter_ebaccs = df_eng_avg["EBACCENT"][0]
    gcse_ebaccs_score = df_eng_avg["EBACCSCORE"][0]
    alevel_grade = df_eng_avg["ALGRADE"][0]
    alevel_score = df_eng_avg["ALSCORE"][0]

    return gcse_att8, gcse_eng_maths_grade5, gcse_enter_ebaccs, gcse_ebaccs_score, alevel_grade, alevel_score


if __name__ == "__main__":
    app.run_server(debug=True)
