

class ClassModifier():

    def class_to_list(self, class_name):
        dict_object = class_name.__dict__
        list_obj = list(dict_object.values())

        return list_obj

    def class_to_dictionary(self, class_name):
        dict_object = class_name.__dict_
        return dict_object