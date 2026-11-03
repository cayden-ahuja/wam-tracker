from app import create_app

app = create_app()

if __name__ == '__main__':
    # Port 5001... macOS uses 5000 for AirPlay Receiver
    app.run(debug=True, port=5001)