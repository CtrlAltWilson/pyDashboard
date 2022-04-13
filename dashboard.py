#!/usr/bin/python3
import dash
import subprocess
import time
import datetime
import requests
import math

import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash import dcc, html, State, Input, Output, callback_context
from calls import *

#TODO
##Create image to thumbnail 

# external JavaScript files
external_scripts = [
    'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.bundle.js',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.jshttps://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js',
    'https://kit.fontawesome.com/e0dc16c1bb.js',
    'https://wilsonngo.com/assets/accessible_files/pyDgtag/async_src.js',
    'https://wilsonngo.com/assets/accessible_files/pyDgtag/gtag.js'
]

# external CSS stylesheets
external_stylesheets = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
    'https://unicons.iconscout.com/release/v4.0.0/css/line.css'
]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.title = "Wilson Ngo"
app._favicon = ('favicon.ico')
server = app.server
app.scripts.config.serve_locally = True
#################################################################################
#
#
# TOKENS
#
#
#################################################################################

if secondrow_charts == 2:
    secondrow_chartsdash = "content rounded-3 p-3"
else:
    secondrow_chartsdash = ""

#Sidebar Links
link1 = link2 = link3 = link4 = link5 = link6 = link7 = link8 = link9 = link10 = ""
icon1 = icon2 = icon3 = icon4 = icon5 = icon6 = icon7 = icon8 = icon9 = icon10 = ""
icon1 = "uil-map-marker"
link1 = html.A("Houston, TX",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
icon2 = "uil-paperclip"
link2 = html.A("Resume", id="openResume", n_clicks=0, href="#", style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
#html.A("Resume",href="/resume",style={"text-decoration":"none", "color":"#aabbcc"})
icon3 = "uil-globe"
link3 = html.A("Website",href="https://www.wilsonngo.com",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
icon4 = "fas fa-envelope-square"
link4 = html.A(" Email",href="mailto:wilson@wilsonngo.com",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
icon5 = "fab fa-linkedin"
link5 = html.A(" Linkedin",href="https://www.linkedin.com/in/hwilsonngo/",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
icon6 = "fab fa-github-square"
link6 = html.A(" Github",href="https://github.com/CtrlAltWilson",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
icon7 = "uil-keyboard"
link7 = html.A("Leetcode",href="https://leetcode.com/wilsonbngo/",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
icon8 = "fab fa-facebook-messenger"
link8 = html.A("Messenger",href="https://fb.me/msg/BxNgo",style={"text-decoration":"none", "color":"#aabbcc"},className="sidebarlink")
#icon9 = "fab fa-instagram-square"
#link9 = html.A("Instagram",href="https://www.instagram.com/justpocki/",style={"text-decoration":"none", "color":"#aabbcc"})
#icon10 = "fab fa-facebook-square"
#link10 = html.A("Facebook",href="https://www.facebook.com/BxNgo",style={"text-decoration":"none", "color":"#aabbcc"})

accImg1      = app.get_asset_url('Projects/ROSCA.png')
accTitle1    = "ROSCA Chatbot"
accMentions1 = ["Company Meeting - August 2021", "Company Meeting - November 2021", "QA Lead - January 2022"]

accImg2      = app.get_asset_url('Projects/commitmentalert.png')
accTitle2    = "Commitment Alert!"
accMentions2 = ["Department Meeting - August 2020","Department Meeting - November 2021"]

accImg3      = app.get_asset_url('Projects/sharepoint.png')
accTitle3    = "SharePoint Communication Site"
accMentions3 = ["Company Meeting - September 2020"]

#accImg4      = 
#accTitle4    = ""
#accMentions4 = []



#################################################################################
#
#
# LEETCODE
#
#
#################################################################################

response = requests.get("https://leetcode.com/api/problems/all/",cookies=Cookie)
lc_data = response.json()
lcez = 552
lcmed = 1176
lchard = 475

def lc_recall():
    global response, lc_data
    response = requests.get("https://leetcode.com/api/problems/all/",cookies=Cookie)
    lc_data = response.json()

def lc_matchPer():
    print ("!:{} 2:{}".format((lcez + lcmed + lchard),lc_getTotal()))
    if (lcez + lcmed + lchard) == lc_getTotal():
        return True
    else:
        return False

def lc_getSolved():
    return lc_data["num_solved"]

def lc_getTotal():
    return lc_data["num_total"]

def lc_getPercent():
    comb = lc_getSolved()/lc_getTotal()*100
    if math.ceil(comb) == comb:
        return math.ceil(comb)
    else:
        return float("{:.2f}".format(comb))

def lc_getEasy():
    return lc_data["ac_easy"]

def lc_getEasyPer():
    return (lc_data["ac_easy"]/lcez)*100

def lc_getMedium():
    return lc_data["ac_medium"]

def lc_getMediumPer():
    return (lc_data["ac_medium"]/lcmed)*100

def lc_getHard():
    return lc_data["ac_hard"]

def lc_getHardPer():
    return (lc_data["ac_hard"]/lchard)*100

def lc_getRemaining():
    return lc_getTotal() - lc_getSolved()


#################################################################################
#
#
# MAIN
#
#
#################################################################################
def guestvisitor():
    return html.A([
        html.A("Wilson"),
        html.Span("", className="main-color")
    ],className="navbar-brand", href="#")
def get_pfp():
    pfp = 'pfp-thumb.jpg'
    return html.Img(className="rounded-pill img-fluid", width="150",src=app.get_asset_url(pfp), alt="")
def get_name():
    if guest == 1:
        return ""
    else:
        return "Wilson"
def get_welcomeback():
    global guest
    if guest == 1:
        #return "Welcome ",get_name(),"!"
        return html.Div([
            html.Div("I am a Software Developer who enjoys taking on projects where I can challenge my analytical and technical skills. "),
            html.Div("If you would like to have a chat tap or scan this barcode for my contact!"),
        ])
    else:
        return "Welcome back, ",get_name(),"!"
def get_ip_ad():

    return html.P(children=["IP Address: ", get_ip()], className="mt-1 mb-0")
def separator(title=None):
    return html.Div([
        html.Span(title, className="separator", id=title, style={"padding": "0 10px", "color":"#aabbcc"})
        ],className="separatorLine",style={"border-bottom": "1px solid #aabbcc", "text-align": "center", "border-radius":"12px"})
def leetcode_graph():
    print("Checking LeetCode Graph")
    if secondrow_charts != 1 and secondrow_charts != 2:
        print("Disabled")
        return ""
    else:
        print("Starting Graph, second row is set to {}".format(secondrow_charts))
        if lc_getEasy() > 0:
            lc_transparent = 1
            chartwidth = "425px"
            if secondrow_charts == 2:
                srCharts = "col-lg-6"
                srChatlayout=250
                srChatlayoutWidth = "75%"
                srCbg = "chart-container rounded-2 p-3"
            else:
                srCharts = ""
                srChatlayout=400
                srChatlayoutWidth = "50%"   
                srCbg = "align-items-center"
            lc_recall()
            lclabels = ["Easy", "Medium", "Hard"]
            #lccolor = ['lightcyan','cyan','royalblue','darkblue']
            #lccolor = ['#C1E1C1','royalblue','#FAA0A0']
            lccolor = ['#1ca8dd','#0578e3','#a086ff']
            #if lc_matchPer():
            if True:
                lcpercent =[
                    "{}%".format(math.ceil(lc_getEasy())), 
                    "{}%".format(math.ceil(lc_getMedium())), 
                    "{}%".format(math.ceil(lc_getHard()))
                    ]
                lcvalues=[
                    lc_getEasyPer(),
                    lc_getMediumPer(),
                    lc_getHardPer()
                    ]
                fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
                fig.add_trace(
                    go.Pie(
                        labels=lclabels, 
                        values=lcvalues,
                        hovertext=lcpercent,
                        name="",
                        marker_colors=lccolor
                        ),1,1)
                fig.update_traces(hole=.75, hoverinfo="label+text") #adjust size of donut
            else:
                lcvalues=[
                    lc_getEasy(), 
                    lc_getMedium(), 
                    lc_getHard()
                    ]
                fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
                fig.add_trace(
                    go.Pie(
                        labels=lclabels, 
                        values=lcvalues,
                        name="",
                        marker_colors=lccolor,
                        ),1,1)
                fig.update_traces(hole=.75, hoverinfo="label+value") #adjust size of donut
            #lcvalues=[5,5,5]
            # Create subplots: use 'domain' type for Pie subplot
            
            # Use `hole` to create a donut-like pie chart

            #leetcode progress title and the giant percent symbol
            if lc_getPercent() > 10:
                fig.update_layout(
                    title_text="Leetcode",
                    title_font_size=20,
                    title_font_color="white",
                    title_font_family="Roboto-LightItalic",
                    title_x=0.50,title_y=0.60,
                    # Add annotations in the center of the donut pies.
                    annotations=([dict(text="{}%".format(lc_getPercent()), x=0.5, y=0.45, font_size=50, showarrow=False,font_color="white"),
                        #dict(text="Last Update: {}".format(datetime.datetime.now()), x=0.5, y=0.55, font_size=10, showarrow=False,font_color="white"),
                        ]),
                    showlegend = False
                    )
            else:
                fig.update_layout(
                    title_text="Leetcode",
                    title_font_size=30,
                    title_font_color="white",
                    title_font_family="Roboto-LightItalic",
                    title_x=0.50,title_y=0.50,
                    showlegend = False
                    )
            if lc_transparent == 1:
                fig.update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    })
            fig.update_layout(
                autosize=True,
                width=srChatlayout,
                height=srChatlayout,
                margin=dict(
                    autoexpand=True,
                    l=0,
                    r=0,
                    t=0,
                    b=0,
                    )
                )
            fig.update_traces(textfont_size=1,
                textfont_color="white",
                insidetextfont_color="black",
                legendgrouptitle_font_color="white",
                selector=dict(type='pie'))

            if secondrow_charts == 1:
                return html.Div([
                        html.Div(className="spacer"),
                        separator("Progression"),
                        html.Div(className="spacer"),
                        html.Div([
                            dcc.Graph(figure=fig,config = {'displaylogo': False, 'displayModeBar': False})
                            ],className=srCbg,style={"margin":"0 auto", "position":"relative","width":chartwidth,"padding":"15px"})
                    ], className="{}".format(srCharts))
            else:
                return html.Div([
                        html.Div(className="spacer"),
                        separator("Progression"),
                        html.Div(className="spacer"),
                        html.Div([
                            html.Div([
                                dcc.Graph(figure=fig,config = {'displaylogo': False, 'displayModeBar': False})
                                ],style={"width":"225px","margin":"auto"})
                            ],className=srCbg,style={"margin":"0 auto", "position":"relative","width":"100%"})
                    ], className="{}".format(srCharts))
        else:
            print("Error, lc_getEasy returned {}".format(lc_getEasy()))
            return ""
def second_graph():
    if secondrow_charts != 2:
        return ""
    else:
        print("Starting Second Graph")
        if lc_getEasy() > 0:
            lc_transparent = 1
            lc_recall()
            labels = ["Easy", "Medium", "Hard"]
            #lccolor = ['lightcyan','cyan','royalblue','darkblue']
            #lccolor = ['#C1E1C1','royalblue','#FAA0A0']
            lccolor = ['#1ca8dd','#0578e3','#a086ff']

            # Create subplots: use 'domain' type for Pie subplot
            fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
            fig.add_trace(go.Pie(labels=labels, values=[lc_getEasy(), lc_getMedium(), lc_getHard()], name="",
                marker_colors=lccolor),1, 1)
            # Use `hole` to create a donut-like pie chart
            fig.update_traces(hole=.9, hoverinfo="label+value")
            fig.update_layout(
                title_text="Leetcode Progress",
                title_font_size=20,
                title_font_color="white",
                title_x=0.50,title_y=0.60,
                # Add annotations in the center of the donut pies.
                annotations=([dict(text="{}%".format(lc_getPercent()), x=0.5, y=0.45, font_size=50, showarrow=False,font_color="white"),
                    #dict(text="Last Update: {}".format(datetime.datetime.now()), x=0.5, y=0.55, font_size=10, showarrow=False,font_color="white"),
                    ]),
                showlegend = False
                )
            
            if lc_transparent == 1:
                fig.update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    })
            fig.update_layout(
                autosize=False,
                width=250,
                height=250,
                margin=dict(
                    l=0,
                    r=0,
                    b=0,
                    t=0
                    )
                )
            fig.update_traces(textfont_size=1,
                textfont_color="white",
                insidetextfont_color="black",
                legendgrouptitle_font_color="white",
                selector=dict(type='pie'))
            return html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig,config = {'displaylogo': False, 'displayModeBar': False})
                      ],style={"width":"225px","margin":"auto"})
                    ],className="chart-container rounded-2 p-3",style={"margin":"0 auto", "position":"relative","width":"100%"})#, style={"height":srChatlayheight,"width":srChatlaywidth,"margin":"auto"})
                ], className="col-lg-6")
