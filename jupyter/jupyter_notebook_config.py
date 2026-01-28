import os

# Spark Configuration
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}

# Allow all origins (for development)
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True

# Disable token for easier access (use with caution in production)
c.NotebookApp.token = ''
c.NotebookApp.password = ''

# Also configure for JupyterLab/ServerApp (Jupyter 3.0+)
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
