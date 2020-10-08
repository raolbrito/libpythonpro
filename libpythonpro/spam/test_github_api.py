from libpythonpro import github_api


def test_buscar_avatar():
    url = github_api.buscar_avatar('raolbrito')
    assert 'https://avatars3.githubusercontent.com/u/66442402?v=4' == url
