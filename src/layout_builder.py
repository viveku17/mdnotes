from dash import dcc, html


def build_title():
    return html.H1(children="MdNotes", className="text-primary")


def build_select_directory():
    return  mt3_div(
        children=[
            html.Div(
                children=[
                    dcc.Input(id="url_select_directory", 
                        type="url", 
                        placeholder="Paste the path to the directory containing your notes", 
                        className="form-control w-100")

                ],
                className="col"
            ),
            html.Div(
                children=[
                    dcc.Input(id="status_select_directory", type="text", readOnly=True, 
                              className="input-group-text bg-danger form-inline w-100"),
                ],
                className="col"
            )
        ],
        className="row"
    )


def build_load_notes():
    return  mt3_div(
        children=[
            html.Div(
                children=[
                    html.Button('Load Notes', id='btn_load_notes', className="btn btn-primary w-100 disabled")
                ],
                className="col"
            ),
            html.Div(
                children=[
                    dcc.Input(id="status_load_notes", type="text", readOnly=True, 
                              className="input-group-text bg-danger form-inline w-100"),
                ],
                className="col"
            )
        ],
        className="row"
    )


def build_main_display():
    return mt3_div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        id="div_navigation_display",
                        className="col-3"
                    ),
                    html.Div(
                        id="div_content_display",
                        className="col"
                    )                    
                ],
                className="row"
            )
        ],
    )


def mt3_div(**kwargs):
    kwargs["className"] = "mt-3 " + kwargs.get("className", "")        
    return html.Div(**kwargs)


# def build_selection_clone_repo():
#     return html.Div(
#         children=[
#             html.Div(
#                 children=[
#                     html.Button('Clone Repo', id='btn_clone_repo', className="btn btn-primary w-100")
#                 ],
#                 className="col"
#             ),
#             html.Div(
#                 children=[
#                     dcc.Input(id="clone_repo_status", type="text", readOnly=True, 
#                               className="input-group-text bg-danger form-inline w-100"),
#                 ],
#                 className="col"
#             )
#         ],
#         className="row mt-2"
#     )


# def build_selection_select_branch():
#     return html.Div(
#         children=[
#             html.Div(
#                 children=[
#                     dcc.Dropdown(id="select_branch", value="main", options=[]),
#                 ],
#                 className="col"
#             ),
#             html.Div(
#                 children=[
#                     html.Div(
#                         children=[
#                             html.Span(children=["Select Branch Filter"], className="input-group-text")
#                         ],
#                         className="input-group-prepend col w-25"
#                     ),
#                     dcc.Input(id="select_branch_filter", type="text", 
#                               className="form-control w-75"),
#                 ],
#                 className="input-group col"
#             )
#         ],
#         className="row mt-2"
#     )


# def build_selection_checkout_branch():
#     return html.Div(
#         children=[
#             html.Div(
#                 children=[
#                     html.Button('Checkout Branch', id='btn_checkout_branch', className="btn btn-primary w-100")
#                 ],
#                 className="col"
#             ),
#             html.Div(
#                 children=[
#                     dcc.Input(id="checkout_branch_status", type="text", readOnly=True, 
#                               className="input-group-text bg-danger form-inline w-100"),
#                 ],
#                 className="col"
#             )
#         ],
#         className="row mt-2"
#     )
