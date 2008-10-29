import sys
import javax.swing as swing
import javax.swing.table.AbstractTableModel as AbstractTableModel
import javax.swing.table.TableColumnModel as TableColumnModel
import java.awt as awt
import java.awt.EventQueue as EventQueue
import java.lang.Object as Object
import JESDebugger
import java.util.Hashtable as Hashtable
import JESGutter
import java.io.FileWriter as FileWriter #Added by Brian for debugging
import media
import java.lang.System as System
from java.lang import Thread
from java.lang import Runnable

MAX_LINES = 200
CROPPED_MESSAGE = '<<LINES ABOVE WERE CROPPED>>'
BUTTON_SIZE=(50,50)
HIGHLIGHT_COLOR = awt.Color.green

def variableDialog(ui):
    var = swing.JOptionPane.showInputDialog(ui, 'Please type the variable to watch')
    return var

def pickVariable(ui, vars):
    if len(vars) > 0:
        var = swing.JOptionPane.showInputDialog(ui,
                                                "Choose Variable to remove",
                                                "Input",
                                                swing.JOptionPane.INFORMATION_MESSAGE,
                                                None,
                                                vars,
                                                vars[0])
        return var
    else:
        swing.JOptionPane.showMessageDialog(ui,
                                           'There are no variables to remove',
                                           'Error',
                                           swing.JOptionPane.ERROR_MESSAGE)
        return None

#-------------------------------------------------------------------------------
class DBControlPanel(swing.JPanel):
    def __init__(self, debugger):
        self.lastValue = None
        self.debugger = debugger
        MAX_SPEED = debugger.MAX_SPEED
        self.slider = swing.JSlider(swing.JSlider.HORIZONTAL, 0, MAX_SPEED,
                                    self.debugger.speed,
                                    stateChanged=self.stateChanged)
        self.last_speed = self.debugger.speed
        labels = Hashtable()
        labels.put(0, swing.JLabel('slow'))
        labels.put(MAX_SPEED, swing.JLabel('fast'))
        self.slider.labelTable = labels
        self.slider.paintLabels = 1

        self.addButton = swing.JButton(swing.ImageIcon('images/plus.jpg'),
                                       actionPerformed=self.actionPerformed,
                                       toolTipText='add Variable',
                                       preferredSize=BUTTON_SIZE)
        self.deleteButton = swing.JButton(swing.ImageIcon('images/minus.jpg'),
                                       actionPerformed=self.actionPerformed,
                                       toolTipText='remove Variable',
                                       preferredSize=BUTTON_SIZE)
        self.stepButton = swing.JButton(swing.ImageIcon('images/boot.jpg'),
                                        actionPerformed=self.actionPerformed,
                                        toolTipText='step',
                                        preferredSize=BUTTON_SIZE)
	self.pauseIcon = swing.ImageIcon('images/pause.jpg')
	self.runIcon = swing.ImageIcon('images/run.jpg')
        self.runButton = swing.JButton(self.runIcon,
                                        actionPerformed=self.actionPerformed,
                                        toolTipText='run',
                                       preferredSize=BUTTON_SIZE)
        self.fullspeedButton = swing.JButton(swing.ImageIcon('images/fullspeed.jpg'),
                                        actionPerformed=self.actionPerformed,
                                        toolTipText='full speed',
                                       preferredSize=BUTTON_SIZE)
        self.stopButton = swing.JButton(swing.ImageIcon('images/stop.jpg'),
                                        actionPerformed=self.actionPerformed,
                                        toolTipText='stop',
                                        preferredSize=BUTTON_SIZE)
        self.setLayout(swing.BoxLayout(self, swing.BoxLayout.X_AXIS))
        self.add(self.slider)
        self.add(self.addButton)
        self.add(self.deleteButton)
        #self.add(self.stepButton) # These two lines commented out by Brian O because of removed Pause functionality -- 23 June 2008
        #self.add(self.runButton)
        self.add(self.fullspeedButton)
        self.add(self.stopButton)
	self.initialButtonState()

    def stateChanged(self, e):
        value = self.slider.getValue()
        self.debugger.speed = value
        if value == 0:
            self.stepButton.setEnabled(1)
            self.pauseState()
        elif self.lastValue == 0:
            self.stepButton.setEnabled(0)
            self.run()
        self.lastValue = value

    def actionPerformed(self, e):
        source = e.getSource()
        if source == self.runButton:
	    if source.icon == self.runIcon:
		self.run()
	    else:
                self.pause()
        elif source == self.fullspeedButton:
	    self.fullspeed()
        elif source == self.stopButton:
	    self.debugger.stopThread()
	    self.stop()
	elif source == self.stepButton:
	    self.step()
	elif source == self.addButton:
            self.debugger.watcher.watchVariable()
        elif source == self.deleteButton:
            self.debugger.watcher.unwatchVariable()

    def refreshSlider(self):
        self.slider.value = self.debugger.speed
            
    def run(self):
        self.runButton.icon = self.pauseIcon
        self.runButton.toolTipText = 'pause'
        if self.debugger.speed == 0:
            self.debugger.setSpeed(self.last_speed)
        self.runButton.enabled = 1
        self.fullspeedButton.enabled = 1
        self.stepButton.enabled = 0
        self.stopButton.enabled = 1
        self.addButton.enabled = 0
        self.deleteButton.enabled = 0
        self.debugger.step()

    def pause(self):
        self.last_speed = self.debugger.speed
        self.debugger.setSpeed(0)
        self.pauseState()

    def stop(self):
	self.initialButtonState()

    def fullspeed(self):
        # kinda like run, but full speed
        self.runButton.icon = self.pauseIcon
        self.runButton.toolTipText = 'pause'
        self.debugger.setSpeed(self.debugger.MAX_SPEED)
        self.fullspeedButton.enabled = 1 
        self.runButton.enabled = 1
        self.stepButton.enabled = 0
        self.stopButton.enabled = 1
        self.addButton.enabled = 0
        self.deleteButton.enabled = 0
        self.debugger.step()

    def initialButtonState(self):
        self.stepButton.enabled = 0
        self.runButton.enabled = 0
        self.stopButton.enabled = 0
        self.addButton.enabled = 1
        self.deleteButton.enabled = 1
        self.fullspeedButton.enabled = 0

    def pauseState(self):
        self.runButton.icon = self.runIcon
        self.runButton.toolTipText = 'run'
        self.stepButton.enabled = 1
        self.runButton.enabled = 1
        self.fullspeedButton.enabled = 1
        self.addButton.enabled = 1
        self.deleteButton.enabled = 1
        self.stopButton.enabled = 1

