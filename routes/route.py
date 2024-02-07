from routes.manageUsers.manage import login, register

def routes(app,render_template):
    
    login(app,render_template)
    register(app, render_template)