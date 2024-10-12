from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QFrame, QHBoxLayout
from utils import extract_text_of, text_to_speech
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class PDFApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PDF VOCAL READER')
        self.setGeometry(100, 100, 500, 300)

        # Style global
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
                margin: 25px;
            }
            QPushButton {
                background-color: #BB86FC;
                color: #101010;
                border-radius: 15px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #AA86FC;
            }
        """)

        layout = QVBoxLayout()

        # Titre
        title = QLabel('PDF CONVERTER TO AUDIO')
        title.setFont(QFont('Helvetica', 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(title)

        # Bouton de sélection de fichier
        self.browse_button = QPushButton('SELECT YOUR PDF FILE')
        self.browse_button.setFont(QFont('Helvetica', 12))
        self.browse_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.browse_button)

        # Pour les historiques
        self.under_title = QLabel('HISTORIC')
        self.under_title.setFont(QFont('Helvetica', 16, QFont.Weight.Bold))
        self.under_title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.inner_widget = QWidget()
        self.inner_layout = QHBoxLayout(self.inner_widget)
        self.inner_layout.addWidget(self.under_title)
        self.inner_widget.setStyleSheet("background-color: #333333;")
        layout.addWidget(self.inner_widget)

        # Label pour afficher le fichier sélectionné
        self.file_label = QLabel('')
        self.file_label.setFont(QFont('Helvetica', 10))
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.file_label)

        self.setLayout(layout)

    # Fonction pour ouvrir le dialogue de sélection de fichier
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "CHOOSE A PDF FILE", "", "PDF Files (*.pdf)")

        if file_path:
            self.file_label.setText(f"Fichier sélectionné : {file_path}")
            # Extraire le texte et lire à haute voix
            text = extract_text_of(file_path)  # Utiliser la fonction importée
            text_to_speech(text)  # Appeler la fonction d'énonciation
        else:
            self.file_label.setText("Aucun fichier sélectionné.")