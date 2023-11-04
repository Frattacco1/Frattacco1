import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calcolatrice')
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.input_line = QLineEdit()
        self.layout.addWidget(self.input_line)

        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            'C', '0', '=', '/',
            '.', '√', '**'
        ]

        grid_layout = QGridLayout()

        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.button_click)
            if button == '=':
                grid_layout.addWidget(btn, row, col, 1, 1)
            else:
                grid_layout.addWidget(btn, row, col, 1, 1)
                
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.layout.addLayout(grid_layout)
        self.central_widget.setLayout(self.layout)

    def button_click(self):
        button = self.sender()
        if button.text() == '=':
            try:
                result = eval(self.input_line.text())
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText("ballz")
        elif button.text() == 'C':
            self.input_line.clear()
        else:
            current_text = self.input_line.text()
            new_text = current_text + button.text()
            self.input_line.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    calc.show()
    sys.exit(app.exec_())
