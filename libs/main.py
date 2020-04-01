from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QComboBox

from libs.algorithm_configuration_provider import AlgorithmConfigurationProvider
from libs.selection_types import SelectionTypes


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.__title = "Genetic Algorithm"
        self.__init_ui()
        self.__form_layout = QFormLayout()
        self.__add_text()
        self.__add_inputs()
        self.__add_selection_method()
        self.__add_buttons()
        self.setLayout(self.__form_layout)
        self.show()

    def __init_ui(self):
        self.setWindowTitle(self.__title)
        # self.setGeometry(1200, 800, 400, 400)

    def __add_text(self):
        main_text = QLabel()
        main_text.setText("\nGenetic Algorithm for finding max/min in Beale Function\n\n")
        main_text.setAlignment(Qt.AlignHCenter)
        self.__form_layout.addWidget(main_text)

    def __add_inputs(self):
        self.__add_function_property_inputs()
        self.__add_algorithm_property_inputs()
        self.__add_prop_inputs()

    def __add_function_property_inputs(self):
        range_double_validator = QDoubleValidator()

        self.__a_range_input = QLineEdit()
        self.__a_range_input.setPlaceholderText('Begin of the range - a')
        self.__a_range_input.setValidator(range_double_validator)
        self.__form_layout.addRow(self.__a_range_input)

        self.__b_range_input = QLineEdit()
        self.__b_range_input.setPlaceholderText('End of the range - b')
        self.__b_range_input.setValidator(range_double_validator)
        self.__form_layout.addRow(self.__b_range_input)

    def __add_algorithm_property_inputs(self):
        only_int_validator = QIntValidator()

        self.__pop_amount_input = QLineEdit()
        self.__pop_amount_input.setPlaceholderText('Population amount')
        self.__pop_amount_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__pop_amount_input)

        self.__bits_amount_input = QLineEdit()
        self.__bits_amount_input.setPlaceholderText('Number of bits')
        self.__bits_amount_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__bits_amount_input)

        self.__epoch_number_input = QLineEdit()
        self.__epoch_number_input.setPlaceholderText('Epochs amount')
        self.__epoch_number_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__epoch_number_input)

        self.__max_time_input = QLineEdit()
        self.__max_time_input.setPlaceholderText('Max time in seconds')
        self.__max_time_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__max_time_input)

    def __add_prop_inputs(self):
        prop_double_validator = QDoubleValidator(0, 1, 8, self)
        prop_double_validator.setNotation(QDoubleValidator.StandardNotation)

        self.__cross_prob_input = QLineEdit()
        self.__cross_prob_input.setPlaceholderText('Cross probability')
        self.__cross_prob_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__cross_prob_input)

        self.__mutation_prob_input = QLineEdit()
        self.__mutation_prob_input.setPlaceholderText('Mutation probability')
        self.__mutation_prob_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__mutation_prob_input)

        self.__inversion_prob_input = QLineEdit()
        self.__inversion_prob_input.setPlaceholderText('Inversion probability')
        self.__inversion_prob_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__inversion_prob_input)

    def __add_selection_method(self):
        self.__selection_method_box = QComboBox()
        self.__selection_method_box.addItems(
            [
             SelectionTypes.BEST.name,
             SelectionTypes.ROULETTE.name,
             SelectionTypes.TOURNAMENT.name
            ]
        )
        self.__form_layout.addRow(self.__selection_method_box)

    def __add_buttons(self):
        self.__button = QPushButton("Start")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed())
        self.__form_layout.addRow(self.__button)

    def __handle_button_pressed(self):
        algorithm_config = self.__get_alg_config()

    def __get_alg_config(self):
        return AlgorithmConfigurationProvider(self.__a_range_input.text(),
                                              self.__b_range_input.text(),
                                              self.__bits_amount_input.text(),
                                              self.__pop_amount_input.text(),
                                              self.__epoch_number_input.text(),
                                              True)

