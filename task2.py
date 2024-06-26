from flask import Flask, send_file
from pydantic import BaseModel, ValidationError, field_validator
from lsystem import draw_lines, LFigure, LSystem2D
from io import BytesIO

app = Flask(__name__)

def l_system_file(grammatic: str):
    return send_file(path_or_file="file/quadratic Koch island - 2.png")



# /l_system/iter=3,angle=90,axiom="F-F-F-F",prod={'F': 'F-F+F+F'}
@app.route("/l_system/<grammatic>")
def l_system(grammatic: str):
    try:
        grammatic_ = grammatic.parse_obj(dict(el.split("=") for el in grammatic.split(",")))
        axiom = grammatic_.axiom
        productions = grammatic_.prod
        iterations = grammatic_.iter
        angel = grammatic_.angle
        lsystem = LSystem2D(axiom, productions, iterations, angel)
        figure = LFigure(lsystem, size=(1000, 1000))
        canvas = draw_lines(figure.lines)
        img_io = BytesIO()
        canvas.save(img_io, format='PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except ValidationError as e:
        result = "<ul>"
        for error in e.errors():
            result+= f"<li>{error}</li>"
        result += "</ul>"
        return result

@app.route('/test')
def test():
     # Def colors
    black = (  0,   0,   0, 255)
    white = (255, 255, 255, 255)
    # Def figure
    iterations = 7
    angel = 25 # In gradus
    axiom = 'f'
    productions = {
        'f': 'F-[[f]+f]+F[+Ff]-f',
        'F': 'FF',
    }

    lsystem = LSystem2D(axiom, productions, iterations, angel)
    figure = LFigure(lsystem, size=(1000, 1000))
    canvas = draw_lines(figure.lines)
    img_io = BytesIO()
    canvas.save(img_io, format='PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
