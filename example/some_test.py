from some_stuff import camel_to_snake_case

def test_camel_to_snake_case():
    assert camel_to_snake_case("python") == "python"
    assert camel_to_snake_case("JavaScript") == "java_script"
    assert camel_to_snake_case("myFunctionName") == "my_function_name"
