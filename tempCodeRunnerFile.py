import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
import speech_recognition as sr


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GURU BROWSER')
        self.setGeometry(100, 100, 800, 600)



        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.webview = QWebEngineView()
        self.webview.load(QUrl('https://duckduckgo.com/'))
        self.tabs.addTab(self.webview, "New Tab")
        self.setCentralWidget(self.tabs)



        # Create the toolbar
        self.toolbar = QToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setVisible(True)

        # Create the reload icon
        reload_icon = QIcon('reload.png')
        reload_action = QAction(reload_icon, 'Reload', self)
        reload_action.triggered.connect(self.webview.reload)
        self.toolbar.addAction(reload_action)

        # Create the previous icon
        prev_icon = QIcon('prev.png')
        prev_action = QAction(prev_icon, 'Previous', self)
        prev_action.triggered.connect(self.webview.back)
        self.toolbar.addAction(prev_action)

        # Create the next icon
        next_icon = QIcon('next.png')
        next_action = QAction(next_icon, 'Next', self)
        next_action.triggered.connect(self.webview.forward)
        self.toolbar.addAction(next_action)

        # Create the new tab icon
        new_tab_icon = QIcon('newtab.png')
        new_tab_action = QAction(new_tab_icon, 'New Tab', self)
        new_tab_action.triggered.connect(self.open_new_tab)
        self.toolbar.addAction(new_tab_action)



        # # Create the close tab icon
        # close_tab_icon = QIcon('closetab.png')
        # close_tab_action = QAction(close_tab_icon, 'Close Tab', self)
        # close_tab_action.triggered.connect(self.close_current_tab)
        # self.toolbar.addAction(close_tab_action)




    def open_new_tab(self):
        new_tab = QWebEngineView()
        new_tab.load(QUrl('https://duckduckgo.com/'))
        self.tabs.addTab(new_tab, "New Tab")
        self.tabs.setCurrentWidget(new_tab)

    def close_current_tab(self):
        current_index = self.tabs.currentIndex()
        self.tabs.removeTab(current_index)




    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.webview.load(q)
    def close_tab(self, index):
        self.tabs.removeTab(index)
app = QApplication(sys.argv)
app.setStyle("Fusion")



palette = QPalette()
palette.setColor(QPalette.Window, Qt.black)
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, Qt.black)
palette.setColor(QPalette.AlternateBase, Qt.black)
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, Qt.black)
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, Qt.cyan)
palette.setColor(QPalette.Highlight, Qt.cyan)
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)



browser = Browser()
browser.show()
sys.exit(app.exec_())

