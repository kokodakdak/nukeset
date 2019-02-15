import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("Kokodak")
m.addMenu("Draw")
m.addCommand("Draw/Timecode","nuke.createNode('burnintc')")
