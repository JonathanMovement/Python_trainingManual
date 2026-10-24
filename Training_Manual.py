import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QPushButton, QVBoxLayout, QCompleter, 
                             QHBoxLayout, QRadioButton, QButtonGroup, 
                             QTextEdit, QComboBox, QListWidget, QStackedWidget, QSizePolicy, 
                             QToolBar, QAction, QMainWindow, QMenu, QGridLayout, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPainter, QBrush, QPainterPath

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.base_style = """
            QLabel, QPushButton{
                font-family: arial black;
            }
            QLabel#welcome_label{
                font-size: 30px;
                font-style: normal;
                background-color: #c8c9cc;
                border-radius: 15px;
                padding: 5px;
            }
            QPushButton#basics_button{
                font-size: 30px;
                background-color: #71747a;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton#basics_button:hover{
                background-color: #454545;
            }
            QPushButton#intermediate_button{
                font-size: 30px;
                background-color: #61656b;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton#intermediate_button:hover{
                background-color: #454545;
            }
            QPushButton#advanced_button{
                font-size: 30px;
                background-color: #fa1414;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton#dark_mode{
                font-size: 20px;
                background-color: #403d3d;
                font-weight: bold;
                padding: 10px;
            }
"""
        self.light_theme = """
            QWidget{
                background-color: #c7c0af;
            }
            QLabel{
                color: black;
            }
            QPushButton{
                background-color: #d0d0d0;
                color: black;
            }
"""
        self.dark_theme = """
            QWidget{
                background-color: #1e1e1e;
            }
            QLabel{
                color:white;
            }
            QPushButton{
                background-color: #333333;
                color: white;
            }
            QLabel#welcome_label{
                background-color: #292828;
                padding: 5px;
                border-radius: 15px;
            }
"""

        self.welcome_label = QLabel("Welcome to the Python interactive Training-Manual", self)
        self.basics_btn = QPushButton("Basics", self)
        self.intermediate_btn = QPushButton("Python Intermediate", self)
        self.advanced_btn = QPushButton("Python Advanced", self)
        self.theme_button = QPushButton("Dark Mode", self)

        # Image + rounded corners method
        self.image_label = QLabel()
        pixmap = self.rounded_pixmap("Pictures, icons//PythonADHD.jpg", 50)
        pixmap = pixmap.scaledToWidth(800, Qt.SmoothTransformation) # scaling the picture
        self.image_label.setPixmap(pixmap)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Python Training Manual")

        main_layout = QVBoxLayout()
        #  Center label
        self.welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        main_layout.addWidget(self.welcome_label)
        # Horizontal layout: left buttons + right image
        center_row = QHBoxLayout()
        
        # Left side buttons column
        left_buttons = QVBoxLayout()
        left_buttons.setAlignment(Qt.AlignCenter | Qt.AlignLeft)
        left_buttons.addWidget(self.basics_btn)
        left_buttons.addWidget(self.intermediate_btn)
        left_buttons.addWidget(self.advanced_btn)
        # Adding left column + right image
        center_row.addLayout(left_buttons)
        center_row.addStretch() # pushes the image to the right
        center_row.addWidget(self.image_label)

        main_layout.addLayout(center_row)
        # Spacer to push theme button to the bottom
        main_layout.addStretch()
        # container for right-align button
        bottom_row = QHBoxLayout()
        bottom_row.addStretch() # pushes next widget to the right
        bottom_row.addWidget(self.theme_button)

        main_layout.addLayout(bottom_row)
        self.setLayout(main_layout)

        # specific object naming for each button
        self.welcome_label.setObjectName("welcome_label")
        self.basics_btn.setObjectName("basics_button")
        self.intermediate_btn.setObjectName("intermediate_button")
        self.advanced_btn.setObjectName("advanced_button")
        self.image_label.setObjectName("PythonADHD_img")
        self.theme_button.setObjectName("dark_mode")

        # connecting the intermediate button with the open_intermediate_page method
        self.intermediate_page = IntermediatePage(self)
        self.intermediate_btn.clicked.connect(self.open_intermediate_page)
        self.basics_page = BasicsPage(self)
        self.basics_btn.clicked.connect(self.open_basics_page)
        self.advanced_page = AdvancedPage(self)
        self.advanced_btn.clicked.connect(self.open_advanced_page)

        self.theme_button.clicked.connect(self.toggle_theme) # connecting the theme button to toggle_theme method

        self.setStyleSheet(self.base_style + self.light_theme) # Window will start initially in light mode

    def toggle_theme(self):
        if self.theme_button.text() == "Dark Mode":
            self.setStyleSheet(self.base_style + self.dark_theme)
            self.theme_button.setText("Light Mode")
        else:
            self.setStyleSheet(self.base_style + self.light_theme)
            self.theme_button.setText("Dark Mode")

    def open_intermediate_page(self):
        self.hide()
        self.intermediate_page.resize(1600, 900)
        self.intermediate_page.show()

    def open_basics_page(self):
        self.hide()
        self.basics_page.resize(1600, 900)
        self.basics_page.show()
    
    def open_advanced_page(self):
        self.hide()
        self.advanced_page.resize(500, 500)
        self.advanced_page.show()

    @staticmethod # defining a method to round the corners of the image
    def rounded_pixmap(path, radius):
        pixmap = QPixmap(path)
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)

        path_obj = QPainterPath()
        path_obj.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
        painter.setClipPath(path_obj)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return rounded
    
