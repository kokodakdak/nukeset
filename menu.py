import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("Kokodak", icon="kokodak_logo.png")
m.addMenu("Draw")
m.addCommand("Draw/Timecode","nuke.createNode('burnintc')")
