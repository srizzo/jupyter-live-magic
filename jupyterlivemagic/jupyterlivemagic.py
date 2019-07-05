import ipywidgets as widgets
from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
from IPython.core.magic import line_magic, cell_magic, line_cell_magic, Magics, magics_class
from jupyter_interval_widget import Interval
from IPython.display import display, clear_output

@magics_class
class JupyterLiveMagic(Magics):
    @cell_magic
    @magic_arguments()
    @argument("-r", "--refresh-rate",
        type=int,
        default=1000,
        help="Refresh rate in milliseconds"
    )
    def live(self, line='', cell=None):
        args = parse_argstring(self.live, line)
        refresh_rate = args.refresh_rate

        outer = self
        output = widgets.Output()
        def update_output(self):
            with output:
                clear_output(wait=True)
                outer.shell.run_cell(cell, store_history=False)

        interval = Interval(value=refresh_rate)
        interval.on_tick(update_output)

        display(widgets.HBox(children=(output, interval)))
