# dicomJupyterExtension

This is Jupyter Notebook Extension for dicom images based on [OHIF Standalone Viewer](https://github.com/OHIF/Viewers/tree/master/StandaloneViewer).

## Installation:

1. Move `dicomViewer` and `dicomViewer.html` to the Jupyter Notebook `static` and `templates` folders, respectively. For example, if the Jupyter Notebook is installed in `/usr/local/lib/python2.7/dist-packages/notebook/`, the corresponding path should be `/usr/local/lib/python2.7/dist-packages/notebook/static` and `/usr/local/lib/python2.7/dist-packages/notebook/templates`;

2. Move `jupyterhandler` to python `sys.path`, e.g., `~/.local/lib/python2.7/site-packages`;

3. Launch Jupyter Notebook by  
`jupyter notebook --NotebookApp.nbserver_extensions="{'jupyterhandler.handler':True}"`.

Now single-clicking any `.dcm` file will open a new page with a dicom viewer.

## Browser on server:
We can use a browser on the server to view the dicom images. 

1. In a Ubuntu EC2 instance, install the browser, GNOME Web (Epiphany) by `sudo apt install epiphany-browser`;

2. Launch a GTK Broadway server by `broadwayd -a 0.0.0.0 -p 8080 :0`;

3. Launch the browser to visit Jupyter Notebook by   
`GDK_BACKEND=broadway BROADWAY_DISPLAY=:0 epiphany -i localhost:8888`;

4. Go to the url `YOUR_EC2_PUBLIC_IP:8080` to use the browser on the server.

## TODO:
* Limit the internet access of the browser so that it can only access the local machine, i.e., localhost:8888 (Jupyter Notebook)
