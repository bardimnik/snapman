import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from Snapman.paths import docpath
from Snapman.program_info import *


class AboutDialog(QWidget):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)

        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        labelIcon = QLabel()
        pixmap = QIcon.fromTheme(EXECUTABLE_NAME).pixmap(QSize(64, 64))
        labelIcon.setPixmap(pixmap)
        labelText = QLabel(PROGRAM_NAME)
        labelText.setFont(font)

        tabWidget = QTabWidget()
        tabWidget.addTab(AboutTab(), _("About"))
        tabWidget.addTab(VersionTab(), _("Version"))
        tabWidget.addTab(AuthorsTab(), _("Authors"))
        tabWidget.addTab(ThanksTab(), _("Thanks"))
        tabWidget.addTab(TranslationTab(), _("Translation"))

        btn = QPushButton(_("Close"), self)
        btn.setIcon(QIcon.fromTheme("window-close"))
        btn.setToolTip(_("Close this window"))
        btn.clicked.connect(self.close)

        labelLayout = QHBoxLayout()
        labelLayout.addWidget(labelIcon)
        labelLayout.addWidget(labelText, Qt.AlignLeft)

        mainLayout = QGridLayout()
        mainLayout.addLayout(labelLayout, 0, 0)
        mainLayout.addWidget(tabWidget, 1, 0)
        mainLayout.addWidget(btn, 2, 0, Qt.AlignRight)
        self.setLayout(mainLayout)

        self.setWindowTitle(_("About") + " " + PROGRAM_NAME)
        self.setWindowIcon(QIcon.fromTheme(EXECUTABLE_NAME))


class AboutTab(QWidget):
    def __init__(self, parent=None):
        super(AboutTab, self).__init__(parent)

        blank = QLabel()
        description = QLabel(DESCRIPTION)
        copyright = QLabel("© 2018, " + AUTHOR)
        source = QLabel(_("Source:") + " "
                        + "<a href='" + SOURCE + "'>" + SOURCE + "</a>")
        license = QLabel(_("License:") + " "
                         + "<a href='https://www.gnu.org/licenses/"
                         "gpl-3.0.en.html'>"
                         + _("GNU General Public License, version 3") + "</a>")

        source.setTextInteractionFlags(Qt.TextBrowserInteraction)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(blank)
        mainLayout.addWidget(blank)
        mainLayout.addWidget(blank)
        mainLayout.addWidget(description)
        mainLayout.addWidget(blank)
        mainLayout.addWidget(copyright)
        mainLayout.addWidget(source)
        mainLayout.addWidget(license)
        mainLayout.addStretch()
        self.setLayout(mainLayout)


class VersionTab(QWidget):
    def __init__(self, parent=None):
        super(VersionTab, self).__init__(parent)

        version = QLabel("<b>" + _("Version") + " " + VERSION + "<b>")
        using = QLabel(_("Using:") + " ")
        python = QLabel("<ul><li>Python " + PYVER)
        pyqt = QLabel("<ul><li>PyQt " + QT_VERSION_STR)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(version)
        mainLayout.addWidget(using)
        mainLayout.addWidget(python)
        mainLayout.addWidget(pyqt)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class AuthorsTab(QWidget):
    def __init__(self, parent=None):
        super(AuthorsTab, self).__init__(parent)

        blank = QLabel()
        notice = QLabel(_("Mail me if you found bugs."))
        name1 = QLabel("<b>" + AUTHOR + "<b>")
        task1 = QLabel("<i>" + _("Principle author") + "</i>")
        mail1 = QLabel("<pre>" + MAIL + "</pre>")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(notice)
        mainLayout.addWidget(blank)
        mainLayout.addWidget(name1)
        mainLayout.addWidget(task1)
        mainLayout.addWidget(mail1)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class ThanksTab(QWidget):
    def __init__(self, parent=None):
        super(ThanksTab, self).__init__(parent)

        blank = QLabel()
        notice = QLabel(_("Thank you for using my program."))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(blank)
        mainLayout.addWidget(notice)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class TranslationTab(QWidget):
    def __init__(self, parent=None):
        super(TranslationTab, self).__init__(parent)

        blank = QLabel()
        notice = QLabel(_("Please, mail me if you want to") + " "
                        + _("improve the translation."))
        name1 = QLabel("<b>" + AUTHOR + "<b>")
        task1 = QLabel("<i>" + _("Spanish and english translation") + "</i>")
        mail1 = QLabel("<pre>" + MAIL + "</pre>")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(notice)
        mainLayout.addWidget(blank)
        mainLayout.addWidget(name1)
        mainLayout.addWidget(task1)
        mainLayout.addWidget(mail1)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
