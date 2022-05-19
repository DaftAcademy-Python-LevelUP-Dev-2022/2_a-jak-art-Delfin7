def greeter(func):
    def aloha(func2):
        return 'Aloha ' + func(func2).title()

    return aloha


def sums_of_str_elements_are_equal(func):
    def sums(func2):
        numbers = func(func2)
        transformed = ''
        temp_sum, num_1, num_2 = 0, 0, 0
        for char in numbers:
            if char == '-':
                transformed += char
            elif char == ' ':
                transformed = transformed + str(temp_sum) + char
                num_1 = temp_sum
                temp_sum = 0
            else:
                temp_sum += int(char)
        else:
            transformed += str(temp_sum)
            num_2 = temp_sum
            if numbers.count('-') in (0, 2) and num_1 == num_2:
                transformed = transformed.replace(' ', ' == ')
            else:
                transformed = transformed.replace(' ', ' != ')
        return transformed

    return sums


def format_output(*required_keys):
    def outer_wrapper(func):
        def wrapper(func2):
            dictionary_formatted = {i: '' for i in required_keys}
            list_split_formatted_keys, list_keys = [], []
            for key in dictionary_formatted:
                list_split_formatted_keys += key.split('__')
            for key in func(func2):
                list_keys.append(key)
            for item in list_split_formatted_keys:
                if item not in list_keys:
                    raise ValueError
            temp = ''
            for key in dictionary_formatted:
                for char in key:
                    if char == '_' and temp[-1] == '_':
                        for second_key in func(func2):
                            if second_key == temp[:-1]:
                                if dictionary_formatted[key] != '':
                                    dictionary_formatted[key] += " "
                                if func(func2)[second_key] == '':
                                    dictionary_formatted[key] += 'Empty value'
                                else:
                                    dictionary_formatted[key] += func(func2)[second_key]
                                break
                        temp = ''
                    else:
                        temp += char
                else:
                    for second_key in func(func2):
                        if second_key == temp:
                            if dictionary_formatted[key] != '':
                                dictionary_formatted[key] += " "
                            if func(func2)[second_key] == '':
                                dictionary_formatted[key] += 'Empty value'
                            else:
                                dictionary_formatted[key] += func(func2)[second_key]
                            break
                    temp = ''
            return dictionary_formatted

        return wrapper

    return outer_wrapper


def add_method_to_instance(klass):
    def outer_wrapper(fun):
        setattr(klass, fun.__name__, lambda function: fun())

        def wrapper():
            return fun()

        return wrapper

    return outer_wrapper
