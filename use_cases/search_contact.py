

class SearchContact:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, mot_cle):
        resultat = []
        contacts = self.repository.get_all()
        for contact in contacts:
            if (
            mot_cle.lower() in contact.nom.lower()
               or mot_cle.lower() in contact.phone 
               or mot_cle.lower() in contact.email.lower()
            ):
                resultat.append(contact)
        return resultat