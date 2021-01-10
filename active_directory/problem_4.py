class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.users_dict = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)
        self.users_dict[user] = True

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users_dict:
        return True

    groups = group.get_groups()

    for g in groups:
        in_group = is_user_in_group(user, g)
        if in_group:
            return True

    return False


parent = Group("parent")
child = Group("child")
other_child = Group("other_child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
other_child_user = "other_child_user"
sub_child.add_user(sub_child_user)

other_child.add_user(other_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))                 # returns True
print(is_user_in_group(other_child_user, parent))               # returns False
print(is_user_in_group(sub_child_user, child))                  # returns True
print(is_user_in_group(other_child_user, child))                # returns False
print(is_user_in_group(other_child_user, other_child))          # returns True
print(is_user_in_group(sub_child_user, sub_child))              # returns True