class Group:

    def __init__(self, group_id, name, description):

        self.set_id(group_id)
        self.set_name(name)
        self.set_description(description)

    def set_id(self, group_id):

        if not isinstance(group_id, int):
            raise TypeError("Group ID must be an integer.")

        if group_id <= 0:
            raise ValueError("Group ID must be greater than zero.")

        self.id = group_id

    def set_name(self, name):

        if not isinstance(name, str):
            raise TypeError("Group name must be a string.")

        name = name.strip()

        if not name:
            raise ValueError("Group name cannot be empty.")

        if len(name) < 3:
            raise ValueError("Group name must contain at least 3 characters.")

        self.name = name.title()

    def set_description(self, description):

        if description is None:
            description = ""

        if not isinstance(description, str):
            raise TypeError("Description must be a string.")

        self.description = description.strip()

    def update_group(self, name, description):

        self.set_name(name)
        self.set_description(description)

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    def __str__(self):

        return (
            f"Group ID    : {self.id}\n"
            f"Group Name  : {self.name}\n"
            f"Description : {self.description}"
        )