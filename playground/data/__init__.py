import pkg_resources


def get_data_file(name):
  return pkg_resources.resource_filename('playground.data', name)
