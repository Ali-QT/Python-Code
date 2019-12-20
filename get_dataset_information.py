
def get_info(adata):
    """
    This function will print-out the information key in the data-set.
    The information contains: creation date, last update, creator name, description and Legal term.

    :param adata:
    :return: No returns
    """

    print('\n Information about Creatures data-set.')

    for each in adata['information']:
        for k in each.keys():
            print(' ', k + ": " + each[k])