def get_logs(item):
    if item == 2:
        return html.Section([
        html.Div([
            leetcode_graph(),
            second_graph(),
            ],className="row")
        ],className="charts mt-4")
    else:
        return ""
def get_logs2(item):
    if item == 1:
        return get_logs(2)
def get_reboot():
    return [
        html.A(
            className="nav-link",
            href="/reboot",
            id="reboot_btn",
            role="button",
            n_clicks = 0
        )
    ]
def get_chart_3():
    return html.Section([
        html.Div([
            html.H3("Chart title number three", className="fs-6 mb-3"),
            html.Div([
                html.Canvas(id="chart3", width="100%")
                ],style={'height' : '300px'})
            ],className="chart-container p-3")
        ],className="charts mt-4")
def ProjectLegend_Pane(n = 0):
    if n == 0:
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.I(className="uil-location-point",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("You Are Here")
                    ]),
                dbc.Col([
                    html.I(" ",className="uil-external-link-alt",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("External Link")
                    ]),
                ], className="contactText"),
            ], className="contactBg")
    else:
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.I(className="uil-star",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("Pop Up Info")
                    ]),
                dbc.Col([
                    html.I(" ",className="uil-external-link-alt",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("External Link")
                    ]),
                ], className="contactText"),
            ], className="contactBg")
