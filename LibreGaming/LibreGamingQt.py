import sys, os, subprocess
from LibreGaming import LibreGaming
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import QProcess


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.LibreGaming_Object = LibreGaming()
        self.PackageManager = self.LibreGaming_Object.getPackageManager()

        self.p = None
        self.setWindowTitle("LibreGamingQt") 
        self.setWindowIcon(QtGui.QIcon('joystick.png'))
        
        self.all_Btn = QPushButton("Install all the Gaming Packages(Steam,Wine-Staging,Gamemode,Lutris,Heroic,MangoHud & Goverlay)")
        self.basic_Btn = QPushButton("Install Basic Gaming Packages(Steam,Wine-Staging,Gamemode)")
        self.overlays_Btn = QPushButton("Install Mangohud & Goverlay")
        self.heroic_Btn = QPushButton("Install Heroic Launcher")
        self.heroicSUSE_Btn = QPushButton("Install Heroic Launcher (For OpenSUSE only)")
        self.lutris_Btn = QPushButton("Install Lutris Launcher")
        self.minigalaxy_Btn = QPushButton("Install Minigalaxy Launcher")
        self.itch_Btn = QPushButton("Install itch.io Launcher")
        self.ath_Btn = QPushButton("Install Athenaeum")

        self.all_Btn.setMinimumSize(0,50)
        self.basic_Btn.setMinimumSize(0,50)
        self.overlays_Btn.setMinimumSize(0,50)
        self.heroic_Btn.setMinimumSize(0,50)
        self.heroicSUSE_Btn.setMinimumSize(0,50)
        self.lutris_Btn.setMinimumSize(0,50)
        self.minigalaxy_Btn.setMinimumSize(0,50)
        self.itch_Btn.setMinimumSize(0,50)
        self.ath_Btn.setMinimumSize(0,50)

        self.all_Btn.pressed.connect(self.installAllPkgs)
        self.basic_Btn.pressed.connect(self.BasicPkgs)
        self.overlays_Btn.pressed.connect(self.Overlays)
        self.heroic_Btn.pressed.connect(self.Heroic)
        self.heroicSUSE_Btn.pressed.connect(self.HeroicSUSE)
        self.lutris_Btn.pressed.connect(self.Lutris)
        self.minigalaxy_Btn.pressed.connect(self.Minigalaxy)
        self.itch_Btn.pressed.connect(self.Itch)
        self.ath_Btn.pressed.connect(self.Athenaeum)
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

        l.addWidget(self.all_Btn)
        l.addWidget(self.basic_Btn)
        l.addWidget(self.overlays_Btn)
        l.addWidget(self.heroic_Btn)
        l.addWidget(self.heroicSUSE_Btn)
        l.addWidget(self.lutris_Btn)
        l.addWidget(self.minigalaxy_Btn)
        l.addWidget(self.itch_Btn)
        l.addWidget(self.ath_Btn)
        l.addWidget(self.text)        
        w = QWidget()
        w.setLayout(l)
        
        self.setup()
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

    def pre_setup(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
        if self.PackageManager == "yay" or self.PackageManager == "paru" or self.PackageManager == "pacman":
            self.p.start("pkexec pacman -S python3-pip")
        else:
            self.p.start("pkexec "+ self.PackageManager +" install python3-pip")
        self.p.waitForFinished()
        self.p.start("pkexec pip install LibreGaming")

    def setup(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start(self.pre_setup())

    def installAllPkgs(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("pkexec LibreGaming -g")

    def BasicPkgs(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("pkexec LibreGaming -b")

    def Lutris(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("pkexec LibreGaming --lutris")

    def Heroic(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            if self.PackageManager == "zypper":
                self.p.start("LibreGaming --lutris")            
            else:
                self.p.start("pkexec LibreGaming --lutris")

    def Overlays(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("pkexec LibreGaming -o")

    def Minigalaxy(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("LibreGaming --minigalaxy")

    def Itch(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("LibreGaming --itch")

    def Athenaeum(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("LibreGaming -ath")

app = QApplication(sys.argv)

w = MainWindow()
w.resize(900,800)
w.show()

app.exec_()