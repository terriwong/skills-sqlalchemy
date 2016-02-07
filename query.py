"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get('8')

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()  # stop by "Citroën" because ascii can't encode the special character.

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.discontinued < 1950) | (Brand.founded < 1950)).all()  # stop by "Citroën" because ascii can't encode the special character.

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    for model in models:

        print "model: %s, brand: %s, headquarters: %s" % (model.name, model.brand_name, model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_summary = {}

    models = Model.query.options(db.joinedload('brand')).all()

    for model in models:
        if model.brand_name not in brands_summary:
            brands_summary[model.brand_name] = []
            brands_summary[model.brand_name].append(model.name)
        else:
            brands_summary[model.brand_name].append(model.name)

    print brands_summary



# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# It returns an object from brand class where the brand name is 'Ford', the returned value include object attributes of id, name, founded, headquarters and discontinued.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# association table manages many-to-many relationship, 
# where it adds many-to-a relationship to left table and a-to-many relationship to the right table. 
# It only has columns of primary keys from both tables.