def SkillsLegend_Pane():
    skillsize = 40
    skillsfont = ".8vw"
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/64cplusi.png"),height=skillsize,width=skillsize),
                html.Div("C++",style={"font-size":skillsfont})
                ]),
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/49csharpi.png"),height=skillsize,width=skillsize),
                html.Div("C#",style={"font-size":skillsfont})
                ]),
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/50exceli.png"),height=skillsize,width=skillsize),
                html.Div("Excel",style={"font-size":skillsfont})
                ]),
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/50herokui.png"),height=skillsize,width=skillsize),
                html.Div("Heroku",style={"font-size":skillsfont})
                ]),
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/50phpi.png"),height=skillsize,width=skillsize),
                html.Div("PHP",style={"font-size":skillsfont})
                ]),
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/50salesforcei.png"),height=skillsize,width=skillsize),
                html.Div("Salesforce",style={"font-size":skillsfont})
                ]),
            dbc.Col([
                html.Img(src=app.get_asset_url("Skills/50sharepointi.png"),height=skillsize,width=skillsize),
                html.Div("SharePoint",style={"font-size":skillsfont})
                ]),

            ], className="contactText"),

        ], className="contactBg")

def ProjectLegend_Pane(n = 0):
    if n == 0:
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.I(className="uil-location-point",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("You Are Here")
                    ]),
                dbc.Col([
                    html.I(" ",className="uil-external-link-alt",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("External Link")
                    ]),
                ], className="contactText"),
            ], className="contactBg")
    else:
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.I(className="uil-star",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("Pop Up Info")
                    ]),
                dbc.Col([
                    html.I(" ",className="uil-external-link-alt",style={"font-size":"20px","color":"lightblue"}),
                    html.Div("External Link")
                    ]),
                ], className="contactText"),
            ], className="contactBg")
def get_ModalResume():
    return dbc.Modal([
        dbc.ModalBody(html.Iframe(id="embedded-pdf", src="assets\\Wilson_Ngo_Resume.pdf")),
        dbc.ModalFooter(dbc.Button(
                "Close", id="closeResume", className="ms-auto", n_clicks=0,style={"width":"100%"}
                ),
            ),
        ],
        id = "Resume",
        is_open=False,
        scrollable=True,
        centered=True,
        #style={"max-width":"100vh"},#,"width":"100%"},
        className="Resume",
        )
def get_ModalRosca():
    return dbc.Modal([
        dbc.ModalBody([
            html.H1(html.B("R.O.S.C.A")),
            html.H2("Raptor's Online Service Chat Assistance"),
            html.Img(src=app.get_asset_url('Projects/RoscaFull.png'),
                style={"width":"100%"}
                ),
            html.H3("Description"),
            html.P("Support is now increasing the client support experience with an online chat interface. During business hours, clients will be able to interact with the support through the chat; if it's during after hours, a bot will provide the proper links to the knowledge base articles based on the description of the issue."),
            html.Br(),
            html.H3("Bot"),
            html.P("Introducing Raptor's Online Service Chat Assistance (ROSCA). Raptor's rapidly evolving bot that will be able to grab specific keywords and attempts to solve the client's issue. I have built this bot to understand and grow with phrases given to it by clients. You can say hi to it and it'll say hi back. You can demand an agent or ask for billing and it knows where to direct you."),
            html.Br(),
            html.H3("How it works"),
            html.P("Using multiple scripting modules, I am able to route the communication from the start to the end of the chat. ROSCA in design is set to pay attention to certain keywords from the client's description of the issue and pull any articles that contain those keywords. ROSCA is continually growing and have already solved a big portion of support's cases."),
            html.Br(),
            html.H3("Notes and Updates"),
            html.P("-Originally it requests for Name, Email, and Phone number. Now, we have it to pull the data of the client already logged in and automatically send that data to the next agent in queue."),
            html.P("-ROSCA channels clients through a double funnel system which puts them into prequeue before the actual queue. This allows them to submit a ticket if the wait is too long."),
            html.P("-ROSCA now logs and automate combined logs for total solved by ROSCA, total sent to agents, and total overall."),
            ]),
        dbc.ModalFooter(dbc.Button(
                "Close", id="closeRosca", className="ms-auto", n_clicks=0,style={"width":"100%"}
                ),
            ),
        ],
        id = "Rosca",
        is_open=False,
        scrollable=True,
        centered=True,
        #style={"max-width":"100vh"},#,"width":"100%"},
        className="Resume",
        )
