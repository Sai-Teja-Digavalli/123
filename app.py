from flask import Flask, redirect, url_for, render_template, Response # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore
from VirtualPainter import VirtualPainter

app = Flask(__name__)
app.register_blueprint(VirtualPainter, url_prefix="")



if __name__ == "__main__":
    app.run(debug=True)
