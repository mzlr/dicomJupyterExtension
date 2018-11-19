from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler


class viewerHandler(IPythonHandler):
    def get(self):
        self.set_header('Content-Type', 'text/html')
        html = self.render_template('dicomViewer.html')
        self.write(html)
        self.finish()
        

class redirectHandler(IPythonHandler):
    def get(self):
        
        new_query = '/viewer?url={"studies":[{"seriesList":[{"instances":[{"rows":1,"url":"dicomweb:' + \
        self.request.path.replace('/edit/','/files/') + \
        '"}]}]}]}'
        
        self.redirect(
            url_path_join(
                self.application.settings['base_url'], new_query))


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    
    route_pattern_redirect = url_path_join(web_app.settings['base_url'], '/edit/.*dcm')
    web_app.add_handlers(host_pattern, [(route_pattern_redirect, redirectHandler)])
    
    route_pattern_viewer = url_path_join(web_app.settings['base_url'], '/viewer')
    web_app.add_handlers(host_pattern, [(route_pattern_viewer, viewerHandler)])
