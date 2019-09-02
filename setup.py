# coding: utf-8

"""
    Demisto API
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "demisto-py"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Demisto API",
    author_email="",
    url="https://github.com/demisto/demisto-py",
    keywords=["Swagger", "Demisto API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under &#39;Settings&#39; -&gt; &#39;Integrations&#39; -&gt; &#39;API keys&#39;   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass &#39;version\\: -1&#39; to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using &#39;curl&#39;\\:  &#x60;&#x60;&#x60; curl &#39;https://hostname:443/incidents/search&#39; -H &#39;content-type: application/json&#39; -H &#39;accept: application/json&#39; -H &#39;Authorization: &lt;API Key goes here&gt;&#39; --data-binary &#39;{\&quot;filter\&quot;:{\&quot;query\&quot;:\&quot;-status:closed -category:job\&quot;,\&quot;period\&quot;:{\&quot;by\&quot;:\&quot;day\&quot;,\&quot;fromValue\&quot;:7}}}&#39; --compressed &#x60;&#x60;&#x60;  # noqa: E501
    """
)
