

class App:
    def __init__(self, io, filehandler, referencehandler):
        self.io = io
        self.bib_file_path = "references.bib"
        #When the program starts filehandler gets references
        # from storage files and these are passed to refHandler
        self.fileHandler = filehandler
        self.referenceHandler = referencehandler

    def run(self):
        while True:
            self.io.write("Syötä 1 lisätäksesi viite")
            self.io.write("Syötä 2 listataksesi kaikki viitteet")
            self.io.write("Syötä 3 luodaksesi bibtext tiedosto")
            self.io.write("Paina enter lopettaaksesi")
            self.io.write("")
            command = self.io.read("Syötä komento: ")

            if not command:
                break

            if command == "1":
                #The input prompts for different ref classes need
                #to be interactive because different refs
                #have different fields
                try:
                    key = self.io.read("Avain: ")
                    author = self.io.read("Kirjailija: ")
                    title = self.io.read("Nimi: ")
                    year = self.io.read("Julkaisuvuosi: ")
                    publisher = self.io.read("Julkaisija: ")

                    #Inputs go as parameters to the object generation methods
                    self.referenceHandler.generate_book_reference_object([key, author, title,
                                                                        int(year), publisher])
                    self.io.write("")

                except Exception as error:
                    self.io.write(error)
                    self.io.write("\nJotain meni vikaan \n")
            elif command == "2":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references()
                    self.io.write("")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")
            elif command == "3":
                try:
                    self.fileHandler.write_bibtext_file(self.bib_file_path)
                    self.io.write("references.bib tiedosto luotu \n")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")