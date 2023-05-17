from flask import Flask, render_template



# Create app instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/type_selector')
def type_selector():
    return render_template('type_selector.html')

@app.route('/adjacent_sibling_combinator')
def adjacent_sibling_combinator():
    return render_template('adjacent_sibling_combinator.html')

@app.route('/attribute_selector')
def attribute_selector():
    return render_template('attribute_selector.html')

@app.route('/child_combinator')
def child_combinator():
    return render_template('child_combinator.html')

@app.route('/class_selector')
def class_selector():
    return render_template('class_selector.html')

@app.route('/containing_text_of_a_attribute')
def containing_text_of_a_attribute():
    return render_template('containing_text_of_a_attribute.html')

@app.route('/descendant_combinator')
def descendant_combinator():
    return render_template('descendant_combinator.html')

@app.route('/ending_text_of_a_attribute')
def ending_text_of_a_attribute():
    return render_template('ending_text_of_a_attribute.html')

@app.route('/first_of_type_selector')
def first_of_type_selector():
    return render_template('first_of_type_selector.html')

@app.route('/general_sibling_combinator')
def general_sibling_combinator():
    return render_template('general_sibling_combinator.html')

@app.route('/has_selector')
def has_selector():
    return render_template('has_selector.html')

@app.route('/id_selector')
def id_selector():
    return render_template('id_selector.html')

@app.route('/last_of_type_selector')
def last_of_type_selector():
    return render_template('last_of_type_selector.html')

@app.route('/not')
def not_():
    return render_template('not.html')

@app.route('/nth_last_of_type_selector')
def nth_last_of_type_selector():
    return render_template('nth_last_of_type_selector.html')

@app.route('/nth_child_n_selector')
def nth_child_n_selector():
    return render_template('nth_child_n_selector.html')

@app.route('/nth_of_type_n_selector')
def nth_of_type_n_selector():
    return render_template('nth_of_type_n_selector.html')

@app.route('/or')
def or_():
    return render_template('or.html')

@app.route('/practice1')
def practice1():
    return render_template('practice1.html')

@app.route('/practice2')
def practice2():
    return render_template('practice2.html')

@app.route('/pseudo_classes')
def pseudo_classes():
    return render_template('pseudo_classes.html')

@app.route('/pseudo_elements')
def pseudo_elements():
    return render_template('pseudo_elements.html')

@app.route('/selector_list')
def selector_list():
    return render_template('selector_list.html')

@app.route('/starting_text_of_a_attribute')
def starting_text_of_a_attribute():
    return render_template('starting_text_of_a_attribute.html')


# Run the app with debug mode
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
