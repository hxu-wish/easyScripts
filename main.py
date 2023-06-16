# This is a sample Python script.
import operator
import os


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def move_string():
    target_strings = ['no_products_found', 'wishlist', 'wishlist_select_items', 'profile_wishlist_empty_state_title',
                      'profile_wishlist_empty_state_subtitle', 'move', 'delete', 'edit', 'rename_list',
                      'wishlist_make_private', 'wishlist_make_public', 'add_to_cart',
                      'shop_related', 'wishlist_private_subtitle', 'wishlist_public_subtitle', 'choose_a_wishlist',
                      'create_a_new_wishlist', 'wishlist_suggestion', 'wishlist_name_hint', 'yes', 'no', 'done', 'ok',
                      'oops', 'rename_wishlist', 'are_you_sure', 'delete_entire_wishlist',
                      'are_you_sure_delete_wishlist', 'are_you_sure_remove_products', 'wishlist_view_count', 'item',
                      'create_wishlist_button_text']

    source_path = '/Users/hxu/Work/repo/onLine/android/app/src/main/res/'
    target_path = '/Users/hxu/Work/repo/onLine/android/wishlist-ui/src/main/res/'
    file_name = '/strings.xml'
    file_footer = '</resources>'
    file_header = '<?xml version="1.0" encoding="UTF-8"?>\n<resources xmlns:ns0="http://schemas.android.com/tools">\n'

    source_directory = os.listdir(source_path)
    filter_directory = [attr for attr in source_directory if
                        attr.startswith('values')]
    for item in target_strings:
        for package_name in filter_directory:
            allPath = source_path + package_name + file_name
            if os.path.exists(allPath):
                with open(allPath) as f:
                    plurals_flag = False
                    for line in f:
                        target_string = 'name="' + item + '"'
                        if operator.contains(line, target_string):
                            targetPackage = target_path + package_name
                            create_directory(targetPackage)

                            is_file_exist = os.path.exists(targetPackage + file_name)
                            file = open(targetPackage + file_name, 'a')
                            if not is_file_exist:
                                file.write(file_header)

                            if operator.contains(line, 'plurals'):
                                plurals_flag = True

                            file.write(line)

                            if target_strings.index(item) == len(target_strings) - 1:
                                file.write(file_footer)
                                file.close()
                        else:
                            if plurals_flag:
                                file.write(line)

                            if operator.contains(line, "</plurals>"):
                                plurals_flag = False



def create_directory(targetPackage):
    if os.path.exists(targetPackage):
        print('package is existed')
    else:
        os.makedirs(targetPackage)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    move_string()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
