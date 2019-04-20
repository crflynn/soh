import pytest


# clipboard
@pytest.fixture(params=[None, "-c", "--clip"])
def clip(request):
    return request.param


# uuid
@pytest.fixture(params=[None, 1, 2, 3, 4, 5])
def uuid_version(request):
    return request.param


@pytest.fixture(params=["-v", "--version"])
def uuid_version_label(request):
    return request.param


@pytest.fixture(params=[None, "dns", "url", "oid", "x500", "invalid"])
def uuid_namespace(request):
    return request.param


@pytest.fixture(params=["-ns", "--namespace"])
def uuid_namespace_label(request):
    return request.param


@pytest.fixture(params=[None, "something"])
def uuid_name(request):
    return request.param


@pytest.fixture(params=["-n", "--name"])
def uuid_name_label(request):
    return request.param


# upper case results
@pytest.fixture(params=[None, "-u", "--upper"])
def upper(request):
    return request.param


# base 64
@pytest.fixture(params=["something"])
def sample_text(request):
    return request.param


# "something" b64encoded
@pytest.fixture(params=["c29tZXRoaW5n"])
def sample_b64(request):
    return request.param


# epoch
@pytest.fixture(params=[None, "-f", "--float"])
def float_(request):
    return request.param


# serve
@pytest.fixture(params=[None, "-p", "--port"])
def port_label(request):
    return request.param


# datetime
@pytest.fixture(params=[None, "-t"])
def t(request):
    return request.param


# json
@pytest.fixture(params=[None, "-i", "--indent"])
def indent_label(request):
    return request.param


@pytest.fixture(params=[2, 3, 5])
def indent(request):
    return request.param


@pytest.fixture(params=[None, "-a", "--ascii"])
def ascii(request):
    return request.param


json_sample = """'{"a":"b","c":1,"d":{"e":"f"}"g":[1,2,3],"s":"♣"}'"""
json_sample_bad = """'{"a":"b","c":1,"d":{"e":"f"}"g":[1,2,3],"s":"♣"'"""


@pytest.fixture(params=[json_sample, json_sample_bad])
def json_text(request):
    return request.param


# create
@pytest.fixture(params=[None, "-o", "--overwrite"])
def overwrite(request):
    return request.param


@pytest.fixture(params=["python", "list", "invalid_language"])
def language(request):
    return request.param
