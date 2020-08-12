import decimal
from datetime import datetime
import pytz


def get_nigerian_time():
    tz_nigeria = pytz.timezone("Africa/Lagos")
    datetime_nigeria = datetime.now(tz_nigeria)
    return datetime_nigeria.strftime("%b-%d-%Y %H:%M:%S")
  


def full_clean(data):
    data = data.strip("\n")
    return data


def get_data(
    class_name: str, row, tag: str = "td",
):
    row_data = row.find(tag, class_=class_name)
    try:
        data = row_data.span.text
    except AttributeError:
        return None

    return full_clean(data)


def convert_str_to_float(value, delimiter: str, prefix: bool = False):
    """
    removes delimiter specifed in str 
    from value and returns a type of float
    """
    if value is None:
        return None
    assert delimiter in value, f"Delimeter '{delimiter}' specified not in {value}"

    value = value.split(delimiter)

    value = value[1] if prefix else value[0]
    # remove any ","
    value = value.translate({ord(","): None})
    return float(value)


def curry_function(func, *args, **kwargs):
    def func_passed_in(data):
        return func(data, *args, **kwargs)

    return func_passed_in


def get_change(data_set, func, table_body_row):
    """
    function : is a lamda expresion that defines how value of type 
    gets converted to type float.
    data_set is a tuple of list
    table_body_row data is being fetched from

    """
    for change in data_set:
        class_name = change[1]
        data = get_data(class_name, table_body_row)
        data = func(data)
        change.append(data)
    return data_set

