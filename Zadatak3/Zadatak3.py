avaliable_types = {
    'py':  'Python source kod',
    'pptx': 'Microsoft PowerPoint datoteka',
    'docx': 'Microsoft Word datoteka'
}

x = input('Vaša datoteka...')

ekstenzija = x.split('.')

print('Vaša datoteka ima ekstenziju .{}, to je {}.'.format(ekstenzija[1], avaliable_types[ekstenzija[1]]))