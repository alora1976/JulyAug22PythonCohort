from flask import Flask, render_template, session, redirect


app=Flask(__name__)

app.secret_key="secret key."

