import json

def check_nesting_depth(obj, depth=0):
    if depth > 19:  # Max depth of 19 (20 levels including level 0).
        return False
    
    if isinstance(obj, list):
        # Recursively check the nesting depth of the list up to the base case.
        return all(check_nesting_depth(item, depth + 1) for item in obj)
    elif isinstance(obj, dict):
        # Recursively check the nesting depth of the dict up to the base case.
        return all(check_nesting_depth(value, depth + 1) for value in obj.values())
    
    return True

def is_valid_json(json_string):
    try:
        parsed = json.loads(json_string)
        # Check if the parsed JSON is a dict (object) or list (array). Will return false for strings, number or booleans, even though they are valid JSON values
        if not isinstance(parsed, (dict, list)):
            return False
        return check_nesting_depth(parsed)
    except ValueError:
        return False

def json_parse(filePath):
    try:
        # using "with" as a context manager to close the file once the block is completed or an exception is thrown
        with open(filePath, 'r') as f:
            f_contents = f.read()
        
        if not f_contents:  # Check if file is empty
            empty_file_msg = 'File empty', 1
            #print(empty_file_msg)
            return empty_file_msg
        elif is_valid_json(f_contents):
            valid_json_msg = "Valid JSON Object:", 0
            #print(valid_json_msg)
            return valid_json_msg
        else:
            invalid_json_msg = "Invalid JSON Object", 1
            #print(invalid_json_msg)
            return invalid_json_msg
    except FileNotFoundError:
        not_found_msg = "File not found"
        #print(not_found_msg)
        return not_found_msg



#json_parse("./dsa-trees/tests/step4/valid.json")
#json_parse("./dsa-trees/tests/step4/valid2.json")
#json_parse("./dsa-trees/tests/step4/invalid.json")
#json_parse("./dsa-trees/tests/step4/invalid2.json")

