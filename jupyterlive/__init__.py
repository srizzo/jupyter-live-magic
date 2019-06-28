from .jupyterlive import JupyterLiveMagics

def load_ipython_extension(ipython):
    ipython.register_magics(JupyterLiveMagics)
