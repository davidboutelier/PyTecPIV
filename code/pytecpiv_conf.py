def pytecpiv_get_pref():
    """
    This function checks the existence of a settings file in the working directory and returns the full paths to the
    sources and projects directory. If the settings files does not exist these paths are returned empty.
    :return: sources_path, projects_path - the full paths to the sources and the projects directory respectively
    """

    import os.path
    import json

    t = os.path.isfile('pytecpiv_settings.json')

    if t:
        with open('pytecpiv_settings.json') as f:
            pytecpiv_settings = json.load(f)
            sources = pytecpiv_settings['sources']
            sources = sources[0]
            sources_path = sources['sources_path']

            projects = pytecpiv_settings['projects']
            projects = projects[0]
            projects_path = projects['projects_path']

    else:
        sources_path = ''
        projects_path = ''
    return sources_path, projects_path
