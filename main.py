from app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


"""
    For Aws EC2, Uncomment the lines below:
    from waitress import serve
        from app import app

    if __name__ == '__main__':
        serve(app, host='0.0.0.0', port=80)

"""