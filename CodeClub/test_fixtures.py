import attr
import pytest

@attr.s
class Cat:
    name = attr.ib()
    main_color = attr.ib()
    supplementary_color = attr.ib()
    tertiary_color = attr.ib()
    tail_length = attr.ib()
    favourite_food = attr.ib()
    owner_first_name = attr.ib()
    owner_last_name = attr.ib()
    owner_phone_nr = attr.ib()
    is_checked_into_cathotel = attr.ib(default=False)
    is_neutered = attr.ib(default=False)
    vaccinations = attr.ib(factory=list)

    def check_in(self):
        self.is_checked_into_cathotel = True

    def check_out(self):
        self.is_checked_into_cathotel = False


@pytest.fixture
def that_cat():
    return Cat('Name', 'Color', 'Color2', 'color3', 2, 'fish', 'henri', 'kelder', 8188439, True, False, [1, 2, 3])


def test_check_cat_in(that_cat):
    that_cat.check_in()
    assert that_cat.is_checked_into_cathotel == True


def test_check_cat_out(that_cat):
    that_cat.check_out()
    assert that_cat.is_checked_into_cathotel == False