#-------------------------------------------------------------------------------
class JESDBVariableWatcher(swing.JPanel):
    def __init__(self, debugger):
	self.debugger = debugger
	self.controlPanel = DBControlPanel(self.debugger)
	self.history = ExecHistory(self.debugger)
	self.table = WatcherTable(self.history)
	self.rendererComponent = swing.JLabel(opaque=1)
	self.table.setDefaultRenderer(Object, MyRenderer())
	self.history.setColumnWidths(self.table)
	self.scrollPane = swing.JScrollPane(self.table) 
        self.scrollPane.verticalScrollBar.model.stateChanged = self.stateChanged
        self.setLayout(awt.BorderLayout())
        self.add(self.scrollPane, awt.BorderLayout.CENTER)
        self.add(self.controlPanel, awt.BorderLayout.NORTH)
        self.lastScrollMaximum = None
        
    def stateChanged(self, event):
        brmodel = event.source
        if brmodel.maximum <> self.lastScrollMaximum:
            brmodel.value = brmodel.maximum
            self.lastScrollMaximum = brmodel.maximum

    def watchVariable(self):
        var = variableDialog(self)
        if var:
            self.history.appendVariable(var)

    def unwatchVariable(self):
        var = pickVariable(self, self.debugger.watcher.getVariables())
        if var:
            self.history.removeVariable(var)

    def getVariables(self):
	return self.history.vars

    def clear(self):
	self.history.clear()

    def snapShot(self, line_no, instr):
        self.history.snapShot(line_no, instr)

    def endExecution(self):
	self.history.endExecution()

#-------------------------------------------------------------------------------
class MyRenderer(swing.JLabel, swing.table.TableCellRenderer):
    def __init__(self):
        self.opaque = 1
        
    def getTableCellRendererComponent(self, table, value, isSelected, hasFocus, row, col):
        self.text = str(value)
        if row <> table.rowCount - 1:
            self.background = awt.Color.white
        else:
            self.background = HIGHLIGHT_COLOR
        return self

#-------------------------------------------------------------------------------
class WatcherTable(swing.JTable):
    def tableChanged(self, event):
	swing.JTable.tableChanged(self, event)
        if event.getFirstRow() == swing.event.TableModelEvent.HEADER_ROW:
            self.model.setColumnWidths(self)
	#if EventQueue.isDispatchThread():
	#    self.resizeAndRepaint()
