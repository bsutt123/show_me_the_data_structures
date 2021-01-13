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

print(is_user_in_group(sub_child_user, parent))  # returns True
print(is_user_in_group(other_child_user, parent))  # returns False
print(is_user_in_group(sub_child_user, child))  # returns True
print(is_user_in_group(other_child_user, child))  # returns False
print(is_user_in_group(other_child_user, other_child))  # returns True
print(is_user_in_group(sub_child_user, sub_child))  # returns True

empty_group = Group("empty")

print(is_user_in_group("1", empty_group))  # returns False
print(is_user_in_group("badinput", empty_group))  # returns False

binary_tree_group = Group("root")
left_group = Group("left")
right_group = Group("right")

binary_tree_group.add_group(left_group)
binary_tree_group.add_group(right_group)

right_group.add_user("right_user_1")
right_group.add_user("right_user_2")
right_group.add_user("right_user_3")
left_group.add_user("left_user_1")
left_group.add_user("left_user_2")
left_group.add_user("left_user_3")

print(is_user_in_group("right_user_1", binary_tree_group))  # returns True
print(is_user_in_group("right_user_2", binary_tree_group))  # returns True
print(is_user_in_group("right_user_3", binary_tree_group))  # returns True

print(is_user_in_group("left_user_1", binary_tree_group))  # returns True
print(is_user_in_group("left_user_2", binary_tree_group))  # returns True
print(is_user_in_group("left_user_3", binary_tree_group))  # returns True

print(is_user_in_group("left_user_1", right_group))  # returns False
print(is_user_in_group("left_user_2", right_group))  # returns False
print(is_user_in_group("left_user_3", right_group))  # returns False

print(is_user_in_group("right_user_1", right_group))  # returns True
print(is_user_in_group("right_user_2", right_group))  # returns True
print(is_user_in_group("right_user_3", right_group))  # returns True

print(is_user_in_group("left_user_1", left_group))  # returns True
print(is_user_in_group("left_user_2", left_group))  # returns True
print(is_user_in_group("left_user_3", left_group))  # returns True

print(is_user_in_group("right_user_1", left_group))  # returns False
print(is_user_in_group("right_user_2", left_group))  # returns False
print(is_user_in_group("right_user_3", left_group))  # returns False