def get_ModalLG():
    return dbc.Modal([
        dbc.ModalBody([
            html.H1(html.B("LobbyGuard Suite")),
            html.H2("LobbyGuard's All-in-One Installer"),
            html.Img(src=app.get_asset_url('Projects/LobbyGuard.png'),
                style={"width":"75%","margin":"auto"}
                ),
            html.H3("Description"),
            html.P("There has been an ongoing issue where installing one of our products, LobbyGuard, requires 15 steps with 8 separate installations. I have combined all of these steps and files into one GUI installer using pascal script. The original installation time takes about 25~60 minutes to complete. With this installer, it is timed to be completed within 15 minutes."),
            html.Br(),
            html.H3("How it works"),
            html.P("After clicking install, this installer will first run 2 separate installers silently while going through the main GUI to install LobbyGuard. Once this is complete, it will proceed to copy required files over and complete the rest of the installation."),
            html.Br(),
            html.H3("Notes"),
            html.P("-Admin credentials will always be required."),
            html.P("-The GUI will allow the user to decide which program to install."),
            ]),
        dbc.ModalFooter(dbc.Button(
                "Close", id="closeLobbyGuard", className="ms-auto", n_clicks=0,style={"width":"100%"}
                ),
            ),
        ],
        id = "LobbyGuard",
        is_open=False,
        scrollable=True,
        centered=True,
        #style={"max-width":"100vh"},#,"width":"100%"},
        className="Resume",
        )
def get_ModalRaptorHub():
    return dbc.Modal([
        dbc.ModalBody([
            html.H1(html.B("RaptorHub")),
            html.H2("Company's Sharepoint Site"),
            html.Img(src=app.get_asset_url('Projects/sharepoint.png'),
                style={"width":"50%","margin":"auto"}
                ),
            html.H3("Description"),
            html.P("Raptor Hub is intended to be the company's communication site where all employees can go for updates, news, documentation, and external links."),
            html.Br(),
            html.H3("How it works"),
            html.P("Designed with SharePoint, anyone working with the company will have access using their company email. Each department has its own subsite where they can post documents that can be used by other departments. Raptor Hub also has external links to sites such as marketing resources, bucketlist, calendly, benefits and pay. "),
            html.Br(),
            html.H3("Notes"),
            html.P("-Ownership has been given to a couple users to maintain the communication site, though I can still help by request."),
            ]),
        dbc.ModalFooter(dbc.Button(
                "Close", id="closeRaptorHub", className="ms-auto", n_clicks=0,style={"width":"100%"}
                ),
            ),
        ],
        id = "RaptorHub",
        is_open=False,
        scrollable=True,
        centered=True,
        #style={"max-width":"100vh"},#,"width":"100%"},
        className="Resume",
        )
def get_ModalCAlert():
    return dbc.Modal([
        dbc.ModalBody([
            html.H1(html.B("Commitment Alert!")),
            html.H2("Popup sound alerts for SalesForce Commitments and Chats"),
            html.H3(html.A([
                "Chrome Extension Link", 
                html.I(" ",className="uil-external-link-alt",style={"font-size":"20px"}),
                ],
                href=pLin9,style={"text-decoration":"none"}),
            ),
            html.Img(src=app.get_asset_url('Projects/commitmentalerts.jpg'),
                style={"width":"75%","margin":"auto"}
                ),
            html.H3("Description"),
            html.P("With Salesforce, the commitments will appear in silent and sometimes behind the window that you are currently working on. This has been an ongoing issue that puts Support members to refuse. I developed a Chrome extension as a workaround to this."),
            html.Br(),
            html.H3("How it works"),
            html.P("This extension will listen for any window with Salesforce’s unique link for commitments. When this unique link appears, Commitment Alerts will launch another window following a link that was either set or defaulted with sound. The user may then close the window and start the commitment. You can essentially set any link that you want to appear when a commitment opens; I recommend using a YouTube link or a website with sound auto-playing for optimal use of the extension."),
            html.Br(),
            html.H3("Notes"),
            html.P("-This extension will only work for Raptor Technologies because of the special link that Raptor uses in Salesforce."),
            html.P("-Commitments are cases from the queue that appears the to agent for 2 minutes. If the agent does not confirm the commitment within the given time, it will put the agent to refusal status."),
            html.H3("Updates"),
            html.P("-This extension now supports sending alerts via Telegram. Developed bots to gather chat ID with python."),
            html.P("-This extension has been updated to also alert for Raptor's chat interface."),
            ]),
        dbc.ModalFooter(dbc.Button(
                "Close", id="closeCAlert", className="ms-auto", n_clicks=0,style={"width":"100%"}
                ),
            ),
        ],
        id = "CAlert",
        is_open=False,
        scrollable=True,
        centered=True,
        #style={"max-width":"100vh"},#,"width":"100%"},
        className="Resume",
        )