#-------------------------------------------------------------------------------
class ExecHistory(AbstractTableModel):
    def __init__(self, debugger):
	self.lines = []
	self.debugger = debugger
	self.vars = []
	self.nextLine = None
	#self.fw = FileWriter("debugger.txt")

    #Required by table model interface
    def getRowCount(self):
	return len(self.lines)

    #Required by table model interface
    def getColumnCount(self):
	return 3 + len(self.vars)

    #Required by table model interface
    def getValueAt(self, row, col):
	line = self.lines[row]
	if col < len(line):
	    return self.lines[row][col]
        else:
	    return ''

    def getColumnName(self, col):
	if col == 0:
	    return 'step'
        elif col == 1:
	    return 'line'
        elif col == 2:
	    return 'instruction'
        else:
	    return 'var: ' + self.vars[col-3]

    def setColumnWidths(self, table):
        columnModel = table.columnModel
        columnModel.getColumn(0).preferredWidth = 10   # step
        columnModel.getColumn(1).preferredWidth = 10   # line number
        columnModel.getColumn(2).preferredWidth = 150  # instruction
        for i in range(len(self.vars)):
            columnModel.getColumn(i + 3).setPreferredWidth(15)

    def endExecution(self):
	if self.nextLine:
	    self.lines.append(self.nextLine)
	    #### Added a row, inform the table manager
        if EventQueue.isDispatchThread():
            self.fireTableStructureChanged()
        else:
            runner = changeRunner()
            runner.model = self
            EventQueue.invokeLater(runner)
	    self.debugger.interpreter.program.gui.editor.document.removeLineHighlighting() # also update the editor currentline highlight
            self.nextLine = None

    def appendVariable(self, var):
	class appendRunner(Runnable):
	    self.model = None
	    def run(self):
		self.model.fireTableStructureChanged()

	self.vars.append(var)
        #### Added a column, inform the table manager
	if EventQueue.isDispatchThread():
	    self.fireTableStructureChanged()
	else:
	    runner = appendRunner()
	    runner.model = self
	    EventQueue.invokeLater(runner)

    def removeVariable(self, var):
	class removeRunner(Runnable):
	    self.model = None
	    def run(self):
		self.model.fireTableStructureChanged()
        self.vars.remove(var)
        #### Removed a column, inform the table manager
	if EventQueue.isDispatchThread():
	    self.fireTableStructureChanged()
	else:
	    runner = removeRunner()
	    runner.model = self
	    EventQueue.invokeLater(runner)

    def snapShot(self, line_no, instr):
	values = []
	#Get the value of each variable being watched
	for var in self.vars:
            try:
                value = eval(var, self.debugger.curframe.f_globals,
                             self.debugger.curframe.f_locals)
                values.append(value)
            except:
                values.append('-') # add dummy
	self.addLine(line_no, instr, values)

    def addLine(self, line_no, instr, values):
	if self.nextLine:
	    fire = 1
	    
	    #If the number of steps is greater than MAX_LINES
	    if len(self.lines) > MAX_LINES:
		#If we have already started cropping lines
                if self.lines[0][1] == CROPPED_MESSAGE:
                    self.lines.remove(self.lines[1])
                    #### Deleted a row, inform the table manager
                    if fire and EventQueue.isDispatchThread():
                        self.fireTableRowsDeleted(1,1)
                    elif fire:
                        runner = deleteRunner()
                        runner.start = 1
                        runner.end = 1
                        runner.model = self
                        EventQueue.invokeLater(runner)
		#We have not started cropping lines yet
                else:
                    line = ['-', CROPPED_MESSAGE]
                    self.lines[0] = line
                    ##### Modified a row, inform the table manager
                    if fire and EventQueue.isDispatchThread():
                        self.fireTableRowsUpdated(0,0)
                    elif fire:
                        runner = updateRunner()
                        runner.model = self
                        EventQueue.invokeLater(runner)
            
	    self.nextLine.extend(values) #Add the variable values to nextLine
            self.lines.append(self.nextLine) #Put nextLine in the list
            #### Inserted a row, inform the table manager
	    if fire and EventQueue.isDispatchThread():
		self.fireTableRowsInserted(len(self.lines)-1, len(self.lines)-1)
	    elif fire:
	        runner = insertRunner()
	    	runner.model = self
	    	EventQueue.invokeLater(runner)
		#Thread.sleep(500)
	    # also update the editor currentline highlight
            #if fire: 
            #    self.debugger.interpreter.program.gui.editor.document.highlightLine(self.nextLine[1])
	    
	    #DEBUGGING - PRINT LINE DATA TO FILE
	    #self.fw.write(str(self.nextLine[0]))
	    #for i in range(1,len(self.nextLine)):
		#self.fw.write("\t")
		#self.fw.write(str(self.nextLine[i]))
	    #self.fw.write("\r\n")
	    #self.fw.flush()
	    #END DEBUGGING BLOCK
        
	self.nextLine = [] #Clear nextLine to begin filling it with next step
        
        #Set the step number
	if len(self.lines) > 0:
            self.nextLine.append(self.lines[len(self.lines)-1][0]+1)
        else:
            self.nextLine.append(1)
	    
	#Add the line number and instruction to the nextLine
        self.nextLine.append(line_no) 
        self.nextLine.append(instr)

    def clear(self):        
        self.nextLine = None
        numrows = len(self.lines)
        self.lines = []
        #### Deleted all rows, inform the table manager
        if numrows > 0:
            if EventQueue.isDispatchThread():
                self.fireTableRowsDeleted(0, numrows-1)
            else:
                runner = deleteRunner()
                runner.end = numrows-1
                runner.model = self
                EventQueue.invokeLater(runner)

#-------------------------------------------------------------------------------
class deleteRunner(Runnable):
    model = None
    start = 0
    end = 0
    def run(self):
        self.model.fireTableRowsDeleted(self.start, self.end)

class insertRunner(Runnable):
    model = None
    def run(self):
        self.model.fireTableRowsInserted(len(self.model.lines)-1, len(self.model.lines)-1)

class updateRunner(Runnable):
    model = None
    def run(self):
        self.model.fireTableRowsUpdated(0,0)
        
class changeRunner(Runnable):
    model = None
    def run(self):
        self.model.fireTableStructureChanged()
    
