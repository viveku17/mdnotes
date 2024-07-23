import requests
from dash import Dash, dcc, html, Input, Output, callback, State
from src import layout_builder
from src import os_service 
from src import data_service


JS_LIST = [
    {
        "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
        "crossorigin": "anonymous"
    }
]

CSS_LIST = [
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
        'rel': 'stylesheet',
        "integrity": "sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN",
        "crossorigin": "anonymous"
    }
]

app = Dash(__name__,
           external_scripts=JS_LIST,
           external_stylesheets=CSS_LIST)


app.layout = html.Div(
    children=[
        layout_builder.build_title(),
        layout_builder.build_select_directory(),
        layout_builder.build_load_notes(),
        layout_builder.build_main_display()
    ],
    className="p-3 container"
)


# ==========================
# Callbacks
# ==========================


@callback(
    Output("status_select_directory", "value"),
    Output("status_select_directory", "className"),
    Output("btn_load_notes", "className"),
    Input("url_select_directory", "value"),
)
def action_select_directory(input_url_select_directory_value):
    output_value_status_select_directory = f"{input_url_select_directory_value} is not a valid directory"
    output_class_status_select_directory = "input-group-text form-inline w-100 bg-danger"
    output_class_btn_load_notes = "btn btn-primary w-100 disabled"
    if input_url_select_directory_value is not None and os_service.is_valid_directory(input_url_select_directory_value):
        output_value_status_select_directory =  f"{input_url_select_directory_value} is a valid directory"
        output_class_status_select_directory = "input-group-text form-inline w-100 bg-success"
        output_class_btn_load_notes = "btn btn-primary w-100 enabled"
    return output_value_status_select_directory, output_class_status_select_directory, output_class_btn_load_notes


@callback(
    Output("status_load_notes", "value"),
    Output("status_load_notes", "className"),
    Output("div_navigation_display", "children"),
    Output("div_content_display", "children"),
    Input("btn_load_notes", "n_clicks"),
    State("url_select_directory", "value"),
)
def action_load_notes(input_clicks_btn_load_notes, state_url_select_directory_value):
    output_value_status_load_notes = f""
    output_class_status_load_notes = "input-group-text form-inline w-100 bg-danger"
    output_children_div_navigation_display = []
    output_children_div_content_display = []
    if state_url_select_directory_value is not None:
        data_service.set_data("ActiveDirectory", state_url_select_directory_value) 
        main_service.load_notes()

        output_value_status_load_notes =  f"Loaded notes from  {state_url_select_directory_value}"
        output_class_status_load_notes = "input-group-text form-inline w-100 bg-success"
        output_children_div_navigation_display = action_init_navigation_display()
        output_children_div_content_display = action_init_content_display()
    return (
        output_value_status_load_notes, 
        output_class_status_load_notes, 
        output_children_div_navigation_display,
        output_children_div_content_display
    )


def action_init_navigation_display():
    return "Navigation"


def action_init_content_display():
    return "Content"



# @callback(
#     Output('clone_repo_status', 'value'),
#     Output('clone_repo_status', 'className'),
#     Output('select_branch', 'options'),
#     Input('btn_clone_repo', 'n_clicks'),
#     State('input_select_directory', 'value'),    
#     prevent_initial_call=True
# )
# def clone_repo_action(btn_clone_repo_clicks, select_repo_url):
#     clone_repo_status_value = "git repo was not cloned correctly"
#     clone_repo_status_class = "input-group-text bg-danger form-inline w-100"
#     select_branch_options = []
#     if is_valid_git_repo(str(select_repo_url)):
#         result = os_service.clone_repo(select_repo_url)
#         if result:
#             clone_repo_status_value = "git repo was cloned correctly"
#             clone_repo_status_class = "input-group-text bg-success form-inline w-100"
#             select_branch_options = os_service.get_active_repo_branches()
#     return clone_repo_status_value, clone_repo_status_class, select_branch_options



# @callback(
#     Output('clone_repo_status', 'value'),
#     Output('clone_repo_status', 'className'),
#     Output('select_branch', 'options'),
#     Input('btn_clone_repo', 'n_clicks'),
#     State('select_repo', 'value'),    
#     prevent_initial_call=True
# )
# def clone_repo_action(btn_clone_repo_clicks, select_repo_url):
#     clone_repo_status_value = "git repo was not cloned correctly"
#     clone_repo_status_class = "input-group-text bg-danger form-inline w-100"
#     select_branch_options = []
#     if is_valid_git_repo(str(select_repo_url)):
#         result = os_service.clone_repo(select_repo_url)
#         if result:
#             clone_repo_status_value = "git repo was cloned correctly"
#             clone_repo_status_class = "input-group-text bg-success form-inline w-100"
#             select_branch_options = os_service.get_active_repo_branches()
#     return clone_repo_status_value, clone_repo_status_class, select_branch_options


# @callback(
#     Output('select_branch', 'value'),
#     Output('select_branch', 'options', allow_duplicate=True),
#     Input('select_branch_filter', 'value'),
#     prevent_initial_call=True,
# )
# def select_branch_filter_action(select_branch_filter_value):
#     branch_filter = select_branch_filter_value.strip().lower()
#     branches = os_service.get_active_repo_branches()
#     select_branch_value = ""
#     select_branch_options = [option for option in branches if option.lower().startswith(branch_filter)]
#     if select_branch_options:
#          select_branch_value = select_branch_options[0]
#     return select_branch_value, select_branch_options


# @callback(
#     Output('checkout_branch_status', 'value'),
#     Output('checkout_branch_status', 'className'),
#     Input('btn_checkout_branch', 'n_clicks'),
# )
# def checkout_branch_action(btn_checkout_branch_clicks):
#     pass
#     # clone_repo_status_value = "git repo was not cloned correctly"
#     # clone_repo_status_class = "input-group-text bg-danger form-inline w-100"
#     # select_branch_options = []
#     # if is_valid_git_repo(str(select_repo_url)):
#     #     result = os_service.clone_repo(select_repo_url)
#     #     if result:
#     #         clone_repo_status_value = "git repo was cloned correctly"
#     #         clone_repo_status_class = "input-group-text bg-success form-inline w-100"
#     #         select_branch_options = os_service.get_active_repo_branches()
#     # return clone_repo_status_value, clone_repo_status_class, select_branch_options



# ==========================
# Private Methods
# ==========================


# def is_valid_git_repo(url):
#     if (url.startswith("https://") and url.endswith(".git")):
#         try:
#             response = requests.get(url)
#             if response:
#                 return (response.status_code == 200)
#         except:
#             pass
#     return False        

