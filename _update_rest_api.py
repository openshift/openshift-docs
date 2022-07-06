#!/usr/bin/env python2

import collections
import os
import shutil
import yaml
import yaml.dumper


# maintain order of yaml dictionaries
def dict_representer(dumper, data):
    return dumper.represent_dict(data.iteritems())


def dict_constructor(loader, node):
    return collections.OrderedDict(loader.construct_pairs(node))


yaml.add_representer(collections.OrderedDict, dict_representer)
yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                     dict_constructor)


def main():
    origin = os.environ.get("ORIGIN_REPO", "../origin")

    # clear out all subdirectories under rest_api
    for f in os.listdir("rest_api"):
        f = os.path.join("rest_api", f)
        if os.path.isdir(f):
            shutil.rmtree(f)

    # copy in subdirectories under rest_api from origin
    for f in os.listdir(os.path.join(origin, "api/docs")):
        srcp = os.path.join(origin, "api/docs", f)
        dstp = os.path.join("rest_api", f)
        if os.path.isdir(srcp):
            shutil.copytree(srcp, dstp)

    # read rest_api topics snippet from origin
    with open(os.path.join(origin, "api/docs/_topic_map.yml")) as f:
        topics = yaml.load(f)

    # read in existing _topic_map.yml
    preamble = ""
    with open("_topic_map.yml") as f:
        while True:
            line = f.readline()
            preamble += line
            if line == "" or line.strip() == "---":
                break

        docs = list(yaml.load_all(f))

    for doc in docs:
        if doc["Dir"] == "rest_api":
            # remove existing topics referencing subdirectories of rest_api
            doc["Topics"] = [t for t in doc["Topics"] if "Dir" not in t]

            # add rest_api topics snippet from origin
            doc["Topics"].extend(topics)

    # write out modified _topic_map.yml
    with open("_topic_map.yml", "w") as f:
        f.write(preamble)
        yaml.dump_all(docs, f, default_flow_style=False)


if __name__ == "__main__":
    main()