def sidebar():
        return html.Aside([
        html.I(className="uil-bars close-aside d-md-none d-lg-none", **{'data-close': "show-side-navigation1"}),
        html.Div([
            get_pfp(),
            html.Div([
                html.H5([
                    html.A([
                        get_name(),
                        ],className="text-decoration-none", href="#")
                    ], className="fs-6 mb-0"),
                html.A(id = 'get_ip_ad')
                ], className="ms-2")
            ],className="sidebar-header d-flex justify-content-center align-items-center px-3 py-4"),
        html.Div([
            dcc.Input(className="form-control w-100 border-0 bg-transparent",id='pw_input', type="password", placeholder="",style={"color":"white","text-align":"center"}),
            #html.I(className="fa fa-search position-absolute d-block fs-6")
            ]),
        html.Ul([
            html.Li([
                html.I(className=icon1),
                html.A(link1),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon2),
                html.A(link2),
                ],""),
            html.Li([
                html.I(className=icon3),
                html.A(link3),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon4),
                html.A(link4),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon5),
                html.A(link5),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon6),
                html.A(link6),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon7),
                html.A(link7),
                ],""),
            html.Li([
                html.I(className=icon8),
                html.A(link8),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon9),
                html.A(link9),
                ]),#,className="has-dropdown"),
            html.Li([
                html.I(className=icon10),
                html.A(link10)
                ],"")
            ])
        ],
        className="sidebar position-fixed top-0 left-0 overflow-auto h-100 float-left", 
        id="show-side-navigation1")
def nav_bar():
    return html.Nav([
        html.Div([
            html.Div([
                html.Button([
                    html.I(className="uil-bars text-white")
                    ],
                    className="navbar-toggler",
                    type="button", 
                    **{
                        'data-bs-toggle': 'collapse', 
                        'data-bs-target': '#toggle-navbar', 
                        'aria-controls' : 'toggle-navbar', 
                        'aria-expanded' : 'false',
                        'aria-label'    : 'Toggle navigation'
                        }
                    ),
                    guestvisitor()
                ],className="navbar-header"),
            html.Div([
                html.Ul([
                   # html.Li([
                        #html.A("Settings",
                         #   className="nav-link dropdown-toggle",
                          #  href="#",
                           # id="navbarDropdown",
                            #role="button",
                            #**{
                             #   'data-bs-toggle': 'dropdown',
                              #  'aria-expanded' : 'false'
                               # }
                            #),
                 #       html.Ul([
                  #          html.Li(html.A("My Account",className="dropdown-item", href="#")),
                   #         html.Li(html.A("My Inbox",className="dropdown-item", href="#")),
                    #        html.Li(html.A("Help",className="dropdown-item", href="#")),
                     #       html.Li(html.Hr(className="dropdown-divider")),
                      #      html.Li(html.A("Log Out",className="dropdown-item", href="#"))
                       #     ],className="dropdown-menu", **{'aria-labelledby' : 'navbarDropdown'})
                   #     ],className="nav-item dropdown"),
          #HOME BUTTON  
#                        html.Li(html.A("Home",
 #                           className="nav-link",
  #                          href="/",
   #                         id="home_btn",
    #                        role="button",
     #                       n_clicks = 0
      #                      )
       #                 ),
                        html.Li(html.A("Skills",
                            className="nav-link",
                            href="#Skills",
                        )),
#                        html.Li(html.A("Progression",
 #                           className="nav-link",
  #                          href="#Progression",
   #                     )),
                        html.Li(html.A("Accolations",
                            className="nav-link",
                            href="#Accolations",
                        )),
                        html.Li(html.A("Self Projects",
                            className="nav-link",
                            href="#Self%20Projects",
                        )),
                        html.Li(html.A("Work Projects",
                            className="nav-link",
                            href="#Work%20Projects",
                        )),

                        html.Li(id = "get_navbar",className="nav-item dropdown"), #reboot
 #                   html.Li([
  #                      html.A([
   #                         html.I(className="uil-comments-alt"),
    #                        html.Span("23")
     #                       ],className="nav-link", href="#")
      #                  ],className="nav-item"),
       #             html.Li([
        #                html.A([
         #                   html.I(className="uil-bell"),
          #                  html.Span("98")
           #                 ], className="nav-link", href="#")
            #            ], className="nav-item"),
             #       html.Li([
              #          html.A([
               #             html.I(className="uil-bars show-side-btn", **{'data-show' : 'show-side-navigation1'})
                #            ],className="nav-link", href="#")
                 #       ],className="nav-item")
                    ],className="navbar-nav ms-auto")
                ],className="collapse navbar-collapse", id="toggle-navbar")
            ],className="container-fluid mx-2")
        ], className="navbar navbar-expand-md") #end nav
def languages_pane():
    return html.Div([
    dbc.Row([
        dbc.Col([
            html.Img(src=app.get_asset_url('Skills/iconjava3.png'),className="LanIcons"),
            html.Div(html.H3("Java", className="IconTitle"),className="IconTitleBg"),
            ]),
        dbc.Col([
            html.Img(src=app.get_asset_url('Skills/iconpython3.png'),className="LanIcons"),
            html.Div(html.H3("Python", className="IconTitle"),className="IconTitleBg"),
            ]),
        dbc.Col([
            html.Img(src=app.get_asset_url('Skills/iconlinux3.png'),className="LanIcons"),
            html.Div(html.H3("Linux", className="IconTitle"),className="IconTitleBg"),
            ]),
        ],style={"margin-top":"5%"}),
    dbc.Row([
        dbc.Col([
            html.Img(src=app.get_asset_url('Skills/iconhtml3.png'),className="LanIcons"),
            html.Div(html.H3("HTML", className="IconTitle"),className="IconTitleBg"),
            ]),
        dbc.Col([
            html.Img(src=app.get_asset_url('Skills/iconcss3.png'),className="LanIcons"),
            html.Div(html.H3("CSS", className="IconTitle"),className="IconTitleBg"),
            ]),
        dbc.Col([
            html.Img(src=app.get_asset_url('Skills/iconjs3.png'),className="LanIcons"),
            html.Div(html.H3("JavaScript", className="IconTitle"),className="IconTitleBg"),
            ]),
        ],style={"margin-top":"5%"})
    ],className="LanPane")
