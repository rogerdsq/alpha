#!/usr/bin/env python2.5
import gtk

window = gtk.Window(gtk.WINDOW_TOPLEVEL)

label = gtk.Label("Hello World!")
window.add(label)

label.show()
window.show()

gtk.main()
