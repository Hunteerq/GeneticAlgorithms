from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QInputDialog, QLineEdit, QFormLayout


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.__title = "Genetic Algorithm"
        self.__init_ui()
        self.__add_text()
        self.__add_inputs()
        self.__add_buttons()
        self.show()

    def __init_ui(self):
        self.setWindowTitle(self.__title)
        self.setGeometry(1200, 800, 400, 400)

    def __add_text(self):
        main_text = QLabel()
        main_text.setText("Genetic Algorithm for finding max/min in Beale Function")
        main_text.setAlignment(Qt.AlignHCenter)
        layout = QVBoxLayout()
        layout.addWidget(main_text)
       # self.setLayout(layout)

    def __add_inputs(self):
        form_layout = QFormLayout()
        self.__epoch_number_input = QLineEdit()
        self.__epoch_number_input.setPlaceholderText('Epochs amount')
        form_layout.addRow(self.__epoch_number_input)
        self.__cross_prob_input = QLineEdit()
        self.__cross_prob_input.setPlaceholderText('Cross mutation probability')
        form_layout.addRow(self.__cross_prob_input)
        self.__cross_homo_prob_input = QLineEdit()
        self.__cross_homo_prob_input.setPlaceholderText('Homo cross mutation probability')
        form_layout.addRow(self.__cross_homo_prob_input)
        self.__mutation_prob_input = QLineEdit()
        self.__mutation_prob_input.setPlaceholderText('Mutation probability')
        form_layout.addRow(self.__mutation_prob_input)
        self.__inversion_prob_input = QLineEdit()
        self.__inversion_prob_input.setPlaceholderText('Inversion probability')
        form_layout.addRow(self.__inversion_prob_input)

        self.setLayout(form_layout)

    def __add_buttons(self):
        pass