def top_pane():
    return html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.A([html.Img(className="rounded-pill img-fluid",width="100",src=app.get_asset_url('poplQR.png'), alt="")], href="https://poplme.co/pocki/a"),
                html.Div([
                    html.Div([
                        html.H1("Dashboard", className="fs-3"),
                        ],className="d-flex align-items-center"),
                    html.P([
                        get_welcomeback(),
                        ], className="mb-0")
                    ],className="ms-3")
                ],className="box d-flex rounded-2 align-items-center mb-4 mb-lg-0 p-3 dashboardbio")
        ])
        ],className=secondrow_chartsdash)

    ], className="welcome")
def contact_pane():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.Div([html.I(className="fas fa-envelope-square")," ",
                    html.Div(
                        html.A("Wilson@WilsonNgo.com", 
                            href="mailto:Wilson@WilsonNgo.com",
                            style={"text-decoration":"none", "color":"white"}
                            ),
                        ),
                    ]),
                ]),
            dbc.Col([
                html.Div([html.I(className="fab fa-linkedin")," ",
                    html.Div(
                        html.A("/in/hwilsonngo/", 
                            href="https://www.linkedin.com/in/hwilsonngo/",
                            style={"text-decoration":"none", "color":"white"}
                            ),
                        ),
                    ]),
                ])
            ], className="contactText"),
        ], className="contactBg")
def info_pane():
    return html.Section([
    html.Div([
        html.Div([
            html.Div([
                html.I(className="uil-envelope-shield fs-2 text-center bg-primary rounded-circle"),
                html.Div([
                    html.Div([
                        html.H3("6", className="mb-0"),
                        ],className="d-flex align-items-center"),
                    html.P("Accolations", className="fs-normal mb-0")
                    ],className="ms-3")
                ],className="box d-flex rounded-2 align-items-center mb-4 mb-lg-0 p-3")
            ], className="col-lg-4"),
        html.Div([
            html.Div([
                html.I(className="uil-file fs-2 text-center bg-danger rounded-circle"),
                html.Div([
                    html.Div([
                        html.H3("34", className="mb-0"),
                        html.Span("Projects", className="d-block ms-2")
                        ],className="d-flex align-items-center"),
                    html.P("Lorem ipsum dolor sit amet", className="fs-normal mb-0")
                    ],className="ms-3")
                ],className="box d-flex rounded-2 align-items-center mb-4 mb-lg-0 p-3")
            ], className="col-lg-4"),
        html.Div([
            html.Div([
                html.I(className="uil-users-alt fs-2 text-center bg-success rounded-circle"),
                html.Div([
                    html.Div([
                        html.H3("5,245", className="mb-0"),
                        html.Span("Users", className="d-block ms-2")
                        ],className="d-flex align-items-center"),
                    html.P("Lorem ipsum dolor sit amet", className="fs-normal mb-0")
                    ],className="ms-3")
                ],className="box d-flex rounded-2 align-items-center p-3")
            ], className="col-lg-4")
        ],className="row")
    ], className="statistics mt-4")
def getaccolation(img,title,mentions):
    if title == "":
        return ""
    accColumn = [dbc.Row(
            html.Img(className="img-fluid rounded-pill",
                height=75,
                width=75,
                src=img,
                alt="admin",
                style={"margin":"auto","width":"8vw"}
                ),
            ),
        dbc.Row(html.H3(title),style={"color":"white","margin-top":"2%"})]
    for item in mentions:
        accColumn.append(dbc.Row(
            html.Div(item,style={"color":"#aabbcc"}),
            ))
    return dbc.Col(accColumn,className="admin align-items-center rounded-2 p-3 mb-4", style={"height":"100%","background-color":"var(--dk-dark-bg)","margin-right":"2%","margin-left":"2%","text-align":"center"})

def accolation():
    return html.Div([
        dbc.Row([
            getaccolation(accImg1,accTitle1,accMentions1),
            getaccolation(accImg2,accTitle2,accMentions2),
            getaccolation(accImg3,accTitle3,accMentions3),
            #getaccolation(accImg4,accTitle4,accMentions4),
            ],style={"height":"300px"}),
        ])
def projects_column1(n = 1):
    if n == 1:
        return html.Div([
            html.Div([
                project_panel(pName6,pSrc6,pDes6,pLan6,pLin6), #Dashboard
                project_panel(pName5,pSrc5,pDes5,pLan5,pLin5), #Portfolio Website
                project_panel(pName7,pSrc7,pDes7,pLan7,pLin7), #Spotipy for Piboy
            ],className="box", style={"height":"100%"})
        ],className="col-md-6")
    elif n == 2:
        return html.Div([
            html.Div([
                html.A(
                    project_panel(pName9,pSrc9,pDes9,pLan9,pLin9), #Commitment Alert
                    id="openCAlert",
                    href="#Work%20Projects",
                    n_clicks=0,
                    style={"text-decoration":"none"}
                ),
                project_panel(pName1,pSrc1,pDes1,pLan1,pLin1), #Raptor RC Bot
                html.A(
                    project_panel(pName11,pSrc11,pDes11,pLan11,pLin11), #LobbyGuard Suite
                    id="openLobbyGuard",
                    href="#Work%20Projects",
                    n_clicks=0,
                    style={"text-decoration":"none"}
                ),
            ],className="box", style={"height":"100%"})
        ],className="col-md-6")
def projects_column2(n = 1):
    if n == 1:
        return html.Div([
            html.Div([
                project_panel(pName3,pSrc3,pDes3,pLan3,pLin3), #Raspi
                project_panel(pName4,pSrc4,pDes4,pLan4,pLin4), #RasRas
                project_panel(pName8,pSrc8,pDes8,pLan8,pLin8), #Crypto Wallet
                ],className="box", style={"height":"100%"})
            ],className="col-md-6")
    elif n == 2:
        return html.Div([
            html.Div([
                html.A(
                    project_panel(pName2,pSrc2,pDes2,pLan2,pLin2), #ROSCA
                    id="openRosca",
                    href="#Work%20Projects",
                    n_clicks=0,
                    style={"text-decoration":"none"}
                ),
                html.A(
                    project_panel(pName10,pSrc10,pDes10,pLan10,pLin10), #RaptorHub
                    id="openRaptorHub",
                    href="#Work%20Projects",
                    n_clicks=0,
                    style={"text-decoration":"none"}
                ),
                ],className="box", style={"height":"100%"})
            ],className="col-md-6")