class IntermediatePage(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.initital_pixmap = QPixmap("Pictures, icons//Intermediate_thumbnail.png")

        self.setWindowTitle("Python Intermediate")

        self.base_style = """
    QLabel, QPushButton{
        font-family: arial black;
        font-size: 35px;
        font-style: normal;
        background-color: #71747a;
        border-radius: 10px;
        padding: 5px;
        margin: 1px;
    }
    QPushButton:hover{
        background-color: #615555;
    }
    QComboBox{
    font-family: calibri;
    font-size: 25px;
    color: #000000;
    font-weight: bold;
    }
"""
        self.light_theme = """
    QWidget{
        background-color: #bdb7b7;
    }
    QPushButton{
        background-color: #d0d0d0;
        color: black;
        padding: 5px;
        margin: 0px;
    }
    QComboBox{
        background-color: #6e5c5c;
    }
    QTextEdit{
        background-color: #ffffff;
        color: #000000;
        font-size: 20px;
    }
"""
        self.dark_theme = """
    QWidget{
        background-color: #1e1e1e;
    }
    QPushButton{
        background-color: #333333;
        color: white;
        padding: 5px;
        margin: 0px;
    }
    QComboBox{
        background-color: #bf0808;
        color: #ffffff;
    }
    QTextEdit{
        background-color: #1e1e1e;
        color: #ffffff;
        font-size: 20px;
    }
"""
        self.image_frame_style = """
    QLabel#contentImage{
        background-color: rgba(0, 0, 0, 20);
        border-radius: 20px;
        padding-top: 30px;
        padding-bottom: 30px;
    }
"""
        # All app widgets / objects
        self.button1func = QPushButton("Functions")
        self.button2clas = QPushButton("Classes")
        self.button3meth = QPushButton("Methods")
        self.button4mod = QPushButton("Modules")
        self.button5api = QPushButton("APIs")
        self.button6deco = QPushButton("Decorators")
        self.button7exce = QPushButton("Exceptions")
        self.button8back = QPushButton("Back")
        self.button9dark = QPushButton("Dark Mode")
        self.button10add = QPushButton("Show Image")
        self.button10add.hide()

        # Dropdown boxes
        self.filterbox1 = QComboBox()
        self.filterbox1.addItem("Functions / Options")
        self.filterbox1.addItem("Explaining return")
        self.filterbox1.addItem("Connecting Functions")
        self.filterbox1.addItem("Lambda Functions")

        self.filterbox2 = QComboBox()
        self.filterbox2.addItem("Methods / Options")
        self.filterbox2.addItem("@staticmethods")
        self.filterbox2.addItem("@property Methods")
        self.filterbox2.addItem("Magic Methods")
        self.filterbox2.addItem("@classmethods")

        self.filterbox3 = QComboBox()
        self.filterbox3.addItem("Modules / Options")
        self.filterbox3.addItem("os Module")
        self.filterbox3.addItem("datetime Module")
        self.filterbox3.addItem("requests Module")
        self.filterbox3.addItem("math Module")

        # Adding state variables
        self.current_topic = None
        self.current_view_mode = "image"
        self.topic_images = {
            "functions": "Pictures, icons//Functions.png",
            "classes": "Pictures, icons//Classes.png",
            "@staticmethods": "Pictures, icons//Staticmethods.png",
            "APIs": "Pictures, icons//APIs.png",
        }
        
        # Creating 2 reusable widgets, Picture or text
        self.content_stack = QStackedWidget()
        self.content_stack.setSizePolicy( # This will allow proper widget scaling inside the methods
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        self.image_label = QLabel("Image will appear here!")
        self.image_label.setObjectName("contentImage")
        self.image_label.setSizePolicy( # This will allow proper image scaling inside the methods
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        self.image_label.setAlignment(Qt.AlignCenter)
        self.content_stack.addWidget(self.image_label)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(False)
        self.text_area.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.text_area.setCursor(Qt.IBeamCursor)
        self.content_stack.addWidget(self.text_area)

        # Window design
        self.master_layout = QHBoxLayout() # ROW
        self.master_layout.setSpacing(10)

        self.col1 = QVBoxLayout() # frist column
        self.col1.setSpacing(4)
        self.col1.setContentsMargins(5, 5, 5, 5)
        self.col2 = QVBoxLayout() # second column for image, additional + dark mode buttons
        self.col2.setSpacing(6)
        self.col2.setContentsMargins(5, 5, 5, 5)
        self.right_buttons = QHBoxLayout() # additional, dark mode, back buttons

        self.col1.addWidget(self.button1func)
        self.col1.addWidget(self.button2clas)
        self.col1.addWidget(self.button3meth)
        self.col1.addWidget(self.button4mod)
        self.col1.addWidget(self.button5api)
        self.col1.addWidget(self.button6deco)
        self.col1.addWidget(self.button7exce)

        self.col1.addWidget(self.filterbox1)
        self.col1.addWidget(self.filterbox2)
        self.col1.addWidget(self.filterbox3)

        self.right_buttons.addWidget(self.button10add)
        self.right_buttons.addWidget(self.button9dark)
        self.right_buttons.addWidget(self.button8back)
        self.right_buttons.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        

        self.col2.addWidget(self.content_stack)

        self.col2.addLayout(self.right_buttons)

        self.master_layout.addLayout(self.col1, 20)
        self.master_layout.addLayout(self.col2, 80)
        self.setLayout(self.master_layout)

        self.setStyleSheet(self.base_style + self.light_theme) # Base style + light theme set initially

        self.show_startup_image()

        self.button8back.clicked.connect(self.go_back)
        self.button1func.clicked.connect(self.load_functions)
        self.button9dark.clicked.connect(self.switch_theme)
        self.button10add.clicked.connect(self.show_topic_image)
        self.button2clas.clicked.connect(self.load_classes)
        self.button5api.clicked.connect(self.load_apis)
        self.button3meth.clicked.connect(self.load_methods)
        self.button4mod.clicked.connect(self.load_modules)
        self.button6deco.clicked.connect(self.load_decorators)
        self.button7exce.clicked.connect(self.load_exceptions)
        self.filterbox1.currentIndexChanged.connect(self.on_functions_option_changed)
        self.filterbox2.currentIndexChanged.connect(self.on_methods_option_changed)

    #-----------------show text content method---------------------------
    def show_text(self, file_path, topic):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            content = "Text file not found."

        if file_path.endswith(".md"):
            self.text_area.setMarkdown(content)
        else:
            self.text_area.setPlainText(content)

        self.content_stack.setCurrentWidget(self.text_area)

        self.current_topic = topic
        self.current_view_mode = "text"

        if topic in self.topic_images:
            self.button10add.show()
        else:
            self.button10add.hide()
    #-----------------show image toggle logic method---------------------
    def show_topic_image(self):
        if self.current_topic is None:
            return
        
        image_path = self.topic_images.get(self.current_topic)
        if not image_path:
            return
        if self.current_topic == "classes":
            self.show_image(image_path, max_width=1600, max_height=780)
        elif self.current_topic == "APIs":
            self.show_image(image_path, max_width= 1220, max_height=700)
        else:
            self.show_image(image_path, max_width=1300, max_height=780)

        self.current_view_mode = "image"
        self.button10add.hide()
        self.current_topic = None
        self.current_view_mode = "image"

    def load_classes(self): # Classes button method (text file)
        self.show_text(
            file_path="Text_files//Classes.md",
            topic="classes"
        )
    
    def load_apis(self): # APIs button method (text file)
        self.show_text(
            file_path="Text_files//APIs.md",
            topic="APIs"
        )
    
    def hide_image_button(self): # Hide "show image" button method
        self.button10add.hide()
        self.current_topic = None
        self.current_view_mode = "image"

    def go_back(self): # Back button method
        self.hide()
        self.parent_window.show()

    def show_startup_image(self): # Start up image method
        self.show_image(
            "Pictures, icons//Intermediate_thumbnail.png",
            max_width=1200,
            max_height=800
        )

    def show_image(self, path, max_width=None, max_height=None): # Showing image content method
        pixmap = MainWindow.rounded_pixmap(path, radius=25)

        if pixmap.isNull():
            self.image_label.setText("Image not found")
            self.content_stack.setCurrentWidget(self.image_label)
            return
        
        if max_width or max_height:
            pixmap = pixmap.scaled(
                max_width or pixmap.width(),
                max_height or pixmap.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        else:
            pixmap = pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        self.image_label.setPixmap(pixmap)
        self.image_label.setStyleSheet("")
        if "Return.png" in path:
            self.image_label.setStyleSheet(self.image_frame_style)
        self.content_stack.setCurrentWidget(self.image_label)

    def load_functions(self): # Method showing functions image
        self.hide_image_button()
        self.show_image("Pictures, icons//Functions.png", max_width=1300, max_height=780)

    def load_methods(self): # Method showing methods image
        self.hide_image_button()
        self.show_image("Pictures, icons//Methods.png", max_width=1400, max_height=780)

    def load_modules(self): # Method showing modules image
        self.hide_image_button()
        self.show_image("Pictures, icons//Modules.png", max_width=1400, max_height=780)

    def load_decorators(self): # Method showing decorators image
        self.hide_image_button()
        self.show_image("Pictures, icons//Decorators.png", max_width=1600, max_height=780)

    def load_exceptions(self):
        self.hide_image_button()
        self.show_image("Pictures, icons//Exceptions.png", max_width=1200, max_height=780)

    def showEvent(self, event): # This method will show the default startup picture when reloading Intermediate layout
        super().showEvent(event)
        self.show_startup_image()

    def switch_theme(self):
        if self.button9dark.text() == "Dark Mode":
            self.setStyleSheet(self.base_style + self.dark_theme)
            self.button9dark.setText("Light Mode")
        else:
            self.setStyleSheet(self.base_style + self.light_theme)
            self.button9dark.setText("Dark Mode")

    #---------------------- COMBOBOX methods ---------------------------------
    def on_functions_option_changed(self, index):
        text = self.filterbox1.itemText(index)
        if text == "Functions / Options":
            self.show_startup_image()
        elif text == "Explaining return":
            self.button10add.hide()
            self.show_image("Pictures, icons//Return.png", max_width=1200, max_height=800)
        elif text == "Connecting Functions":
            self.button10add.hide()
            self.show_image("Pictures, icons//Combining_functions.png", max_width= 1300, max_height=720)
        elif text == "Lambda Functions":
            self.show_image("Pictures, icons//Lambda Functions.png", max_width=1200, max_height=800)

    def on_methods_option_changed(self, index):
        text = self.filterbox2.itemText(index)

        if text == "Methods / Options":
            self.show_startup_image()
        elif text == "@staticmethods":
            self.show_image("Pictures, icons//Staticmethods.png", max_width=1200, max_height=800)
        elif text == "@property Methods":
            pass
        elif text == "Magic Methods":
            self.show_image("Pictures, icons//Magic methods.png", max_width=1300, max_height=720)
        elif text == "@classmethods":
            self.show_image("Pictures, icons//Class Methods.png", max_width=1400, max_height=750)

class BasicsPage(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.setWindowTitle("Python Basics")

        # Toolbar
        toolbar = QToolBar("Basics Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Left actions
        self.intro_action = QAction("Introduction\nto Python", self)
        self.print_action = QAction("Printing", self)
        self.rules_action = QAction("Rules to remember", self)
        self.add_assign_action = QAction("Add and assign", self)
        self.if_elif_else_action = QAction("Conditional \nStatements", self)
        self.for_loops = QAction("for / while Loops", self)

        toolbar.addAction(self.intro_action)
        toolbar.addAction(self.print_action)
        toolbar.addAction(self.rules_action)
        toolbar.addAction(self.add_assign_action)
        toolbar.addAction(self.if_elif_else_action)
        toolbar.addAction(self.for_loops)

        # Spacer to push widgets right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        # Right-side dropdowns
        self.menu1 = QMenu("Collections", self)
        self.lists_action = QAction("Lists", self)
        self.tuples_action = QAction("Tuples", self)
        self.sets_action = QAction("Sets", self)
        self.dictionaries_action = QAction("Dictionaries", self)

        self.menu1.addAction(self.lists_action)
        self.menu1.addSeparator()
        self.menu1.addAction(self.tuples_action)
        self.menu1.addSeparator()
        self.menu1.addAction(self.sets_action)
        self.menu1.addSeparator()
        self.menu1.addAction(self.dictionaries_action)

        self.collections_menu = QAction("Collections", self)
        self.collections_menu.setMenu(self.menu1)

        toolbar.addAction(self.collections_menu)

        # Central Widget
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)

        # Header label
        self.header_label = QLabel("Welcome to Python")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setFont(QFont("Arial Black", 22))

        # Content stack
        self.content_stack = QStackedWidget()

        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)

        self.image_view = QLabel("Image here")
        self.image_view.setAlignment(Qt.AlignCenter)

        self.content_stack.addWidget(self.text_view)
        self.content_stack.addWidget(self.image_view)

        # Bottom bar
        bottom_bar = QHBoxLayout()
        self.back_btn = QPushButton("Back")
        self.addtional_btn = QPushButton("Additional")

        # CSS Styling
        self.back_btn.setObjectName("back")
        self.addtional_btn.setObjectName("additional")

        self.setStyleSheet("""
            QMainWindow{
                           background-image: url("Pictures, icons/GUI-background.png");
                           background-repeat: no-repeat;
                           background-position: center;
                           }
            QPushButton#back{
                           background-color: #292928;
                           color: white;
                           padding: 8px 28px;
                           border: 3px double;
                           font-size: 15px;
                           font-family: calibri;
                           font-weight: bold;
                           }
            QPushButton#back:hover{
                           background-color: #141414;
                           }
            QPushButton#additional{
                           background-color: #292928;
                           color: white;
                           padding: 8px 28px;
                           border: 3px double;
                           font-size: 15px;
                           font-family: calibri;
                           font-weight: bold;
                           }
            QPushButton#additional:hover{
                           background-color: #141414;
                           }
            QToolBar{
                           background-color: #262625;
                           spacing: 15px;
                           padding: 3px;
                           }
            QToolButton{
                           background-color: #2e2e2e;
                           color: #dbdbd9;
                           border-radius: 5px;
                           padding: 9px 16px;
                           margin: 3px 3px;
                           font-family: calibri;
                           font-size: 15px;
                           font-weight: bold;
                           }
            QToolButton:hover{
                           background-color: #3c3c3c;
                           }
            QToolButton:pressed{
                           background-color: #505050;
                           }
            QMenu{
                           background-color: #2b2b2b;
                           color: white;
                           border: 1px solid #444;
                           }
            QMenu::item{
                           padding: 6px 20px;
                           }
            QMenu::item:selected{
                           background-color: #3c3c3c;
                           }
            QLabel{
                           color: #c9c9c5;
                           }
""")

        bottom_bar.addWidget(self.back_btn)
        bottom_bar.addStretch()
        bottom_bar.addWidget(self.addtional_btn)

        # Assemble layout
        central_layout.addWidget(self.header_label)
        central_layout.addWidget(self.content_stack)
        central_layout.addLayout(bottom_bar)

        self.setCentralWidget(central_widget)

        self.start_up_image() # running the start up image

        # State variable
        self.current_topic = None
        self.addtional_btn.hide()

        # Signals / Events
        self.back_btn.clicked.connect(self.go_back)
        self.intro_action.triggered.connect(self.load_introduction)
        self.print_action.triggered.connect(self.load_printing)
        self.if_elif_else_action.triggered.connect(self.load_conditionals)
        self.rules_action.triggered.connect(self.load_rules)
        self.add_assign_action.triggered.connect(self.load_add_assign)
        self.lists_action.triggered.connect(self.load_lists)
        self.tuples_action.triggered.connect(self.load_tuples)
        self.sets_action.triggered.connect(self.load_sets)
        self.dictionaries_action.triggered.connect(self.load_dictionaries)
        self.for_loops.triggered.connect(self.load_loops)
        self.collections_menu.triggered.connect(self.load_collections)

    def update_additional_button(self):
        self.addtional_btn.hide() # Hide by default
        try:
            self.addtional_btn.clicked.disconnect()
        except TypeError:
            pass
       
        topic_map = {
            "lists": self.load_lists_methods,
            "tuples": self.load_tuples_methods,
            "sets": self.load_sets_methods,
            "dictionaries": self.load_dictionaries_methods
        }

        if self.current_topic in topic_map:
            self.addtional_btn.setText("Built-in Methods")
            self.addtional_btn.clicked.connect(topic_map[self.current_topic])
            self.addtional_btn.show()
    
    def show_text(self, path, header): # Text files method
        self.header_label.setText(header)
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            content = "Text file not found."

        if path.endswith(".md"):
            self.text_view.setMarkdown(content)
        else:
            self.text_view.setPlainText(content)

        self.content_stack.setCurrentWidget(self.text_view)

    def show_image(self, path, max_width=None, max_height=None): # Images method
        pixmap = MainWindow.rounded_pixmap(path, radius=25)

        if pixmap.isNull():
            self.image_view.setText("Image not found")
            self.content_stack.setCurrentWidget(self.image_view)
            return
        
        if max_width or max_height:
            pixmap = pixmap.scaled(
                max_width or pixmap.width(),
                max_height or pixmap.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        else:
            pixmap = pixmap.scaled(
                self.image_view.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        self.image_view.setPixmap(pixmap)
        self.content_stack.setCurrentWidget(self.image_view)

    def start_up_image(self): # Start up image method
        self.show_image(
            "Pictures, icons//PythonProgramming.png",
            max_width=1500,
            max_height=830
        )

    def load_introduction(self):
        self.current_topic = "intro"
        self.show_image("Pictures, icons//Intro.png", max_width=1500, max_height=830)
        self.header_label.setText("What is Python?")
        self.update_additional_button()
    
    def load_printing(self):
        self.current_topic = "printing"
        self.show_image("Pictures, icons//Print.png", max_width=1500, max_height=900)
        self.header_label.setText("Printing in Python")
        self.update_additional_button()

    def load_rules(self):
        self.current_topic = "rules"
        self.show_image("Pictures, icons//Rules_to_remember.png", max_width=1500, max_height=830)
        self.header_label.setText("Rules to remember in Python")
        self.update_additional_button()

    def load_add_assign(self):
        self.current_topic = "add_assign"
        self.show_image("Pictures, icons//Add_assign.png", max_width=1500, max_height=830)
        self.header_label.setText("Assignment operators in Python")
        self.update_additional_button()

    def load_conditionals(self):
        self.current_topic = "conditionals"
        self.show_image("Pictures, icons//Conditional_statements.png", max_width=1500, max_height=830)
        self.header_label.setText("Conditional statements in Python")
        self.update_additional_button()

    def load_loops(self):
        self.current_topic = "loops"
        self.show_image("Pictures, icons//for-while.png", max_width=1500, max_height=850)
        self.header_label.setText("For vs While loops in Python")
        self.update_additional_button()

    def load_collections(self):
        self.current_topic = "collections"
        self.show_image("Pictures, icons//collections_tutorial.png", max_width=1500, max_height=830)
        self.header_label.setText("Collections in Python")
        self.update_additional_button()

    def load_lists(self):
        self.current_topic = "lists"
        self.show_image("Pictures, icons//Lists_tutorial.png", max_width=1500, max_height=830)
        self.header_label.setText("Lists in Python (ordered + mutable)")
        self.update_additional_button()
    
    def load_tuples(self):
        self.current_topic = "tuples"
        self.show_image("Pictures, icons//tuples_tutorial.png", max_width=1500, max_height=830)
        self.header_label.setText("Tuples in Python (ordered + immutable)")
        self.update_additional_button()
    
    def load_sets(self):
        self.current_topic = "sets"
        self.show_image("Pictures, icons//sets_tutorial.png", max_width=1500, max_height=830)
        self.header_label.setText("Sets in Python (unordered + mutable + unique)")
        self.update_additional_button()

    def load_dictionaries(self):
        self.current_topic = "dictionaries"
        self.show_image("Pictures, icons//dictionaries_tutorial.png", max_width=1500, max_height=830)
        self.header_label.setText("Dictionaries in Python (mutable + key-value pairs)")
        self.update_additional_button()

    def load_lists_methods(self):
        self.show_image("Pictures, icons//list_methods.png", max_width=1500, max_height=830)
        self.header_label.setText("Built-in Methods for Lists")

    def load_tuples_methods(self):
        self.show_image("Pictures, icons//tuple_methods.png", max_width=1500, max_height=830)
        self.header_label.setText("Built-in Methods for tuples\nTuples have only 2 methods you can use, count() and index()")

    def load_sets_methods(self):
        self.show_image("Pictures, icons//set_methods.png", max_width=1500, max_height=830)
        self.header_label.setText("Built-in Methods for Sets")

    def load_dictionaries_methods(self):
        pass

    def showEvent(self, event): # Method to restart start_up_image when reloading the page
        super().showEvent(event)

        self.header_label.setText("Welcome to Python")
        self.current_topic = None
        self.addtional_btn.hide()
        self.start_up_image()
        
    def go_back(self):
        self.hide()
        self.parent_window.show()

class AdvancedPage(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.setWindowTitle("Python Advanced")

        title = QLabel("Python advanced / Frameworks")
        grid = QGridLayout()
        back_btn = QPushButton("Back")

        self.buttons = ["Advanced-Classes", "Math Library",
                   "OS Library\nFile writing/detection", "Pandas Library",
                   "Matplotlib library", "PyQt Framework",
                   "Django Framework", "Projects"
                   ]

        row = 0 # 👉
        col = 0 # 👇

        self.dialog_map = {
            "Advanced-Classes": ClassesAdvanced,
            "Math Library": MathDialog,
            "OS Library\nFile writing/detection": OSDialog,
            "Pandas Library": PandasDialog,
            "Matplotlib library": MatplotlibDialog,
            "PyQt Framework": PyQtDialog,
            "Django Framework": DjangoDialog,
            "Projects": ProjectsDialog
        }

        for text in self.buttons:
            button = QPushButton(text)
            grid.addWidget(button, row, col)

            button.clicked.connect(
                lambda checked, t=text: self.open_dialog(t)
            )

            col += 1
            if col > 1:
                col = 0
                row += 1

        self.master_layout = QVBoxLayout()
        self.master_layout.addWidget(title, alignment=Qt.AlignCenter|Qt.AlignTop)
        self.master_layout.addStretch()
        self.master_layout.addLayout(grid)
        self.master_layout.addStretch()

        button_row = QHBoxLayout()
        button_row.addWidget(back_btn, alignment=Qt.AlignLeft)

        self.master_layout.addLayout(button_row)

        central_widget = QWidget()
        central_widget.setLayout(self.master_layout)
        self.setCentralWidget(central_widget)

        back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.hide()
        self.parent_window.show()

    def open_dialog(self, title):
        dialog_class = self.dialog_map.get(title)

        if dialog_class:
            dialog = dialog_class(self, self.parent_window)
            dialog.exec()

class ClassesAdvanced(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("Advanced Classes in Python")
        self.resize(900, 700)

        self.layout = QVBoxLayout()
        self.label = QLabel(f"This is the Class Inheritance window")
        self.image_label = QLabel(self)
        self.initial_img = QPixmap("Pictures, icons//Classes_advanced.png")
        self.label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(self.initial_img)

        self.back_button = QPushButton("Back")
        self.init_button = QPushButton("__init__ Method")
        self.inherit_btn = QPushButton("Inheritance")
        self.polymorphism_btn = QPushButton("Polymorphism")
        self.enchapsulation_btn = QPushButton("Encapsulation")
        self.home_button = QPushButton("Home")

        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(self.label, alignment=Qt.AlignTop | Qt.AlignCenter)
        self.row2.addWidget(self.image_label, alignment=Qt.AlignCenter)
        self.row3.addWidget(self.back_button)
        self.row3.addWidget(self.init_button)
        self.row3.addWidget(self.inherit_btn)
        self.row3.addWidget(self.polymorphism_btn)
        self.row3.addWidget(self.enchapsulation_btn)
        self.row3.addWidget(self.home_button)

        self.layout.addLayout(self.row1)
        self.layout.addLayout(self.row2)
        self.layout.addLayout(self.row3)

        self.setLayout(self.layout)

        # Connecting Events
        self.back_button.clicked.connect(self.go_back)
        self.home_button.clicked.connect(self.go_home)

    def go_back(self):
        self.close()

    def go_home(self):
        self.close()
        self.previous_page.hide()
        self.main_window.show()

    def init_method(self):
        pass

    def inheritance(self):
        pass

    def polymorphism(self):
        pass

    def encapsulation(self):
        pass

class MathDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("Math Library in Python")

        layout = QVBoxLayout()
        label = QLabel(f"This is the Math library window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

class OSDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("OS library in Python")

        layout = QVBoxLayout()
        label = QLabel(f"This is the OS library window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

class PandasDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("Pandas Library in Python")

        layout = QVBoxLayout()
        label = QLabel(f"This is the Pandas library window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

class MatplotlibDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("MatplotLib Library in Python")

        layout = QVBoxLayout()
        label = QLabel(f"This is the Matplotlib library window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

class PyQtDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window
        self.setWindowTitle("PyQt5")

        layout = QVBoxLayout()
        label = QLabel(f"This is the PyQt Framework window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

class DjangoDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("Django Framework")

        layout = QVBoxLayout()
        label = QLabel(f"This is the Django Framework window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

class ProjectsDialog(QDialog):
    def __init__(self, previous_page, main_window):
        super().__init__()

        self.previous_page = previous_page
        self.main_window = main_window

        self.setWindowTitle("Projects")

        layout = QVBoxLayout()
        label = QLabel(f"This is the Projects window")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Test Button")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    training_manual = MainWindow()
    training_manual.show()
    sys.exit(app.exec_())