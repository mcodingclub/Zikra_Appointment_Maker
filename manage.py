from app import create_app
from werkzeug.serving import run_simple

app=create_app()

if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == '__main__':
#     run_simple('localhost', 5000, app)        # I used Thread so when i interpt keyboared giving error to solve that error i am using run_simple