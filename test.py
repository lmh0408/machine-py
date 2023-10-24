import os

def get_file_category(file_name):
  """Extracts the category of a file from its file name.

  Args:
    file_name: The name of the file.

  Returns:
    The category of the file, or None if the file name does not contain a category.
  """

  category = None
  try:
    print(file_name.split(os.sep))
    print('------------------------')
    print(file_name.split(os.sep)[0])
    print(file_name.split(os.sep)[1])
    print(file_name.split(os.sep)[2])

    print(file_name.split(os.sep)[2].split('_')[0])

    category = file_name.split(os.sep)[1].split('_')[0]
  except IndexError:
    pass

  return category


# Example usage:

# file_name = "3_data_2023_10_24.csv"
file_name = "./news/3_SEUNG-HWAN OH SHUTS DOWN TWINS IN FIRST SPRING ACTION.txt"

category = get_file_category(file_name)

print(category)