def bottom_info_pane():
    return html.Div([
    html.Div([
        html.Div([
            html.I(className="uil-eye"),
            html.H3(lc_getSolved()),
            html.P("Leetcode Solved", className="lead")
            ],className="box bg-primary p-3")
        ],className="col-md-6 col-lg-3 mb-4 mb-lg-0"),
    html.Div([
        html.Div([
            html.I(className="uil-user"),
            html.H3(lc_getEasy()),
            html.P("Easy Solved", className="lead")
            ],className="box bg-success p-3")
        ],className="col-md-6 col-lg-3 mb-4 mb-lg-0"),
    html.Div([
        html.Div([
            html.I(className="uil-shopping-cart"),
            html.H3(lc_getMedium()),
            html.P("Medium Solved", className="lead")
            ],className="box bg-warning p-3")
        ],className="col-md-6 col-lg-3 mb-4 mb-md-0"),
    html.Div([
        html.Div([
            html.I(className="uil-feedback"),
            html.H3(lc_getHard()),
            html.P("Hard Solved", className="lead")
            ],className="box bg-danger p-3")
        ],className="col-md-6 col-lg-3")
    ],className="row")
def project_panelLink(pLin):
    if pLin != "":
        if pLin == "is_Star": #has info
            return html.A([
                html.I(className="uil-star",style={"font-size":"20px","color":"lightblue"}),
            ],className="img",style={"margin-left":"auto","margin-right":"0"})
        elif pLin == "is_Here": #for dashboard
            return html.A([
                html.I(className="uil-location-point",style={"font-size":"20px","color":"lightblue"})
            ],className="img",style={"margin-left":"auto","margin-right":"0"})
        elif pLin == pLin9: #for commitment alert
            return html.A([
                html.I(className="uil-star",style={"font-size":"20px","color":"lightblue"}),
                html.I(" ",className="uil-external-link-alt",style={"font-size":"20px","color":"lightblue"})
            ],className="img",style={"margin-left":"auto","margin-right":"0"},href=pLin)
        else:
            return html.A([
                html.I(className="uil-external-link-alt",style={"font-size":"20px","color":"lightblue"})
            ],className="img",style={"margin-left":"auto","margin-right":"0"},href=pLin)
def project_panel(pName,pSrc,pDes,pLan,pLin):
    if pName == "":
        return ""
    else:

        if pSrc == "":
            pSrc = "placeholder.jpg"
        if pDes == "":
            pDes = "Very long description here"
        if pLan == "":
            pLan == "Some Language"
        if pLin != "" and pLin != pLin9 and pLin != "is_Here" and pLin != "is_Star":
            return html.A(
                html.Div([
                    html.Div([
                        html.Img(className="img-fluid rounded-pill projectthumb",
                            height=75,
                            width=75,
                            src=app.get_asset_url(pSrc),
                            alt="admin"
                            )
                        ],className="img"),
                    html.Div([
                        html.H3(pName, className="fs-5 mb-1"),
                        html.P("{}".format(pLan), className="mb-0",style={"color":"lightgray"}),
                        html.P(pDes, className="mb-0")
                        ],className="ms-3"),
                    project_panelLink(pLin),
                    ],className="admin d-flex align-items-center rounded-2 p-3 mb-4", style={"height":"30%"}),
                href = pLin,
                style={"text-decoration":"none"}
                )
        elif pLin == "is_Star" or pLin == pLin9:
            return html.Div([
                    html.Div([
                        html.Img(className="img-fluid rounded-pill projectthumb",
                            height=75,
                            width=75,
                            src=app.get_asset_url(pSrc),
                            alt="admin"
                            )
                        ],className="img"),
                    html.Div([
                        html.H3(pName, className="fs-5 mb-1"),
                        html.P("{}".format(pLan), className="mb-0",style={"color":"lightgray"}),
                        html.P(pDes, className="mb-0"),
                        html.P("...see more", className="mb-0",style={"color":"lightblue"}),
                        ],className="ms-3"),
                    project_panelLink(pLin),
                    ],className="admin d-flex align-items-center rounded-2 p-3 mb-4", style={"height":"30%"})
        else:
            return html.Div([
                    html.Div([
                        html.Img(className="img-fluid rounded-pill projectthumb",
                            height=75,
                            width=75,
                            src=app.get_asset_url(pSrc),
                            alt="admin"
                            )
                        ],className="img"),
                    html.Div([
                        html.H3(pName, className="fs-5 mb-1"),
                        html.P("{}".format(pLan), className="mb-0",style={"color":"lightgray"}),
                        html.P(pDes, className="mb-0")
                        ],className="ms-3"),
                    project_panelLink(pLin),
                    ],className="admin d-flex align-items-center rounded-2 p-3 mb-4", style={"height":"30%"})
def footer():
    return html.Div([
        html.I(html.A("WilsonNgo.com", href="WilsonNgo.com",style={"text-decoration":"none", "color":"#aabbcc"})),
        html.I(" © 2022 Wilson Ngo. All rights reserved."),
        ],style={"color":"#aabbcc", "text-align":"center"})
##### INDEX PAGE #####
def redirect_main():
    return html.A("ENTER",
        className="nav-item dropdown",
        href="/main",
        id="main_btn",
        role="button",
        n_clicks = 0,
        style={"text-decoration":"none", "color":"royalblue", "font-size":"10vw","margin":"auto"}
    )

