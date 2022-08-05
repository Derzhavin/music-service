import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.app:app",
                host="0.0.0.0",
                port=5000,
                reload=True,
                ssl_keyfile="./key.key",
                ssl_certfile="./cert.crt"
    )