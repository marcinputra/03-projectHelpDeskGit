# Projekt helpDesk

### Opis:

Aplikacja rejestruje zdarzenia awarii komputerów. Użytkownik loguje się do aplikacji poprzez wcześniej założone konto. 
Po zalogowaniu może zobaczyć swoje zgłoszenia oraz stan ich lub dodać nowe. Może także modyfikować swoje otwarte zgłoszenia. Administrator może wykonywać wszyskie zadania użytkownika oraz dodatkowo może zamykać zgłoszenie.

### Wymagania:

Aplikacja została napisana na wersji Pythona 3.12. Potrzebne zależności i pakiety do działania aplikacji znajdują się w pliku `requirements.txt`.

Przed uruchomieniem aplikacji należy stworzyć bazę danych. Do utworzenia bazy należy z uruchmić plik `db_init.pl` foldery `.\data\`.  Zostanie utworzona baza danych z przykładowymi plikami.
Po utworzniu aplikacji możemy uruchomić aplikcję z pliku `app.py` znajdującego się folderze `.\helpDesk`. 
Do zalogownaia się jako użytkownik: user, z hasłem: 1234, zaś jako administrator: admin, z hasłem: 1234.
##### UWAGA.
Należy sprawdzić na jakim adresie i porcie jest uruchomiona aplikacja. Domyślnie jest to: `http://127.0.0.1:5000`.

### Autor aplikacji:

Marcin Putra (github: `https://github.com/marcinputra/03-projectHelpDeskGit`)