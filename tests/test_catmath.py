from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(10) == 50
    assert catmath.cat_years_to_hooman_years(11) != 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.2) == 1


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    # ...for a certain definition of "success."
    assert catmath.is_cat_leap_year(2011) is False
    assert catmath.is_cat_leap_year(2000) is True
    assert catmath.is_cat_leap_year(2016) is True
