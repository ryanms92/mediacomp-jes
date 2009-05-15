# JES- Jython Environment for Students
# Copyright (C) 2002-2007 the JES team 
# See JESCopyright.txt for full licensing information
# This class, Copyright 2007, Alex Rudnick
# 5/13/09: Changes for redesigning configuration writing from python to java -Buck

import JESConfig
import java.awt as awt
import java.util as util
import java.awt.Event as Event
import java.awt.event.KeyEvent as KeyEvent
import java.lang as lang
import java.net as net
import javax.swing as swing
import java.io as io
import os

import JESConstants

import httplib, urllib, base64

COMMAND_SEND = "Send Report"
COMMAND_CANCEL = "Cancel"

BUGREPORTMESSAGE = """<html>If you find any problems with JES, or if anything
breaks unexpectedly, we'd love to know! You can use this form to send the
developers a note with your bug report. JES will only send us your first
name, so unless you tell us, we won't know exactly who you are.</html>"""

class JESBugReporter(swing.JFrame):

    def __init__(self):
        self.contentPane.layout = swing.BoxLayout(self.contentPane,
            swing.BoxLayout.Y_AXIS)
	
        self.add(swing.JLabel(BUGREPORTMESSAGE))

        self.add(swing.Box.createVerticalStrut(10))

        whbox = swing.Box(swing.BoxLayout.Y_AXIS)
        whlabel = swing.JLabel("<html>What went wrong to indicate a problem?</html>")
        self.whatHappenedArea = swing.JTextArea(5, 40)
        whbox.add(whlabel)
        whbox.add(self.whatHappenedArea)

        wydbox = swing.Box(swing.BoxLayout.Y_AXIS)
        wydlabel = swing.JLabel("<html>And what were you doing at the time? (please be as specific as possible)</html>")
        self.whatYouDidArea = swing.JTextArea(5, 40)
        wydbox.add(wydlabel)
        wydbox.add(self.whatYouDidArea)

        buttonbox = swing.Box(swing.BoxLayout.X_AXIS)
        self.sendbutton = swing.JButton(COMMAND_SEND,
            actionPerformed=self.actionPerformed)
        self.cancelbutton = swing.JButton(COMMAND_CANCEL,
            actionPerformed=self.actionPerformed)
        buttonbox.add(self.sendbutton)
        buttonbox.add(self.cancelbutton)

        self.add(whbox)
        self.add(wydbox)

        self.add(swing.Box.createVerticalStrut(10))
        self.add(buttonbox)

        whbox.setAlignmentX(awt.Component.LEFT_ALIGNMENT)
        wydbox.setAlignmentX(awt.Component.LEFT_ALIGNMENT)
        buttonbox.setAlignmentX(awt.Component.LEFT_ALIGNMENT)
        whlabel.setAlignmentX(awt.Component.LEFT_ALIGNMENT)
        wydlabel.setAlignmentX(awt.Component.LEFT_ALIGNMENT)

        self.whatYouDidArea.setAlignmentX(awt.Component.LEFT_ALIGNMENT)
        self.whatYouDidArea.setBorder(
            swing.BorderFactory.createEtchedBorder())

        self.whatYouDidArea.setLineWrap(1)
        self.whatYouDidArea.setWrapStyleWord(1)

        self.whatHappenedArea.setAlignmentX(awt.Component.LEFT_ALIGNMENT)
        self.whatHappenedArea.setBorder(
            swing.BorderFactory.createEtchedBorder())

        self.whatHappenedArea.setLineWrap(1)
        self.whatHappenedArea.setWrapStyleWord(1)

        self.pack()

        self.size = (450, 400)
	self.setLocationRelativeTo(None)
        self.show()

    def actionPerformed(self, event):
        cmd = event.getActionCommand()

        if cmd == COMMAND_SEND:
            if(self.whatHappenedArea.getText() != "" and self.whatYouDidArea.getText() != ""):
                self.sendBugReport()
                swing.JOptionPane.showMessageDialog(None,
                    "Thank you! The problem has been reported.")

        self.setVisible(0)
        self.dispose()

        # What happened?
        # (input box)
        # What were you doing when it happened?
        # (input box)
        # (submit) (cancel)

    def buildBugReport(self):
        studentName = JESConfig.getInstance().getStringProperty(JESConfig.CONFIG_NAME)
#        config = self.readFromConfigFile()
#        studentName = config[JESConstants.CONFIG_NAME]

        if(len(studentName) > 0):
            firstname = studentName.split()[0]
        else:
            firstname = 'Somebody'

        report = ("""
%s reports:<br/>
%s<br/>----<br/>
%s""") % (firstname,
          self.whatHappenedArea.getText(),
          self.whatYouDidArea.getText())

        return report

    def sendBugReport(self):
        userpass = 'attach:carmen'
        userpass = base64.encodestring(urllib.unquote(userpass)).strip()
        
        params = urllib.urlencode({'appendId': 1,
            'append': self.buildBugReport() })

        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain",
                   "Authorization":"Basic "+userpass}

        conn = httplib.HTTPConnection(JESConstants.COWEB_HOST)
        conn.request("POST", JESConstants.BUG_COWEB_ADDRESS, params, headers)

        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()

#    def readFromConfigFile(self):
#        try:
#            homedir=os.path.expanduser("~")
#            f=open(homedir+io.File.separator + JESConstants.JES_CONFIG_FILE_NAME,'r')
#            text=f.read()
#            f.close()
#            array=text.splitlines()
#            return array
#        except:
#            print "Error reading configuration file."
#            return ['Somebody']
            ## slightly gross; we're assuming that the name is always going
            ## to be the first thing in the file.
