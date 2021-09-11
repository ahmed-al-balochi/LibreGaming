import sys, os
import LibreGaming
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import QProcess


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None
        self.setWindowTitle("LibreGamingQt") 
        self.setWindowIcon(QtGui.QIcon('joystick.png'))
        
        self.rootBtn = QPushButton("Get Root Access (Click here first to Install Gaming packages)")
        self.allBtn = QPushButton("Install All packages and ProtonGE")
        self.protonBtn = QPushButton("Install ProtonGE Only")
        self.gamesBtn = QPushButton("Install Gaming Packages Only")
        self.athBtn = QPushButton("Install Athenaeum (Not included in the 2nd option)")

        self.rootBtn.setMinimumSize(0,50)
        self.allBtn.setMinimumSize(0,50)
        self.protonBtn.setMinimumSize(0,50)
        self.gamesBtn.setMinimumSize(0,50)
        self.athBtn.setMinimumSize(0,50)

        self.rootBtn.pressed.connect(self.getRootAccess)
        self.allBtn.pressed.connect(self.InstallAll)
        self.protonBtn.pressed.connect(self.InstallProtonGE)
        self.gamesBtn.pressed.connect(self.InstallGamesPkgs)
        self.athBtn.pressed.connect(self.InstallAthenaeum)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QGridLayout()

        #newAction = QAction(QIcon('new.png'), '&New', self)

        menubar = QMenuBar()
        l.addWidget(menubar, 0, 0)
        menubar.addAction("About")
        menubar.triggered.connect(self.About)

        # setting font and size
        self.setFont(QFont('Ubuntu', 10))

        l.addWidget(self.rootBtn)
        l.addWidget(self.allBtn)
        l.addWidget(self.protonBtn)
        l.addWidget(self.gamesBtn)
        l.addWidget(self.athBtn)
        l.addWidget(self.text)        
        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def min(self, event):
        self.setWindowState(self.windowState() | QWindow.Minimized)
        event.accept()

    def close(self, event):
        self.setWindowState(self.windowState() | QWindow.Close)
        event.accept()

    def About(self):
        msgBox = QMessageBox()
        msgBox.about(self, "About", "Thank You for Using LibreGamingQt\n\n Author: Ahmed Al Balochi\n License: GPLv3 \n Email: a7mad98.work@gmail.com\n Github Page Link: https://github.com/Ahmed-Al-Balochi/LibreGaming")
    
    def message(self, s):
        self.text.appendPlainText(s)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Finished Installing',
            QProcess.Starting: 'Installation Starting',
            QProcess.Running: 'Installation Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        w.raise_()
        self.p = None

    def getRootAccess(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("gksu ls /")
            w.lower()

    def InstallAll(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("LibreGaming -a")

    def InstallProtonGE(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("protonup -y")

    def InstallGamesPkgs(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("LibreGaming -g")

    def InstallAthenaeum(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("flatpak install flathub com.gitlab.librebob.Athenaeum -y")

app = QApplication(sys.argv)

w = MainWindow()
w.resize(550,650)
w.show()

app.exec_()
