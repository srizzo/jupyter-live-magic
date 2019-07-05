from .jupyterlivemagic import JupyterLiveMagic

def load_ipython_extension(ipython):
    ipython.register_magics(JupyterLiveMagic)
