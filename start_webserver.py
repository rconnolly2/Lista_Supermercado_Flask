from website import create_app


app = create_app() # Creo app de flask


if __name__ == "__main__":
    app.run(debug=True)