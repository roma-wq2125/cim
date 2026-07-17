import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLayout, QGridLayout,\
      QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class MainWIn(QWidget):
    def __init__(self):
        super().__init__()

        # Layouts
        #main
        mainlayout = QVBoxLayout()
        mainlayout.setContentsMargins(20,20,20,20)

        #Other
        other_layout = QHBoxLayout()
        other_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.settings_button = QPushButton("s")
        other_layout.addWidget(self.settings_button, alignment=Qt.AlignmentFlag.AlignLeft)


        #Str
        str_layout = QHBoxLayout()
        
        # Main textarea

        self.number = 0

        self.textarea = QLabel(f"{str(self.number)}")
    
        str_layout.addWidget(self.textarea, alignment=Qt.AlignmentFlag.AlignCenter)

        
        #Input
        input_layout = QGridLayout()
        input_layout.setSpacing(6)


        # First button group
        self.button0 = QPushButton("0")
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button_dot = QPushButton(".")
        self.button_mod = QPushButton("\\")

        # Second button group
        self.button_dif = QPushButton("/")
        self.button_mul = QPushButton("*")
        self.button_min = QPushButton("-")
        self.button_pl = QPushButton("+")
        self.button_eq = QPushButton("=")
        # Third button group
        self.button_del = QPushButton("Del")
        self.button_ac = QPushButton("AC")
        self.button_per = QPushButton("%")

        # Adding to layouts
        input_layout.addWidget(self.button_del, 0, 0)
        input_layout.addWidget(self.button_ac, 0, 1)
        input_layout.addWidget(self.button_dif, 0, 3)
        input_layout.addWidget(self.button_per, 0, 2)


        input_layout.addWidget(self.button7, 1, 0)
        input_layout.addWidget(self.button8, 1, 1)
        input_layout.addWidget(self.button_mul, 1, 3)
        input_layout.addWidget(self.button9, 1, 2)

        input_layout.addWidget(self.button4, 2, 0)
        input_layout.addWidget(self.button5, 2, 1)
        input_layout.addWidget(self.button6, 2, 2)
        input_layout.addWidget(self.button_min, 2, 3)

        input_layout.addWidget(self.button1, 3, 0)
        input_layout.addWidget(self.button2, 3, 1)
        input_layout.addWidget(self.button3, 3, 2)
        input_layout.addWidget(self.button_pl, 3, 3)

        input_layout.addWidget(self.button_mod, 4, 0)
        input_layout.addWidget(self.button0, 4, 1)
        input_layout.addWidget(self.button_dot, 4, 2)
        input_layout.addWidget(self.button_eq, 4, 3)

        # Strucuturing layouts
        self.setLayout(mainlayout)
        mainlayout.addLayout(other_layout)
        mainlayout.addLayout(str_layout)
        mainlayout.addLayout(input_layout)



## App init
app = QApplication()
window = MainWIn()
window.show()
sys.exit(app.exec())