page_main = (sidebar(),
    html.Section([
        nav_bar(),
        html.Div([
            contact_pane(),
            html.Div(className="spacer"),
            top_pane(),
            separator("Skills"),
            html.Div(className="spacer"),
            SkillsLegend_Pane(),
            languages_pane(),
            get_logs2(secondrow_charts),
            #info_pane(),
            get_logs(secondrow_charts),
            html.Div(className="spacer"),
            separator("Accolations"),
            html.Div(className="spacer"),
            accolation(),
            html.Div(className="spacer"),
            separator("Self Projects"),
            html.Div(className="spacer"),
            ProjectLegend_Pane(),
            html.Section([
                html.Div([
                    projects_column1(),
                    projects_column2(),
                ],className="row")
            ],className="admins mt-4"),
            html.Div(className="spacer"),
            separator("Work Projects"),
            html.Div(className="spacer"),
            ProjectLegend_Pane(1),
            html.Section([
                html.Div([
                    projects_column1(2),
                    projects_column2(2),
                ],className="row")
            ],className="admins mt-4"),
            html.Div(className="spacer"),
            html.Section([
                #bottom_info_pane()
                ],className="statis mt-4 text-center"),
            html.Div(className="spacer"),
            #get_chart_3(),
            html.Div(className="spacer"),
            #html.Div(id="chart3"),
            html.Div(" ",className="spacer",style={"margin-bottom":"10%"}),
            #html.Footer("WilsonNgo.com",style={"color":"white"}),
            footer(),
            get_ModalResume(),
            get_ModalRosca(),
            get_ModalLG(),
            get_ModalRaptorHub(),
            get_ModalCAlert(),
            ], className="p-4")
        ],id="wrapper") #end wrapper section
    )#Load everything up before the callbacks

page_reboot = html.Div([
    dcc.Interval(id='interval', interval=1*1000, n_intervals=0),
    html.H2("REBOOTING...",style={"text-decoration":"none", "color":"#aabbcc","font-size":"10vw","line-height":"1"}),
    #html.H3(id='rTimer', children=''),
    html.Nav([
        html.H1(
            html.A("Home",
                className="nav-item dropdown",
                href="/",
                id="home_btn",
                role="button",
                n_clicks = 0
                )
            )
        ], className="navbar navbar-expand-md"), #end nav

    ])

##DEPRECIATED
page_index = html.Div([
    html.Br(),
    html.H1("WILSON",style={"text-decoration":"none", "color":"#aabbcc","font-size":"10vw","line-height":"1"}),
    html.H1("NGO",style={"text-decoration":"none", "color":"#aabbcc","font-size":"10vw","line-height":"1"}),
    html.H1("SOFTWARE",style={"text-decoration":"none", "color":"#aabbcc","font-size":"7vw","line-height":"1"}),
    html.H1([
        html.A("ENGINEER",style={"text-decoration":"none", "color":"#aabbcc","font-size":"9.25vw","line-height":"1"}),
        html.Span("DEVELOPER", className="main-color",style={"text-decoration":"none","font-size":"9.25vw","line-height":"1"})
        ]),
    html.Nav([
        html.H1(redirect_main())
    ], className="navbar navbar-expand-md", style={"padding":"0 28% 0 30%"}), #end nav
    ])

##DEPRECIATED
page_resume = html.Div([
    nav_bar(),
    html.Iframe(id="embedded-pdf", src="assets\\Wilson_Ngo_Resume.pdf",style={"height":"100%","width":"100%","min-height":"100vh"})
    ])



app.layout = html.Div([
    dcc.Location(id='url',refresh=False),
    html.Div(id='page-content')
])

#Resume Modal
@app.callback(
    Output("Resume","is_open"),
    [
    Input("openResume", "n_clicks"),
    Input("closeResume","n_clicks")
    ],
    [
    State("Resume","is_open")
    ]
    )
def toggle_resume(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


#Raspi Modal
@app.callback(
    Output("Rosca","is_open"),
    [
    Input("openRosca", "n_clicks"),
    Input("closeRosca","n_clicks")
    ],
    [
    State("Rosca","is_open")
    ]
    )
def toggle_resume(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


#LobbyGuard Modal
@app.callback(
    Output("LobbyGuard","is_open"),
    [
    Input("openLobbyGuard", "n_clicks"),
    Input("closeLobbyGuard","n_clicks")
    ],
    [
    State("LobbyGuard","is_open")
    ]
    )
def toggle_resume(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#RaptorHub Modal
@app.callback(
    Output("RaptorHub","is_open"),
    [
    Input("openRaptorHub", "n_clicks"),
    Input("closeRaptorHub","n_clicks")
    ],
    [
    State("RaptorHub","is_open")
    ]
    )
def toggle_resume(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Commitment Alert Modal
@app.callback(
    Output("CAlert","is_open"),
    [
    Input("openCAlert", "n_clicks"),
    Input("closeCAlert","n_clicks")
    ],
    [
    State("CAlert","is_open")
    ]
    )
def toggle_resume(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


#Changing Pages
@app.callback(
    Output('page-content','children'),
    Input('url','pathname')
    )
def display_page(pathname):
    if pathname == '/reboot':
        return page_reboot
    elif pathname == '/main':
        return page_main
    elif pathname == '/resume':
        return page_resume
    else:
        return page_main #page_index
@app.callback(
    #suppress_callback_exceptions=True
    [
    Output('get_ip_ad', 'children'),
    Output('get_navbar', 'children'),
    ],
    Input('pw_input','value'),
    )
def check_password(pw_input):
    global guest
    if pw_input == password:
        guest = 0
        ip = get_ip_ad()     
        reboot = get_reboot()
    else:
        guest = 1
        ip = dash.no_update
        reboot = dash.no_update
    return ip,reboot

@app.callback(
    Output('reboot_btn', 'children'),
    Input('reboot_btn', 'n_clicks')
    )
def displayClick(btn1):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'reboot_btn' in changed_id:
        if debug_win == 1:
            msg = 'Rebooting...'
        else:
            msg = 'Rebooting...'
            subprocess.call(["sudo reboot now"], shell=True)
    else:
        msg = 'Reboot'
    return html.Div(msg)

#@app.callback(
#    [
 #   Output('rTimer', 'children'),
  #  Output('url','pathname')
   # ],
   # Input('interval', 'n_intervals')
   # )
#def update_timer(n):
 #   if 60-n <= 0:
  #      return str(0), '/'
   # else:
    #    return str(60-n), dash.no_update
class Dashboard():
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type','text/plain')])
        return ['Hello!']

if __name__ == '__main__':
    app.run_server(debug=isWin, host='0.0.0.0', port=8008)

Dashboard()