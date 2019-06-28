import ipywidgets as widgets
from IPython.core.magic import line_magic, cell_magic, line_cell_magic, Magics, magics_class
from jupyter_interval_widget import Interval
from IPython.display import display, clear_output

@magics_class
class JupyterLiveMagics(Magics):
    @cell_magic
    def live(self, line='', cell=None):
        outer = self
        output = widgets.Output()
        def update_output(self):
            with output:
                clear_output(wait=True)
                outer.shell.run_cell(cell, store_history=False)

        interval = Interval(value=500)
        interval.on_tick(update_output)

        display(widgets.HBox(children=(output, interval)))
