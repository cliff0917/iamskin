from dash import html
import dash_bootstrap_components as dbc
import feffery_antd_components as fac

import globals, database
from components import comment_img, bold_text

def serve(types):
    comments = []
    type_comments = database.read_data(types)

    if len(type_comments) == 0:
        return html.Div(
            fac.AntdEmpty(
                description=bold_text.serve('暫無評論'),
            )
        )
    
    # 新的 comment 會顯示在較上面
    for type_comment in type_comments[::-1]:
        comment_section, img = None, None
        name, time, rate, comment, img_path = type_comment

        if comment != '':
            comment_section = html.Div(
                [
                    fac.AntdText(
                        '評論：',
                        style={
                            'font-weight': 'bold',
                        },
                    ),
                    fac.AntdText(comment)
                ],
                style={
                    'margin-top': '5px',
                    'margin-left': '1rem',
                }
            )

        if img_path != '':
            img = comment_img.serve(img_path, '306px')

        single_comment = html.Div(
            [
                fac.AntdAvatar(
                    mode='icon',
                    size='xs',
                    style={
                        'backgroundColor': 'rgb(16, 105, 246)'
                    }
                ),
                fac.AntdText(
                    f'{name[0]}{"*" * 5}{name[-1]}',
                    style={
                        'margin-left': '5px',
                    }
                ),
                fac.AntdText(
                    time,
                    type='secondary',
                    style={
                        'margin-left': '1rem',
                    },
                ),
                html.Br(),
                fac.AntdText(
                    f'檢測類別：{globals.config["service_intro"][types]["title"][:2]}',
                    style={
                        'margin-left': '1rem',
                        'font-weight': 'bold',
                    },
                ),
                html.Br(),
                fac.AntdText(
                    '評分：',
                    style={
                        'margin-left': '1rem',
                        'font-weight': 'bold',
                    },
                ),
                fac.AntdRate(
                    count=5,
                    defaultValue=rate,
                    disabled=True,
                ),
                html.Br(),
                comment_section,
                img,
                html.Hr()
            ],
            style={
                'background-color': 'white'
            }
        )
        comments.append(single_comment)

    return html.Div(comments)