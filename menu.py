import nuke
import nukescripts
import checkenv
import openfile

tb = nuke.toolbar("Nodes")
m = tb.addMenu("Kokodak", icon="kokodak_logo.png")
m.addMenu("Draw")
m.addCommand("Draw/Timecode","nuke.createNode('burnintc')")
m.addCommand("Draw/slate","nuke.createNode('slate')")

mb = menubar.addMenu("Kokodak")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/kokodakdak/nukeset/issues')")
mb.addCommand("-","-","")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()")
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()")
mb.addCommand("CheckENV","checkenv.main()")
mb.addCommand("OpenFile","reload(openfile);openfile.main()","F8", shortcutContext=2)
