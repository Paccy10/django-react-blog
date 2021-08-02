import pytest


def test_user_str(base_user):
    """Test custom user model string representation"""

    username = base_user.__str__()

    assert username == f"{base_user.username}"


def test_user_short_name(base_user):
    """Test that the user model get_short_name method works"""

    short_name = base_user.get_short_name()

    assert short_name == f"{base_user.username}"


def test_base_user_email_is_normalized(base_user):
    """Test that the new base user email is normalized"""

    email = "person@API.COM"

    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(super_user):
    """Test that the new super user email is normalized"""

    email = "person@API.COM"

    assert super_user.email == email.lower()


def test_super_user_is_not_staff(user_factory):
    """Test that an error is raised when an admin user is_staff set to False"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email="", is_superuser=True, is_staff=False)

        assert str(err.value) == "Superusers must have is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    """Test that an error is raised when an admin user is_superuser set to False"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email="", is_superuser=False, is_staff=True)

        assert str(err.value) == "Superusers must have is_superuser=True"


def test_create_user_with_no_email(user_factory):
    """Test that creating a new user with no email address raises an error"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)

        assert str(err.value) == "User Account: An email address is required"


def test_create_user_with_no_username(user_factory):
    """Test that creating a new user with no username address raises an error"""

    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)

        assert str(err.value) == "Users must have a username"


def test_create_superuser_with_no_email(user_factory):
    """Test that creating a new super user with no email address raises an error"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)

        assert str(err.value) == "Superuser Account: An email address is required"


def test_create_user_with_incorrect_email(user_factory):
    """Test that creating a new user with an invalid email address raises an error"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email="trial.com")

        assert str(err.value) == "You must provide a valid email address"
