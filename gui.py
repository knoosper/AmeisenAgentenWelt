import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


from gi.repository import Gtk, Gio

class HelloWorldApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="antworld",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_activate(self, data=None):
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.set_title("Ant Agent World")
        window.set_border_width(24)
        label = Gtk.Label("Hello World!")
        window.add(label)
        window.show_all()
        self.add_window(window)

if __name__ == "__main__":
    app = HelloWorldApp()
    app.run(None)





















"""
class gtk_aaw(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="AAW")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

win = Gaaw()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
"""
